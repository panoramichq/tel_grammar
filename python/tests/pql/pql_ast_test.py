import sys
sys.path.append('./src')

from antlr4 import CommonTokenStream, InputStream, ParserRuleContext
from antlr4.tree import Tree
from dataclasses import dataclass
from collections import namedtuple
from typing import Optional, Tuple
from unittest import mock, TestCase

from pql_grammar.antlr.PqlLexer import PqlLexer
from pql_grammar.antlr.PqlParser import PqlParser
from pql_grammar.antlr.PqlParserVisitor import PqlParserVisitor
from pql_grammar import operators as op
from pql_grammar.ast import model as ast


def full_text(ctx: ParserRuleContext) -> str:
    # extracts full text from a tree of nodes,
    # including white space.
    if ctx:
        if isinstance(ctx, ParserRuleContext):
            return ctx.start.getInputStream().getText(ctx.start.start, ctx.stop.stop)
        else:
            try:
                # some primitive context object
                return ctx.text
            except AttributeError:
                # Terminal Node of some sort
                return str(ctx)
    else:
        return None


def unquote(s: str):
    # Quoted schema, table, column names come in Postgres style - double-quotes
    # in-string double-quotes are escaped by doubling the double-quotes ANSI SQL style.
    # https://docs.oracle.com/goldengate/1212/gg-winux/GWURF/gg_parameters183.htm#GWURF728
    # Example:
    #   '"table name ""with quoted portion"""' becomes 'table name "with quoted portion"'
    if not s:
        return s
    if s[0] == '"' and s[-1] == '"':
        s = s[1:-1]
    return s.replace('""', '"')


class AstParser:

    @classmethod
    def unwrap_expr_parens(cls, e: PqlParser.ExprContext) -> PqlParser.ExprContext:
        # it's allowed to wrap expressions into superflous amounts of parens
        #   (((column > 5)))
        # These come across as triple-nested [TerminalNodeImpl('('), expr, TerminalNodeImpl(')')]
        # Here we check for len == 3 and if last and first Terminals are (), return middle element - expression,
        # Run this recursively.
        # inner attribute is enabled only on cleanly-paren-wrapped expressions
        if e.inner:
            return cls.unwrap_expr_parens(e.inner)
        else:
            return e

    @classmethod
    def parse_taxon(cls, e: PqlParser.TaxonContext) -> ast.Taxon:
        return ast.Taxon(
            full_text(e.slug),
            full_text(e.namespace),
            bool(e.is_optional),
            full_text(e.tag)
        )

    @classmethod
    def parse_function_argument_pair(cls, e: PqlParser.ExprContext) -> Tuple[Optional[str],str]:
        e = cls.unwrap_expr_parens(e)
        o = full_text(e.operator)
        if o == '=':
            arg_name = full_text(e.left)
            arg_value = full_text(e.right)
        else:
            arg_name = None
            arg_value = full_text(e)
        return (arg_name, arg_value)

    @classmethod
    def parse_function(cls, e: PqlParser.FunctionContext) -> ast.Function:
        return ast.Function(
            full_text(e.function_name),
            [
                cls.parse_function_argument_pair(expr)
                for expr in e.arguments.expr()
            ]
        )

    @classmethod
    def parse_column_value(cls, v: PqlParser.expr) -> ast.Values:
        # v is always PqlParser.expr, but anything can be inside
        # It's not super relevant what's inside Expr, since
        # we sent the original string-ified version of contenst to Husky anyway.
        # There are some good reasons to parse the value for realz:
        # - understanding if there is an outter `CAST( expr as TypeCast())` in there that needs re-syntaxing
        # - deciding if specific value is taxon AND if it's in or is not in WHERE clause to channel it to pre/post agg
        # However, we can do that crudely just on string representations of contents and avoid parsing them.
        # Still, let's try to parse top level into one of:
        # - Taxon
        # - TelExpr where all other kinds of complex expressions are packed
        # Specifically note that we allow Literal, Function other otherwise basic structures to be packed into Tel box.

        # So, if it's not Taxon object at top level, we unwrap redundant parens and pack string into TelExpr
        v = cls.unwrap_expr_parens(v)

        t: Optional[PqlParser.TaxonContext] = v.taxon()
        if t:
            return cls.parse_taxon(t)
        else:
            return ast.TelExpr(full_text(v))

    @classmethod
    def parse_column_typecast(cls, v: PqlParser.FunctionContext) -> Optional[ast.Function]:
        if not v:
            return None
        return cls.parse_function(v)

    @classmethod
    def parse_column_alias(cls, v: PqlParser.TaxonContext) -> Optional[ast.Taxon]:
        if not v:
            return None
        return cls.parse_taxon(v)

    @classmethod
    def parse_column(cls, e: PqlParser.ColumnsContext):
        return ast.Column(
            cls.parse_column_value(e.value),
            cls.parse_column_typecast(e.type_cast),
            cls.parse_column_alias(e.alias)
        )

    @staticmethod
    def _literalValue_to_python_native(e:PqlParser.LiteralValueContext):
        is_number = e.NUMERIC_LITERAL()
        is_string = e.DOUBLE_QUOTED_STRING() or e.SINGLE_QUOTED_STRING()
        is_null = e.K_NULL()
        is_bool = e.K_TRUE() or e.K_FALSE()

        # TODO:
        # - BLOB_LITERAL
        # - CURRENT_[DATE|TIME|TIMESTAMP]

        if is_null:
            return None

        if is_bool:
            return bool(e.K_TRUE())

        try:
            v = e.getText()
        except IndexError:
            raise Exception(f"Could not extract literal value node from '{e.getText()}'.")

        if is_number:
            # TODO: contemplate decimal type instead
            try:
                return int(v)
            except ValueError:
                try:
                    return float(v)
                except Exception:
                    raise Exception(f"Could not convert SQL number {v} to native number representation.")

        if is_string:
            return unquote(v)

        return v

    _sql_name_map = {
        'AND': op.OpName.AND,
        'OR': op.OpName.OR,
        'NOT': op.OpName.NOT,
        'IS': op.OpName.IS,
        '=': op.OpName.EQ,  # notice WHERE clause specific handling. NOT assignment. EQ!
        '==': op.OpName.EQ,  # opportunistic inclusion, while we don't expect to see it in WHERE
        '<>': op.OpName.NEQ,
        '!=': op.OpName.NEQ,  # opportunistic inclusion, while we don't expect to see it in WHERE
        '>': op.OpName.GT,
        '>=': op.OpName.GTE,
        '<': op.OpName.LT,
        '<=': op.OpName.LTE,
        'LIKE': op.OpName.LIKE,
        '+':op.OpName.PLUS,
        '-':op.OpName.MINUS,
        '*':op.OpName.STAR,
        '/':op.OpName.DIV,
        '%':op.OpName.MOD,
    }

    @classmethod
    def _lookup_operator_internal_name(cls, sql_operator: str):
        op_name = cls._sql_name_map.get(sql_operator.upper())
        if not op_name:
            raise Exception(f"Could not match operator '{sql_operator}' in where clause to a supported action.")
        return op_name

    @classmethod
    def parse_where_clause_expr(cls, ctx: PqlParser.ExprContext) -> ast.Node :
        ctx = cls.unwrap_expr_parens(ctx)

        v = ctx.literalValue()
        if v:
            return ast.Literal(
                cls._literalValue_to_python_native(v),
                full_text(v)
            )

        v = ctx.unary_operator
        if v:
            operator = full_text(v).upper()
            return ast.Expr(
                operator,
                [cls.parse_where_clause_expr(ctx.right)]
            )

        v: Optional[str] = full_text(ctx.operator)
        if v:
            # this is super generic expression of type
            #  left OP right
            # with a lot of options for OP value.
            return ast.Expr(
                v.upper(),
                [
                    cls.parse_where_clause_expr(ctx.left),
                    cls.parse_where_clause_expr(ctx.right)
                ]
            )

        v: PqlParser.TaxonContext = ctx.taxon()
        if v:
            return cls.parse_taxon(v)

        v: PqlParser.FunctionContext = ctx.function()
        if v:
            return cls.parse_function(v)

        raise Exception(f'Where expression "{full_text(ctx)}" is not supported yet.')


class AssertPqlVisitor(PqlParserVisitor):
    """
    Special TelVisitor for testing grammar. Throws error in case of invalid node.
    """
    def visitErrorNode(self, node):
        wrong_symbol = node.symbol.text
        position = node.symbol.column + 1
        details = f'Unexpected symbol "{wrong_symbol}" at position {position}'
        raise AssertionError(details)

    @classmethod
    def parse_string(cls, s):
        inp_stream = InputStream(s)
        lexer = PqlLexer(inp_stream)
        stream = CommonTokenStream(lexer)
        parser = PqlParser(stream)
        tree = parser.parsePql()
        # Use error visitor on parsed tree to test it
        visitor = cls()
        visitor.visit(tree)


class PqlAstTests(TestCase):
    maxDiff = None

    def test_select(self):

        pql = """
            select
                ?ns1|taxon1,
                ns2|taxon2,
                slug1 as myns|slug1,
                (?ns3|taxon3 + (slug2 - 1234)) as myns|custom_data,
                fn_4(fn_1(slug))::TypeCast(arg1=value1)
            where
                ns6|taxon6 > 1234
                and (ns0|taxon10 + 4321) == 0
        """

        statements = []

        class V(AssertPqlVisitor):
            def visitSelectStmt(self, ctx:PqlParser.SelectStmtContext):
                columns = [
                    ast.Column(
                        AstParser.parse_column_value(column.value),
                        AstParser.parse_column_typecast(column.type_cast),
                        AstParser.parse_column_alias(column.alias)
                    )
                    for column in ctx.selectClause().columns()
                ]
                where_clause = AstParser.parse_where_clause_expr(ctx.whereClause().expr())

                statements.append(ast.SelectStmt(
                    columns,
                    where_clause
                ))

        V.parse_string(pql)

        stmt_should_be = ast.SelectStmt(
            [
                ast.Column(ast.Taxon('taxon1', 'ns1', True)),
                ast.Column(ast.Taxon('taxon2', 'ns2', False)),
                ast.Column(ast.Taxon('slug1'), None, ast.Taxon('slug1', 'myns')),
                ast.Column(
                    ast.TelExpr('?ns3|taxon3 + (slug2 - 1234)'),
                    None,
                    ast.Taxon('custom_data', 'myns')
                ),
                ast.Column(
                    ast.TelExpr('fn_4(fn_1(slug))'),
                    ast.Function(
                        'TypeCast',
                        [('arg1','value1')]
                    ),
                )
            ],
            ast.Expr(
                'AND',
                [
                    ast.Expr(
                        '>',
                        [
                            ast.Taxon('taxon6', 'ns6'),
                            ast.Literal(1234, '1234')
                        ]
                    ),
                    ast.Expr(
                        '==',
                        [
                            ast.Expr(
                                '+',
                                [
                                    ast.Taxon('taxon10', 'ns0'),
                                    ast.Literal(4321, '4321')
                                ]
                            ),
                            ast.Literal(0, '0')
                        ]
                    )
                ]
            )
        )

        assert statements
        stmt = statements[0]

        assert len(stmt.columns) == len(stmt_should_be.columns)
        for result, should_be in zip(stmt.columns, stmt_should_be.columns):
            assert result == should_be

        # ast.ast_diff(stmt.where_clause, stmt_should_be.where_clause)
        assert stmt.where_clause == stmt_should_be.where_clause

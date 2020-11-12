import sys
sys.path.append('./src')

from antlr4 import CommonTokenStream, InputStream, ParserRuleContext
from antlr4.tree import Tree
from dataclasses import dataclass
from collections import namedtuple
from typing import Optional
from unittest import mock, TestCase

from pql_grammar.antlr.PqlLexer import PqlLexer
from pql_grammar.antlr.PqlParser import PqlParser
from pql_grammar.antlr.PqlParserVisitor import PqlParserVisitor
from pql_grammar import operators as op


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


class WhereClauseParser:

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
    def _unwrap_expr_parens(cls, e: PqlParser.ExprContext) -> PqlParser.ExprContext:
        # it's allowed to wrap expressions into superflous amounts of parens
        #   (((column > 5)))
        # These come across as triple-nested [TerminalNodeImpl('('), expr, TerminalNodeImpl(')')]
        # Here we check for len == 3 and if last and first Terminals are (), return middle element - expression,
        # Run this recursively.
        if e.inner:
            return cls._unwrap_expr_parens(e.inner)
        else:
            return e

    @classmethod
    def _lookup_operator_internal_name(cls, sql_operator: str):
        op_name = cls._sql_name_map.get(sql_operator.upper())
        if not op_name:
            raise Exception(f"Could not match operator '{sql_operator}' in where clause to a supported action.")
        return op_name

    @classmethod
    def _parse_where_clause_expr(cls, ctx: PqlParser.ExprContext) -> op.OperatorSchema :
        ctx = cls._unwrap_expr_parens(ctx)
        v = ctx.literalValue()
        if v:
            return op.schema_literal(cls._literalValue_to_python_native(v))

        v = ctx.unary_operator
        if v:
            operator = cls._lookup_operator_internal_name(full_text(v))
            if operator in (op.OpName.PLUS, op.OpName.MINUS):
                return op.schema_stanza(
                    operator,
                    op.schema_literal(0),
                    cls._parse_where_clause_expr(ctx.right),
                )
            if operator == op.OpName.NOT:
                return op.schema_stanza(
                    operator,
                    cls._parse_where_clause_expr(ctx.right),
                )

        v: PqlParser.taxon = ctx.taxon()
        if v:
            return op.schema_stanza(
                op.OpName.attr,
                op.schema_literal(full_text(v))
            )

        # v: PqlParser.NullComparisonContext = ctx.nullComparison()
        # if v:
        #     # Note, converting `V is (NOT) null`
        #     # into SQL-incompatible `V ==/!= null` that we CAN do in python.
        #     # Mostly to avoid creating redundant operators module code.
        #     is_negated = bool(v.K_NOT() or v.K_NOTNULL())
        #     if is_negated:
        #         return op.schema_stanza(
        #             op.OpName.NOT,
        #             op.schema_stanza(
        #                 op.OpName.IS,
        #                 cls._parse_where_clause_expr(ctx.left),
        #                 op.schema_literal(None)
        #             )
        #         )
        #     else:
        #         return op.schema_stanza(
        #             op.OpName.IS,
        #             cls._parse_where_clause_expr(ctx.left),
        #             op.schema_literal(None)
        #         )

        v: Optional[str] = full_text(ctx.operator)
        if v:
            # this is super generic expression of type
            #  left (NOT) OP right
            # with a lot of options for OP value.
            # not all of these values are supported by our `operators` module logic.
            # Next call throws errors for unmatched operators
            operator = cls._lookup_operator_internal_name(v)
            _rv = op.schema_stanza(
                operator,
                cls._parse_where_clause_expr(ctx.left),
                cls._parse_where_clause_expr(ctx.right),
            )
            # if bool(ctx.is_negated):
            #     return op.schema_stanza(
            #         op.OpName.NOT,
            #         _rv
            #     )
            # else:
            return _rv

        # v = ctx.K_IN()
        # if v:
        #     if ctx.compoundSelectStmt():
        #         raise Exception(f'Where expression "{full_text(ctx.compoundSelectStmt())}" is not supported yet.')
        #     expressions = ctx.expressions()
        #     if expressions:
        #         comps = [
        #             cls._parse_where_clause_expr(expr)
        #             for expr in expressions.expr()
        #         ]
        #         # converting these into multiple OR equal
        #         left = cls._parse_where_clause_expr(ctx.left)
        #         clause = op.schema_stanza(
        #             op.OpName.OR,
        #             *[
        #                 op.schema_stanza(
        #                     op.OpName.EQ,
        #                     left,
        #                     comp
        #                 )
        #                 for comp in comps
        #             ]
        #         )
        #         if bool(ctx.is_negated):
        #             return op.schema_stanza(
        #                 op.OpName.NOT,
        #                 clause,
        #             )
        #         else:
        #             return clause

        if ctx.function():
            raise NotImplementedError('Dont know how to pack functions yet')

        raise Exception(f'Where expression "{full_text(ctx)}" is not supported yet.')


class AssertPqlVisitor(PqlParserVisitor, WhereClauseParser):
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


class PQLTests(TestCase):
    maxDiff = None

    def test_select_no_filter(self):

        pql = """
            select
                ?ns1|taxon1,
                ?ns2|taxon2,
                slug1 as myns|slug1,
                (?ns3|taxon3 + (slug2 - 1234)) as myns|custom_data,
                fn_4(fn_1(slug))::TypeCast(arg1=value1)
            where
                ns6|taxon6 > 1234
                and (ns0|taxon10 + 1234) == 0
        """

        @dataclass
        class Column:
            value:str
            type_cast:Optional[str] = None
            alias:Optional[str] = None

        columns = []
        where_clause = []
        class V(AssertPqlVisitor):
            def visitColumns(self, ctx:PqlParser.ColumnsContext):
                column : PqlParser.ColumnContext
                for column in ctx.column():
                    v = full_text(column.value)
                    type_cast = full_text(column.type_cast.function()) if column.type_cast else None
                    alias = full_text(column.alias)
                    columns.append(Column(v, type_cast, alias))
            def visitWhereClause(self, ctx:PqlParser.WhereClauseContext):
                ww = self._parse_where_clause_expr(ctx.expr())
                where_clause.extend(ww)

        V.parse_string(pql)

        assert columns == [
            Column('?ns1|taxon1'),
            Column('?ns2|taxon2'),
            Column('slug1', None, 'myns|slug1'),
            Column('(?ns3|taxon3 + (slug2 - 1234))', None, 'myns|custom_data'),
            Column('fn_4(fn_1(slug))', 'TypeCast(arg1=value1)')
        ]
        assert where_clause == [
            'AND',
            ['GT',
                ['attr',
                    ['@literalValue', 'ns6|taxon6']
                ],
                ['@literalValue', 1234]
            ],
            ['EQ',
                ['PLUS',
                    ['attr',
                        ['@literalValue', 'ns0|taxon10']
                    ],
                    ['@literalValue', 1234]
                ],
                ['@literalValue', 0]
            ]
        ]

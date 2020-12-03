# fmt: off

from antlr4 import CommonTokenStream, InputStream, ParserRuleContext
from antlr4 import ParserRuleContext
from typing import Optional, Tuple, List, Type, Any

from ..antlr.PqlLexer import PqlLexer
from ..antlr.PqlParser import PqlParser
from ..antlr.PqlParserVisitor import PqlParserVisitor as _PqlParserVisitor

from . import model as ast


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
    wrapper = (s[0], s[-1])
    if wrapper == ('"', '"') or wrapper == ("'", "'"):
        s = s[1:-1]

    # TODO: decide which one we want to support
    # TEL style escapes
    return s.replace('\\"', '"').replace("\\'", "'")
    # # SQL style escapes
    # return s.replace('""', '"').replace("''", "'")


class PqlAntlrToAstParser:

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
    def parse_function_argument_pair(cls, e: PqlParser.ExprContext) -> Tuple[Optional[str],Any]:
        e = cls.unwrap_expr_parens(e)
        o = full_text(e.operator)
        if o == '=':
            arg_name = full_text(e.left)
            arg_value = cls.parse_expr(e.right)
        else:
            arg_name = None
            arg_value = cls.parse_expr(e)
        return arg_name, arg_value

    @classmethod
    def parse_function(cls, e: PqlParser.FunctionContext) -> ast.Function:
        return ast.Function(
            full_text(e.function_name),
            tuple([
                cls.parse_function_argument_pair(expr)
                for expr in e.arguments.expr()
            ]) if e.arguments else None
        )

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
            cls.parse_expr(e.value),
            cls.parse_column_typecast(e.type_cast),
            cls.parse_column_alias(e.alias)
        )

    @classmethod
    def parse_literal(cls, e:PqlParser.LiteralValueContext):
        return ast.Literal(
            cls.parse_literal_value(e),
            full_text(e)
        )

    @staticmethod
    def parse_literal_value(e:PqlParser.LiteralValueContext):
        is_number = bool(e.NUMERIC_LITERAL())
        is_string = bool(e.DOUBLE_QUOTED_STRING()) or bool(e.SINGLE_QUOTED_STRING())
        is_null = bool(e.K_NULL())
        is_bool = bool(e.K_TRUE()) or bool(e.K_FALSE())

        # TODO:
        # - BLOB_LITERAL
        # - CURRENT_[DATE|TIME|TIMESTAMP]

        if is_null:
            return None

        if is_bool:
            return bool(e.K_TRUE())

        try:
            v = full_text(e)
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

    @classmethod
    def parse_from_clause_expr(cls, ctx: PqlParser.FromClauseContext) -> Tuple[ast.Table, ...]:
        return tuple([
            ast.Table(
                full_text(table.table_name),
                full_text(table.table_alias)
            )
            for table in ctx.tables()
        ])

    @classmethod
    def parse_expr(cls, ctx: PqlParser.ExprContext) -> ast.Node :
        ctx = cls.unwrap_expr_parens(ctx)

        v = ctx.literalValue()
        if v:
            return cls.parse_literal(v)

        v = ctx.unary_operator
        if v:
            operator = full_text(v).upper()
            return ast.Expr(
                operator,
                (cls.parse_expr(ctx.right),)
            )

        v: Optional[str] = full_text(ctx.operator)
        if v:
            # this is super generic expression of type
            #  left OP right
            # with a lot of options for OP value.
            return ast.Expr(
                v.upper(),
                (
                    cls.parse_expr(ctx.left),
                    cls.parse_expr(ctx.right)
                )
            )

        v: PqlParser.TaxonContext = ctx.taxon()
        if v:
            return cls.parse_taxon(v)

        v: PqlParser.FunctionContext = ctx.function()
        if v:
            return cls.parse_function(v)

        raise Exception(f'Where expression "{full_text(ctx)}" is not supported yet.')


class PqlVisitor(_PqlParserVisitor):

    def visit_from_pql_string(self, pql: str):
        inp_stream = InputStream(pql)
        lexer = PqlLexer(inp_stream)
        stream = CommonTokenStream(lexer)
        parser = PqlParser(stream)
        tree = parser.parsePql()
        self.visit(tree)

    def visit_from_tel_string(self, tel: str):
        inp_stream = InputStream(tel)
        lexer = PqlLexer(inp_stream)
        stream = CommonTokenStream(lexer)
        parser = PqlParser(stream)
        tree = parser.parseTel()
        self.visit(tree)


def from_pql(pql: str, cls:Type[PqlVisitor] = PqlVisitor) -> List[ast.Node]:

    statements = []

    class V(cls):

        def visitSelectStmt(self, ctx:PqlParser.SelectStmtContext):
            columns = tuple([
                ast.Column(
                    PqlAntlrToAstParser.parse_expr(column.value),
                    PqlAntlrToAstParser.parse_column_typecast(column.type_cast),
                    PqlAntlrToAstParser.parse_column_alias(column.alias)
                )
                for column in ctx.selectClause().columns()
            ])

            v = ctx.fromClause()
            if v:
                from_clause = PqlAntlrToAstParser.parse_from_clause_expr(v)
            else:
                from_clause = None

            v = ctx.whereClause()
            if v:
                where_clause = PqlAntlrToAstParser.parse_expr(v.expr())
            else:
                where_clause = None

            statements.append(ast.SelectStmt(
                columns=columns,
                from_clause=from_clause,
                where_clause=where_clause
            ))

        def visitSetStmt(self, ctx:PqlParser.SetStmtContext):
            key = full_text(ctx.key)
            # TODO: parse this better. There are literals there possibly. Need to unpack them.
            value = full_text(ctx.value)
            statements.append(
                ast.SetStmt(
                    key,
                    value
                )
            )

    V().visit_from_pql_string(pql)

    return statements


def from_tel(tel: str, cls:Type[PqlVisitor] = PqlVisitor) -> ast.Node:

    statements = []

    class V(cls):
        def visitExpr(self, ctx:PqlParser.ExprContext):
            statements.append(
                PqlAntlrToAstParser.parse_expr(ctx)
            )

    V().visit_from_tel_string(tel)

    return statements[0] if statements else None

# fmt: off

from antlr4 import (
    CommonTokenStream,
    InputStream,
    ParserRuleContext,
    RecognitionException,
    Recognizer,
    Token,
)
from antlr4.error.ErrorListener import ErrorListener
from decimal import Decimal
from typing import Optional

from .antlr.PqlParser import PqlParser
from .antlr.PqlParserVisitor import PqlParserVisitor as _PqlParserVisitor

from . import model as ast


class ParseError(ValueError):
    pass


class TelErrorListener(ErrorListener):
    # TODO: Contemplate DiagnosticErrorListener as base class for richer error reporting

    def syntaxError(
        self,
        recognizer: Recognizer,
        offending_symbol: Token,
        line: int,
        column: int,
        msg: str,
        e: RecognitionException
    ):
        # See chapter 9.2 "Altering and Redirecting ANTLR Error Messages"
        # http://books.killf.info/%E7%BC%96%E8%AF%91%E5%8E%9F%E7%90%86/The%20Definitive%20ANTLR4%20Reference.pdf

        tokens = recognizer.getInputStream()
        input = full_text(tokens.tokenSource.inputStream)
        # when input == '' splitlines makes it [] - empty. Need at last one line.
        lines = input.splitlines() or ['']
        error_line = lines[line - 1]
        start = offending_symbol.start
        stop = offending_symbol.stop

        base_msg = f'Unexpected "{full_text(offending_symbol)}"' if offending_symbol else msg
        base_msg = base_msg.replace('<EOF>', '<End Of Input>')

        if len(lines) > 1:
            line_msg = f'line {line}, '
        else:
            line_msg = ''

        # "unexpected end of line" errors have index reversed
        # stop is smaller than start.
        if start < stop:
            pos_msg = f'positions {start+1} to {stop+1}'
        else:
            pos_msg = f'position {start+1}'


        if len(error_line) <= start + 1:
            error_line_focus = error_line
        else:
            error_line_focus = (
                error_line[:start] +
                '-->' +
                error_line[start:stop+1] +
                '<--' +
                error_line[stop+1:]
            )
        msg = f'{base_msg} ({line_msg}{pos_msg}) in fragment "{error_line_focus}"'
        raise ParseError(msg)


def full_text(ctx: ParserRuleContext) -> str:
    # extracts full text from a tree of nodes,
    # including white space.
    if ctx:
        if isinstance(ctx, ParserRuleContext):
            try:
                start = ctx.start.start
            except AttributeError:
                start = None
            try:
                stop = ctx.stop.stop
            except AttributeError:
                stop = None

            if not(start is None) and stop is None:
                stop = start

            if start is None:
                return str(ctx)

            return ctx.start.getInputStream().getText(start, stop)
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


class TelVisitor(_PqlParserVisitor):

    def visitParseTel(self, ctx:PqlParser.ParseTelContext):
        return self.visitExpr(ctx.expr())

    def _parse_literal(self, ctx: PqlParser.LiteralValueContext):
        is_number = bool(ctx.NUMERIC_LITERAL())
        is_string = bool(ctx.DOUBLE_QUOTED_STRING()) or bool(ctx.SINGLE_QUOTED_STRING())
        is_null = bool(ctx.K_NULL())
        is_bool = bool(ctx.K_TRUE()) or bool(ctx.K_FALSE())

        if is_null:
            return None

        if is_bool:
            return bool(ctx.K_TRUE())

        try:
            v = full_text(ctx)
        except IndexError:
            raise ParseError(f"Could not extract literal value node from '{ctx.getText()}'.")

        if is_number:
            # TODO: contemplate decimal type instead
            try:
                return int(v)
            except ValueError:
                try:
                    return float(v)
                except Exception:
                    raise ParseError(f"Could not convert SQL number {v} to native number representation.")

        if is_string:
            return unquote(v)

        return v

    def visitLiteralValue(self, ctx:PqlParser.LiteralValueContext):
        return ast.Literal(
            self._parse_literal(ctx),
            full_text(ctx)
        )

    def visitTaxon(self, ctx:PqlParser.TaxonContext):
        return ast.Taxon(
            full_text(ctx.slug),
            full_text(ctx.namespace),
            bool(ctx.is_optional),
            full_text(ctx.tag)
        )

    def visitFn(self, ctx:PqlParser.FnContext):
        return ast.Function(
            full_text(ctx.function_name),
            tuple([
                # argument_name may be undefined, returning Null for name.
                # that's fine.
                # Null for name value means it's not named, but positional argument.
                # positional args are stored as (None, arg_value) tuples.
                (full_text(fn_arg.argument_name), self.visitExpr(fn_arg.argument_value))
                for fn_arg in ctx.arguments.fnArg()
            ]) if ctx.arguments else None
        )

    def visitExpr(self, ctx:PqlParser.ExprContext):
        # unpack parens
        if ctx.inner:
            return self.visitExpr(ctx.inner)

        v = ctx.literalValue()
        if v:
            return self.visitLiteralValue(v)

        v = ctx.unary_operator
        if v:
            operator = full_text(v).upper()

            # expr
            right = self.visitExpr(ctx.right)

            # some unary operators have no meaning
            # and packing them into AST just creates noise for consuming
            if operator == '+':
                # skip the BS. ignore the plus
                # We can do this because we don't support `++a` expressions
                return right

            if (
                operator == '-' and
                isinstance(right, ast.Literal) and
                isinstance(right.value, (int, float, Decimal))
            ):
                # right.value will always be positive digit.
                # Our syntax parser guarantees that.
                return ast.Literal(
                    right.value * -1,
                    full_text(ctx)  # unary minus with underlying literal value as one string
                )

            if (
                operator == 'NOT' and
                isinstance(right, ast.Literal)
            ):
                # unlikely to ever happen, but still
                _v = not right.value
                return ast.Literal(
                    _v,
                    'true' if _v else 'false'
                )

            # else:
            #     # cannot avoid packaging unary "-" separate.
            #     # it's in front of a non-literal expression that need to be negated manually later
            # TODO: contemplate converting this from unary `-expr` into regular `-1 * expr`
            #       to escape Unary minus completely.

            # We dealt with '+'. We half-dealt with '-'
            # What's left is 'NOT'
            # These leftovers we pass through as unary.
            return ast.Expr(
                operator,
                (right,)
            )

        v: Optional[str] = full_text(ctx.operator)
        if v:
            # this is super generic expression of type
            #  left OP right
            # with a lot of options for OP values.
            # The only exception is IN operator where there no `right` but `right_list`

            # we standardize operator keywords to upper case
            # this is to establish a standard expectation for consuming code
            # 'and' -> 'AND'
            op = v.upper()

            # Let's handle IN-like cases first and fall through left-OP-right for rest.
            # IN-like cases are characterized by non-null `.right_list` (instead of .right)
            if ctx.right_list:
                right = [
                    self.visitExpr(expr)
                    for expr in ctx.right_list.expr()
                ]
            else:
                right = [self.visitExpr(ctx.right)]

            is_negated = ctx.is_negated

            # Normally AST parsers should not be in business of
            # rewriting the subject matter.
            # However, there is one ugly nuance of SQL-like language
            # that does not warrant "rewrite" but a "more standard way to express"
            #    a BETWEEN b AND c
            #    a NOT BETWEEN b AND c
            # It's an ugly wart of SQL that requires very special-cased handling
            # in all consumer code if it stays as BETWEEN.
            # TO save the children, and humanity, will express BETWEEN as explicit inequality
            #    a BETWEEN b AND c   -->   (a >= b) AND (a <= c)
            #    a NOT BETWEEN b AND c  -->   (a < b) OR (a > c)
            # Dont think of it as "transform".
            # Think of it as the only sane way to express what BETWEEN means.

            if op == 'BETWEEN':
                left = self.visitExpr(ctx.left)

                # this one is an Expr('AND', [v1, v2]))
                between_and = self.visitExpr(ctx.right)

                if (
                    isinstance(between_and, ast.Expr) and
                    between_and.operator == 'AND' and
                    len(between_and.args) == 2
                ):
                    pass
                else:
                    raise ParseError(
                        f"Contents of BETWEEN's AND expression - {full_text(ctx.right)} - are not valid. "
                        "Must be of form `valueA AND valueB`."
                    )

                if is_negated:
                    #    a NOT BETWEEN b AND c  -->   (a < b) OR (a > c)
                    ex = ast.Expr(
                        'OR',
                        (
                            ast.Expr(
                                '<',
                                (
                                    left,  # TODO: think about copy
                                    between_and.args[0]
                                )
                            ),
                            ast.Expr(
                                '>',
                                (
                                    left,  # TODO: think about copy
                                    between_and.args[1]
                                )
                            ),
                        )
                    )
                else:
                    # a BETWEEN b AND c   -->   (a >= b) AND (a <= c)
                    ex = ast.Expr(
                        'AND',
                        (
                            ast.Expr(
                                '>=',
                                (
                                    left,  # TODO: think about copy
                                    between_and.args[0]
                                )
                            ),
                            ast.Expr(
                                '<=',
                                (
                                    left,  # TODO: think about copy
                                    between_and.args[1]
                                )
                            ),
                        )
                    )
                # we internalized NOT into the expression.
                # can return without further NOT processing
                return ex

            ex = ast.Expr(
                op,
                tuple([self.visitExpr(ctx.left)] + right)
            )

            # lastly, some statements allow NOT before operator
            # (if it's before expression, it's captured by Unary operator)
            # In this case as opposed to creating of a separate NOT-variant operator
            # we just wrap the non-NOT version of the statement into
            # a unary NOT
            #   c not in (1,2,3)
            # becomes
            #   not (c in (1,2,3))

            if ctx.is_negated:
                return ast.Expr(
                    'NOT',
                    (ex,)
                )
            else:
                return ex

        v: PqlParser.TaxonContext = ctx.taxon()
        if v:
            return self.visitTaxon(v)

        v: PqlParser.FnContext = ctx.fn()
        if v:
            return self.visitFn(v)

import sys
from unittest import TestCase

sys.path.append('./src')

from pql_grammar.ast import model as ast
from pql_grammar.ast.to_pql import to_pql
from pql_grammar.ast.from_pql import PqlAntlrToAstParser, PqlVisitor, PqlParser


class ErrorAssertingPqlVisitor(PqlVisitor):
    """
    Special TelVisitor for testing grammar. Throws error in case of invalid node.
    """
    def visitErrorNode(self, node):
        wrong_symbol = node.symbol.text
        position = node.symbol.column + 1
        details = f'Unexpected symbol "{wrong_symbol}" at position {position}'
        raise AssertionError(details)


pql = """\
select
    ?ns1|taxon1,
    ns2|taxon2,
    slug1 as myns|slug1,
    ?ns3|taxon3 + (slug2 - 1234) as myns|custom_data,
    (ns3|taxon3 + 5)::TypeCast() as myns|custom_data_cast,
    fn_4(fn_1(slug))::TypeCast(arg1=value1)
where
    ns6|taxon6 > 1234
    and (ns0|taxon10 + 4321) == 0
"""

# renderer is recursive and ads parens for safety
# TODO: contemplate ways to avoid adding superfluous parens
# and upper-cases all keywords
pql_rendered_should_be = """\
SELECT
    ?ns1|taxon1,
    ns2|taxon2,
    slug1 AS myns|slug1,
    ?ns3|taxon3 + (slug2 - 1234) AS myns|custom_data,
    (ns3|taxon3 + 5)::TypeCast() AS myns|custom_data_cast,
    (fn_4(fn_1(slug)))::TypeCast(arg1=value1)
WHERE
    ((ns6|taxon6 > 1234) AND ((ns0|taxon10 + 4321) == 0))
;
"""

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
            ast.TelExpr('ns3|taxon3 + 5'),
            ast.Function(
                'TypeCast'
            ),
            ast.Taxon('custom_data_cast', 'myns')
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


class PqlAstTests(TestCase):
    maxDiff = None

    def test_select(self):

        statements = []

        class V(ErrorAssertingPqlVisitor):
            def visitSelectStmt(self, ctx:PqlParser.SelectStmtContext):
                columns = [
                    ast.Column(
                        PqlAntlrToAstParser.parse_column_value(column.value),
                        PqlAntlrToAstParser.parse_column_typecast(column.type_cast),
                        PqlAntlrToAstParser.parse_column_alias(column.alias)
                    )
                    for column in ctx.selectClause().columns()
                ]
                where_clause = PqlAntlrToAstParser.parse_where_clause_expr(ctx.whereClause().expr())

                statements.append(ast.SelectStmt(
                    columns,
                    where_clause
                ))

        V().visit_from_string(pql)

        assert statements
        stmt = statements[0]

        assert len(stmt.columns) == len(stmt_should_be.columns)
        for result, should_be in zip(stmt.columns, stmt_should_be.columns):
            assert result == should_be

        # ast.ast_diff(stmt.where_clause, stmt_should_be.where_clause)
        assert stmt.where_clause == stmt_should_be.where_clause

    def test_render_pql_from_ast(self):
        pql_result = to_pql(stmt_should_be)
        assert pql_rendered_should_be == pql_result

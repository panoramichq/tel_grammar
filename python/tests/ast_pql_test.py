import sys
from unittest import TestCase

sys.path.append('./src')

from pql_grammar.ast import model as ast
from pql_grammar.ast.to_pql import to_pql
from pql_grammar.ast.from_pql import PqlVisitor, PqlParser, from_pql
from pql_grammar.ast.tools import find_all


class ErrorAssertingPqlVisitor(PqlVisitor):
    """
    Special TelVisitor for testing grammar. Throws error in case of invalid node.
    """
    def visitErrorNode(self, node):
        wrong_symbol = node.symbol.text
        position = node.symbol.column + 1
        details = f'Unexpected symbol "{wrong_symbol}" at position {position}'
        raise AssertionError(details)


pql_all_cases = """\
select
    ?ns1|taxon1,
    ns2|taxon2,
    slug1 as myns|slug1,
    ?ns3|taxon3 + (slug2 - 1234) as myns|custom_data,
    (ns3|taxon3 + 5)::TypeCast() as myns|custom_data_cast,
    fn_4(fn_1(slug))::TypeCast(arg1='value1')
from my_ns, your_ns as super_ns
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
    (?ns3|taxon3 + (slug2 - 1234)) AS myns|custom_data,
    (ns3|taxon3 + 5)::TypeCast() AS myns|custom_data_cast,
    (fn_4(fn_1(slug)))::TypeCast(arg1='value1')
FROM
    my_ns,
    your_ns AS super_ns
WHERE
    ((ns6|taxon6 > 1234) AND ((ns0|taxon10 + 4321) == 0))
;
"""

stmt_should_be = ast.SelectStmt(
    columns = (
        ast.Column(ast.Taxon('taxon1', 'ns1', True)),
        ast.Column(ast.Taxon('taxon2', 'ns2', False)),
        ast.Column(ast.Taxon('slug1'), None, ast.Taxon('slug1', 'myns')),
        ast.Column(
            ast.Expr(
                '+',
                (
                    ast.Taxon(
                        'taxon3',
                        'ns3',
                        True
                    ),
                    ast.Expr(
                        '-',
                        (
                            ast.Taxon('slug2'),
                            ast.Literal(1234, '1234'),
                        ),
                    ),
                ),
            ),
            None,
            ast.Taxon('custom_data', 'myns'),
        ),
        ast.Column(
            ast.Expr(
                '+',
                (
                    ast.Taxon(
                        'taxon3',
                        'ns3',
                    ),
                    ast.Literal(5, '5'),
                ),
            ),
            ast.Function(
                'TypeCast'
            ),
            ast.Taxon('custom_data_cast', 'myns')
        ),
        ast.Column(
            ast.Function('fn_4', (
                (None, ast.Function('fn_1', (
                    (None, ast.Taxon('slug')),
                ),),),
            ),),
            ast.Function(
                'TypeCast',
                (
                    ('arg1',ast.Literal('value1', "'value1'")),
                ),
            ),
        ),
    ),
    from_clause = (
        ast.Table('my_ns'),
        ast.Table('your_ns', 'super_ns')
    ),
    where_clause = ast.Expr(
        'AND',
        (
            ast.Expr(
                '>',
                (
                    ast.Taxon('taxon6', 'ns6'),
                    ast.Literal(1234, '1234'),
                ),
            ),
            ast.Expr(
                '==',
                (
                    ast.Expr(
                        '+',
                        (
                            ast.Taxon('taxon10', 'ns0'),
                            ast.Literal(4321, '4321'),
                        ),
                    ),
                    ast.Literal(0, '0'),
                ),
            ),
        ),
    ),
)


class PqlAstTests(TestCase):
    maxDiff = None

    def test_multiple_statements(self):
        pql = """
            set fill_empty_dates = true;
            select a, b;
        """
        statements = from_pql(pql, ErrorAssertingPqlVisitor)

        assert len(statements) == 2
        set_stmt = statements[0]
        select_stmt = statements[1]

        # TODO: make SET parse literal values properly into python native bool, int, str etc.
        # Till then, this is mostly a placeholder for future functionality
        assert set_stmt == ast.SetStmt('fill_empty_dates', 'true')
        assert select_stmt == ast.SelectStmt(
            columns=(
                ast.Column(ast.Taxon('a')),
                ast.Column(ast.Taxon('b')),
            )
        )

    def test_select(self):
        statements = from_pql(pql_all_cases, ErrorAssertingPqlVisitor)
        assert statements
        stmt = statements[0]

        assert len(stmt.columns) == len(stmt_should_be.columns)
        for result, should_be in zip(stmt.columns, stmt_should_be.columns):
            assert result == should_be
        # ast.ast_diff(stmt.where_clause, stmt_should_be.where_clause)
        assert stmt.where_clause == stmt_should_be.where_clause

        # ensure produced nodes are hashable
        set(
            find_all(
                stmt,
                lambda o: isinstance(o, ast.Node)
            )
        )

    def test_parse_from_statement(self):
        pql_input = """\
            SELECT
                a,
                b
            from
                dataset_one,
                dataset_two as two
            WHERE
                a > b
            ;
        """
        statements = from_pql(pql_input, ErrorAssertingPqlVisitor)
        assert len(statements) == 1
        select_stmt: ast.SelectStmt = statements[0]
        assert select_stmt.from_clause == (
            ast.Table('dataset_one'),
            ast.Table('dataset_two', 'two'),
        )

        # ensure produced nodes are hashable
        set(
            find_all(
                statements,
                lambda o: isinstance(o, ast.Node)
            )
        )

    def test_render_pql_from_ast(self):
        pql_result = to_pql([stmt_should_be])
        assert pql_result == pql_rendered_should_be

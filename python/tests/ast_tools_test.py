# fmt: off

import sys
from unittest import TestCase

sys.path.append('./src')

from pql_grammar.ast import model as ast
from pql_grammar.ast.tools import find_all


sample_tree = ast.SelectStmt(
    columns = (
        ast.Column(ast.Taxon('taxon1', 'ns1', True)),
        ast.Column(ast.Taxon('taxon2', 'ns2', False)),
        ast.Column(ast.Literal(5555, '5555')),
        ast.Column(ast.Taxon('slug1'), None, ast.Taxon('slug1', 'myns')),
        ast.Column(
            ast.Expr(
                '+',
                (
                    ast.Taxon(
                        'taxon3',
                        'ns3',
                        True,
                    ),
                    ast.Expr(
                        '-',
                        (
                            ast.Taxon('slug'),
                            ast.Literal(12345, '12345'),
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
                'TypeCast',
            ),
            ast.Taxon('custom_data_cast', 'myns'),
        ),
        ast.Column(
            ast.Function('fn_4', (
                (None, ast.Function('fn_1', (
                    (None, ast.Taxon('slug'),),
                ),),),
            ),),
            ast.Function(
                'TypeCast',
                (('arg1','value1'),),  # normally inner pair is a tuple, but for comparison making list.
            ),
        ),
    ),
    from_clause = (
        ast.Table('my_ns'),
        ast.Table('your_ns', 'super_ns'),
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


class AstToolsTests(TestCase):
    maxDiff = None

    def test_find_all(self):
        vv = list(find_all(
            sample_tree,
            lambda o: isinstance(o, ast.Literal)
        ))

        assert vv == [
            ast.Literal(value=5555, raw_value='5555'),
            ast.Literal(value=12345, raw_value='12345'),
            ast.Literal(value=5, raw_value='5'),
            ast.Literal(value=1234, raw_value='1234'),
            ast.Literal(value=4321, raw_value='4321'),
            ast.Literal(value=0, raw_value='0'),
        ]

    def test_nodes_hashable(self):

        a = {
            ast.Taxon('slug1'),
            ast.Taxon('slug2'),
        }

        b = {
            ast.Taxon('slug2'),
            ast.Taxon('slug1'),
        }

        assert a == b

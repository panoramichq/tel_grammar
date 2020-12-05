# fmt: off

import sys
from unittest import TestCase

sys.path.append('./src')

from pql_grammar import model as ast
from pql_grammar.tools import find_all


class AstToolsTests(TestCase):
    maxDiff = None

    def test_find_all(self):
        vv = list(find_all(
            ast.Expr(
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
            lambda o: isinstance(o, ast.Literal)
        ))

        assert vv == [
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

# fmt: off

import pytest
import sys

sys.path.append('./src')

from pql_grammar import model as ast
from pql_grammar.to_pql import to_tel
from pql_grammar.from_pql import PqlVisitor, from_tel
from pql_grammar.tools import find_all


inputs = (
    '?ns1|taxon1',
    'ns2|taxon2',
    'slug1',
    '?ns3|taxon3 + (slug2 - 1234)',
    '(ns3|taxon3 + 5)',
    'fn_4(fn_1(slug))',
    'TypeCast(arg1=\'value1\')',
    'ns6|taxon6 > 1234 and (ns0|taxon10 + 4321) == 0'
)


ast_should_bes = (
    ast.Taxon('taxon1', 'ns1', True),
    ast.Taxon('taxon2', 'ns2', False),
    ast.Taxon('slug1'),
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
)


outputs = (
    '?ns1|taxon1',
    'ns2|taxon2',
    'slug1',
    '(?ns3|taxon3 + (slug2 - 1234))',
    '(ns3|taxon3 + 5)',
    'fn_4(fn_1(slug))',
    'TypeCast(arg1=\'value1\')',
    '((ns6|taxon6 > 1234) AND ((ns0|taxon10 + 4321) == 0))'
)


@pytest.mark.parametrize(
    'input, ast_should_be, output_should_be',
    zip(inputs, ast_should_bes, outputs)
)
def test_tel_to_ast_and_back(input: str, ast_should_be: ast.Node, output_should_be: str):
    ast_is = from_tel(input)
    assert ast_is == ast_should_be

    output_is = to_tel(ast_is)
    assert output_is == output_should_be

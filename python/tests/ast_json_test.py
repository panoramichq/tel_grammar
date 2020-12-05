# fmt: off

import pytest
import sys

sys.path.append('./src')

from pql_grammar import model as ast
from pql_grammar.tools import ast_diff
from pql_grammar.to_json import to_json
from pql_grammar.from_json import from_json


null = None
false = False
true = True


inputs = (
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
                    ast.Taxon('slug'),
                    ast.Literal(1234, '1234')
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
    {
        "__typename": "Taxon",
        "slug": "taxon1",
        "namespace": "ns1",
        "is_optional": true
    },
    {
        "__typename": "Taxon",
        "slug": "taxon2",
        "namespace": "ns2",
        "is_optional": false
    },
    {
        "__typename": "Taxon",
        "slug": "slug1",
        "is_optional": false
    },
    {
        "__typename": "Expr",
        "operator": "+",
        "args": [
            {
                "__typename": "Taxon",
                "slug": "taxon3",
                "namespace": "ns3",
                "is_optional": true
            },
            {
                "__typename": "Expr",
                "operator": "-",
                "args": [
                    {
                        "__typename": "Taxon",
                        "slug": "slug",
                        "is_optional": false
                    },
                    {
                        "__typename": "Literal",
                        "value": 1234,
                        "raw_value": "1234"
                    }
                ]
            }
        ]
    },
    {
        "__typename": "Expr",
        "operator": "+",
        "args": [
            {
                "__typename": "Taxon",
                "slug": "taxon3",
                "namespace": "ns3",
                "is_optional": false
            },
            {
                "__typename": "Literal",
                "value": 5,
                "raw_value": "5"
            }
        ]
    },
    {
        "__typename": "Function",
        "function_name": "fn_4",
        "args": [
            [
                null,
                {
                    "__typename": "Function",
                    "function_name": "fn_1",
                    "args": [
                        [
                            null,
                            {
                                "__typename": "Taxon",
                                "slug": "slug",
                                "is_optional": false
                            }
                        ]
                    ]
                }
            ]
        ]
    },
    {
        "__typename": "Expr",
        "operator": "AND",
        "args": [
            {
                "__typename": "Expr",
                "operator": ">",
                "args": [
                    {
                        "__typename": "Taxon",
                        "slug": "taxon6",
                        "namespace": "ns6",
                        "is_optional": false
                    },
                    {
                        "__typename": "Literal",
                        "value": 1234,
                        "raw_value": "1234"
                    }
                ]
            },
            {
                "__typename": "Expr",
                "operator": "==",
                "args": [
                    {
                        "__typename": "Expr",
                        "operator": "+",
                        "args": [
                            {
                                "__typename": "Taxon",
                                "slug": "taxon10",
                                "namespace": "ns0",
                                "is_optional": false
                            },
                            {
                                "__typename": "Literal",
                                "value": 4321,
                                "raw_value": "4321"
                            }
                        ]
                    },
                    {
                        "__typename": "Literal",
                        "value": 0,
                        "raw_value": "0"
                    }
                ]
            }
        ]
    }
)


@pytest.mark.parametrize(
    'input, output_should_be',
    zip(inputs, outputs)
)
def test_tel_to_ast_and_back(input: str, output_should_be: str):
    json_is = to_json(input)
    assert json_is == output_should_be

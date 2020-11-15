import sys
from unittest import TestCase

sys.path.append('./src')

from pql_grammar.ast import model as ast
from pql_grammar.ast.tools import ast_diff
from pql_grammar.ast.to_json import to_json
from pql_grammar.ast.from_json import from_json


null = None
false = False
true = True


ast_should_be = ast.SelectStmt(
    columns = [
        ast.Column(ast.Taxon('taxon1', 'ns1', True)),
        ast.Column(ast.Taxon('taxon2', 'ns2', False)),
        ast.Column(ast.Taxon('slug1'), None, ast.Taxon('slug1', 'myns')),
        ast.Column(
            ast.Expr(
                '+',
                [
                    ast.Taxon(
                        'taxon3',
                        'ns3',
                        True
                    ),
                    ast.Expr(
                        '-',
                        [
                            ast.Taxon('slug'),
                            ast.Literal(1234, '1234')
                        ]
                    )
                ]
            ),
            None,
            ast.Taxon('custom_data', 'myns')
        ),
        ast.Column(
            ast.Expr(
                '+',
                [
                    ast.Taxon(
                        'taxon3',
                        'ns3',
                    ),
                    ast.Literal(5, '5'),
                ]
            ),
            ast.Function(
                'TypeCast'
            ),
            ast.Taxon('custom_data_cast', 'myns')
        ),
        ast.Column(
            ast.Function('fn_4', [
                [None, ast.Function('fn_1', [
                    [None, ast.Taxon('slug')]
                ])]
            ]),
            ast.Function(
                'TypeCast',
                [['arg1','value1']]  # normally inner pair is a tuple, but for comparison making list.
            ),
        )
    ],
    where_clause = ast.Expr(
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


json_should_be = {
    "__typename": "SelectStmt",
    "columns": [
        {
            "__typename": "Column",
            "value": {
                "__typename": "Taxon",
                "slug": "taxon1",
                "namespace": "ns1",
                "is_optional": true
            }
        },
        {
            "__typename": "Column",
            "value": {
                "__typename": "Taxon",
                "slug": "taxon2",
                "namespace": "ns2",
                "is_optional": false
            }
        },
        {
            "__typename": "Column",
            "value": {
                "__typename": "Taxon",
                "slug": "slug1",
                "is_optional": false
            },
            "alias": {
                "__typename": "Taxon",
                "slug": "slug1",
                "namespace": "myns",
                "is_optional": false
            }
        },
        {
            "__typename": "Column",
            "value": {
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
            "alias": {
                "__typename": "Taxon",
                "slug": "custom_data",
                "namespace": "myns",
                "is_optional": false
            }
        },
        {
            "__typename": "Column",
            "value": {
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
            "type_cast": {
                "__typename": "Function",
                "function_name": "TypeCast"
            },
            "alias": {
                "__typename": "Taxon",
                "slug": "custom_data_cast",
                "namespace": "myns",
                "is_optional": false
            }
        },
        {
            "__typename": "Column",
            "value": {
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
            "type_cast": {
                "__typename": "Function",
                "function_name": "TypeCast",
                "args": [
                    [
                        "arg1",
                        "value1"
                    ]
                ]
            }
        }
    ],
    "where_clause": {
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
}


class JsonAstTests(TestCase):
    maxDiff = None

    def test_render_json_from_ast(self):
        json_result = to_json(ast_should_be)
        # import json; print(json.dumps(json_result, indent=4))
        assert json_should_be == json_result

    def test_render_ast_from_json(self):
        ast_result = from_json(json_should_be)
        # import json; print(json.dumps(json_result, indent=4))
        ast_diff(ast_should_be, ast_result)
        assert ast_should_be == ast_result

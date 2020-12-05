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
    'ns6|taxon6 > 1234 and (ns0|taxon10 + 4321) == 0',
    'slug like \'blah%\'',
    'slug not like \'blah%\'',
    'slug in (1,2)',
    'slug not in (1,2)',
    # Special non-literal extractions:
    #
    # BETWEEN expressions extremely annoying to deal with in consumer code
    # Between is expressed as union of simple expressions depicting its meaning.
    'a BETWEEN b AND c', ##   -->   (a >= b) AND (a <= c)
    'a NOT BETWEEN b AND c', ##  -->   (a < b) OR (a > c)
    # unary expressions are annoying to deal with in consumer code
    # too many edge cases. This parser extracts meaning statically where possible.
    'NOT a',  ## (NOT (Taxon a))
    '-a',  ## ('-' (Taxon a))
    '+a',  ## (Taxon a)  # skip +
    '-2',  ## (Literal -2)  # negate number if expr is number
    'NOT 3',  ## becomes boolean false
    'NOT 0',  ## becomes boolean true
    'NOT "text"',  ## becomes boolean false
    'NOT ""',  ## becomes boolean true
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
    ast.Expr(
        'LIKE',
        (
            ast.Taxon(
                'slug',
            ),
            ast.Literal('blah%', "'blah%'"),
        ),
    ),
    ast.Expr(
        'NOT',
        (
            ast.Expr(
                'LIKE',
                (
                    ast.Taxon(
                        'slug',
                    ),
                    ast.Literal('blah%', "'blah%'"),
                ),
            ),
        )
    ),
    ast.Expr(
        'IN',
        (
            ast.Taxon(
                'slug',
            ),
            ast.Literal(1, "1"),
            ast.Literal(2, "2"),
        ),
    ),
    ast.Expr(
        'NOT',
        (
            ast.Expr(
                'IN',
                (
                    ast.Taxon(
                        'slug',
                    ),
                    ast.Literal(1, "1"),
                    ast.Literal(2, "2"),
                ),
            ),
        )
    ),
    # 'a BETWEEN b AND c', ##   -->   (a >= b) AND (a <= c)
    ast.Expr(
        'AND',
        (
            ast.Expr(
                '>=',
                (
                    ast.Taxon('a'),
                    ast.Taxon('b'),
                ),
            ),
            ast.Expr(
                '<=',
                (
                    ast.Taxon('a'),
                    ast.Taxon('c'),
                ),
            ),
        ),
    ),
    # 'a NOT BETWEEN b AND c', ##  -->   (a < b) OR (a > c)
    ast.Expr(
        'OR',
        (
            ast.Expr(
                '<',
                (
                    ast.Taxon('a'),
                    ast.Taxon('b'),
                ),
            ),
            ast.Expr(
                '>',
                (
                    ast.Taxon('a'),
                    ast.Taxon('c'),
                ),
            ),
        ),
    ),
    ast.Expr('NOT', (ast.Taxon('a'),)),  # 'not a'
    ast.Expr('-', (ast.Taxon('a'),)),  # '-a'
    ast.Taxon('a'),  ## '+a' skips +
    ast.Literal(-2, '-2'),  ## '-2'
    ast.Literal(False, 'false'),  # NOT 3
    ast.Literal(True, 'true'),  # NOT 0
    ast.Literal(False, 'false'),  # NOT 'text'
    ast.Literal(True, 'true'),  # NOT ''
)


outputs = (
    '?ns1|taxon1',
    'ns2|taxon2',
    'slug1',
    '(?ns3|taxon3 + (slug2 - 1234))',
    '(ns3|taxon3 + 5)',
    'fn_4(fn_1(slug))',
    'TypeCast(arg1=\'value1\')',
    '((ns6|taxon6 > 1234) AND ((ns0|taxon10 + 4321) == 0))',
    '(slug LIKE \'blah%\')',
    'NOT (slug LIKE \'blah%\')',
    '(slug IN (1, 2))',
    'NOT (slug IN (1, 2))',
    '((a >= b) AND (a <= c))',  # was: a BETWEEN b AND c
    '((a < b) OR (a > c))',  # was: a NOT BETWEEN b AND c
    'NOT a',  # ast.Expr('NOT', (ast.Taxon('a'),)),  # 'not a'
    '-a',  # ast.Expr('-', (ast.Taxon('a'),)),  # '-a'
    'a',  # ast.Taxon('a'),  ## '+a' skips +
    '-2',  # ast.Literal(-2, '-2'),  ## '-2'
    'false',  # NOT 3
    'true',  # NOT 0
    'false',  # NOT 'text'
    'true',  # NOT ''
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



@pytest.mark.parametrize(
    'ast_input, str_output_should_be',
    (
        (
            ast.Expr(
                'AND',
                (
                    ast.Taxon(
                        'slug',
                    ),
                    ast.Expr(
                        'OR',
                        (
                            ast.Literal(1, "1"),
                            ast.Literal(2, "2"),
                        ),
                    ),
                    ast.Literal(3, "3"),
                ),
            ),
            '(slug AND (1 OR 2) AND 3)',
        ),
        (
            ast.Expr(
                'BETWEEN',
                (
                    ast.Taxon(
                        'slug',
                    ),
                    ast.Expr(
                        'AND',
                        (
                            ast.Literal(2, "2"),
                            ast.Literal(3, "3"),
                        ),
                    ),
                )
            ),
            '(slug BETWEEN 2 AND 3)',
        ),
    )
)
def test_ast_to_tel_special_cases(ast_input: ast.Node, str_output_should_be: str):
    output_is = to_tel(ast_input)
    assert output_is == str_output_should_be

import pytest

from antlr4 import CommonTokenStream, InputStream

from tel_grammar.antlr.TelLexer import TelLexer
from tel_grammar.antlr.TelParser import TelParser
from tel_grammar.antlr.TelVisitor import TelVisitor


class AssertTelVisitor(TelVisitor):
    """
    Special TelVisitor for testing grammar. Throws error in case of invalid node.
    """

    def visitErrorNode(self, node):
        wrong_symbol = node.symbol.text
        position = node.symbol.column + 1
        details = f'Unexpected symbol "{wrong_symbol}" at position {position}'
        raise AssertionError(details)


@pytest.mark.parametrize(
    ["test_case"],
    [
        # Basic operations
        ('slug + slug_slug',),
        ('1 + slug',),
        ('1.2 + slugs - 10',),
        ('(1 + slug) - 3',),
        ('34 - (slug * 2)',),
        ('-10 + 20.5 * slug',),
        ('-10 * (slug + (another_slug - 300) * 24.654)',),
        # Functions
        ('fn_1(slug)',),
        ('fn_1(slug)  + 23.23',),
        ('fn_2(slug, 123, 10.2)',),
        # this test case is meant to test parser's ability to handle optional params
        ('fn_3(slug)',),
        # this test case is meant to test parser's ability to handle optional params
        ('fn_3(slug, optional_param)',),
        # Special cases
        # Handle ambiguity
        ('slug(test_slug, 13)',),
        # Handle namespaced taxons
        ('ds|slug + 10 - sluging',),
        # Handle nested functions
        ('fn_4(fn_1(slug))',),
        ('"str1" + "str2"',),
        ('"str1\\"escape"',),
        # Handle optional taxons
        ('?ds|slug + 10 - ?sluging + sluggingX',),
        ('fb|a:x + fb|a + a:x + ?fb|a:x + ?fb|a + ?a:x',),
        # handle single quotes
        ("'my test'",),
        ("'my \\' new test'",),
        # Handle taxon slugs and functions with dot
        ('db.prod',),
        ('db.prod|schema.table.column',),
        ('db.prod|schema.table.column:v2.0',),
        ('fn.contains()',),
        ('fn.contains.v2(db.prod, 3.14)',),
    ],
)
def test_grammar(test_case):
    inp_stream = InputStream(test_case)
    lexer = TelLexer(inp_stream)
    stream = CommonTokenStream(lexer)
    parser = TelParser(stream)
    tree = parser.parse()
    # Use error visitor on parsed tree to test it
    visitor = AssertTelVisitor()
    visitor.visit(tree)

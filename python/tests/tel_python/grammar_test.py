import pytest
from antlr4 import CommonTokenStream, InputStream

from tel_python.TelLexer import TelLexer
from tel_python.TelParser import TelParser

@pytest.mark.parametrize(["test_case"], [
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
])
def test_grammar(test_case):
    inp_stream = InputStream(test_case)
    lexer = TelLexer(inp_stream)
    stream = CommonTokenStream(lexer)
    parser = TelParser(stream)
    assert parser.expr()

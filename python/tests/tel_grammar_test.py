import os
import sys
import pytest

from antlr4 import CommonTokenStream, InputStream, ParserRuleContext

sys.path.append('./src')

from pql_grammar.from_pql import from_tel, ParseError


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
        ('db.prod|schema.table.column:v2.b0',),
        ('fn.contains()',),
        ('fn.contains.v2(db.prod, 3.14)',),
        # Handle not operator
        ('not (true || false)',),
        ('NOT (TRUE && FALSE)',),
        # Handle null test operators
        ('slug is null',),
        ('slug IS NULL',),
        ('slug is not null',),
        ('slug IS NOT NULL',),
        ('slug is         NULL',),
        ('slug is   NOT   NULL',),
    ],
)
def test_grammar(test_case):
    assert from_tel(test_case)


@pytest.mark.parametrize(
    ["test_case"],
    [
        # Basic operations
        ('1.3.3 + slug',),
        ('1 + slug) - 3',),
        # ('34 - (slug * 2',), passes because does not need closing paren
        ('-------------',),
        # Handle namespaced taxons
        ('ds|sl|ug - sluging',),
        # Handle nested functions
        ('slug is',),
        ('not',),
        ('',),
        ('a BETWEEN e',),
        ('a BETWEEN f OR x',),
    ],
)
def test_grammar_bad(test_case):
    with pytest.raises(ParseError) as ex:
        assert from_tel(test_case)

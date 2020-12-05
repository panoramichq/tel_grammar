# fmt: off

import sys
sys.path.append('./src')

import pytest

from pql_grammar import model as ast


inputs = (
    ast.Taxon('slug'),
    ast.Taxon('slug', 'ns'),
    ast.Taxon('slug', 'ns', is_optional=True),
    ast.Taxon('slug', None, is_optional=True),
    ast.Taxon('slug', 'ns', is_optional=True, tag='Tagggg'),
    ast.Taxon('slug', None, is_optional=True, tag='Tagggg'),
    ast.Taxon('slug', 'ns', tag='Tagggg'),
    ast.Taxon('slug', None, tag='Tagggg'),
)

outputs = (
    'slug',
    'ns|slug',
    '?ns|slug',
    '?slug',
    '?ns|slug:Tagggg',
    '?slug:Tagggg',
    'ns|slug:Tagggg',
    'slug:Tagggg',
)


@pytest.mark.parametrize('input, output', zip(inputs, outputs))
def test_taxon_raw_value(input: ast.Taxon, output: str):
    assert input.raw_value == output

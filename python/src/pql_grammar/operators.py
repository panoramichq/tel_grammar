"""
Conditional logic runners designed for latent evaluation.

First you construct the logic, then pass into resulting callable an object that contains values mentioned in the logic
Designed for expressing a SQL WHERE clause logic before you have data and then running each row's data through it.

  # WHERE columnA = 'gold' AND columnB > 100
  clause = AND(
    EQ(
      attr('columnA'),
      'gold'
    ),
    GT(
      attr('columnB'),
      100
    )
  )

  remaining_data = [
    row
    for row in rows
    if clause(row)
  ]

Works for dict's (keys and values over `.get(` interface) AND object attributes (properties) (`getattr(o, attr)`)

(This is NOT designed to be serialized for pushing over wire. Make something else for that.)

"""
import enum
import logging
import re

from dataclasses import dataclass
from typing import Tuple, List, Any, Optional, Union, Literal


logger = logging.getLogger(__name__)


_v = lambda v, o: v(o) if callable(v) else v


def AND(*children):
    def _(o):
        return all((
            _v(a, o)
            for a in children
        ))
    return _


def OR(*children):
    def _(o):
        return any((
            _v(a, o)
            for a in children
        ))
    return _


def NOT(a):
    def _(o):
        return not _v(a, o)
    return _


def EQ(a, b):
    def _(o):
        return _v(a, o) == _v(b, o)
    return _


def NEQ(a, b):
    def _(o):
        return _v(a, o) != _v(b, o)
    return _


def IS(a, b):
    def _(o):
        return _v(a, o) is _v(b, o)
    return _


# https://codereview.stackexchange.com/a/36864/229677
_char_regex_map = {
    ch : '\\'+ch
    for ch in '.^$*+?{}[]|()\\'
}
_char_regex_map['%'] = '.*?'
_char_regex_map['_'] = '.'
def sql_like_fragment_to_regex_string(fragment):
    return '^' + ''.join([
        _char_regex_map.get(ch, ch)
        for ch in fragment
    ]) + '$'


def LIKE(a, fragment):
    _regex = re.compile(sql_like_fragment_to_regex_string(fragment))
    def _(o):
        return bool(_regex.match(_v(a, o)))
    return _


def GT(a, b):
    def _(o):
        return _v(a, o) > _v(b, o)
    return _


def GTE(a, b):
    def _(o):
        return _v(a, o) >= _v(b, o)
    return _


def LT(a, b):
    def _(o):
        return _v(a, o) < _v(b, o)
    return _


def LTE(a, b):
    def _(o):
        return _v(a, o) <= _v(b, o)
    return _


def PLUS_UNARY(a):
    def _(o):
        # no-op
        return _v(a, o)
    return _


def MINUS_UNARY(a):
    def _(o):
        return -1 * _v(a, o)
    return _


def PLUS(a, b):
    def _(o):
        return _v(a, o) + _v(b, o)
    return _


def MINUS(a, b):
    def _(o):
        return _v(a, o) - _v(b, o)
    return _


def STAR(a, b):
    def _(o):
        return _v(a, o) * _v(b, o)
    return _


def DIV(a, b):
    def _(o):
        return _v(a, o) / _v(b, o)
    return _


def MOD(a, b):
    def _(o):
        return _v(a, o) % _v(b, o)
    return _


class TableColumnName(list):
    def __init__(self, column_name, table_name=None, schema_name=None, catalog_name=None):
        super().__init__([
            e
            for e in [column_name, table_name, schema_name, catalog_name]
            if not (e is None)
        ])


def attr(name: Union[str, list, TableColumnName], default=None):
    """
    This attr getter works only on Class-like objects,
    where you access values through attributes, not keys
    Done so specifically to stay away from ambiguity of working with named tuples.
    Also allows repackaging instances of objects ON_DEMAND where values are hiding in @properties
    and are, thus allowing Where logic to trigger expensive properties only when needed,
    as opposed to forcing serialization of full object into dict before piping through the where clause.

    Best examples of what `o` is - @dataclass or namedtuple instances.
    Obviously, pydantic models and all other class instances will do too.
    """
    def _(o):
        # do NOT add .get( handling here, especially do NOT add it as first action.
        # You will break namedtuples, where .get(index) is present
        # but o.attr_name is the only right way to ask for data by name (not index)
        if isinstance(o, (TableColumnName, list)):
            if len(o) > 1:
                logger.warning(f"WHERE clause references column by long name '{list(reversed(o))}', "
                               "which is not compatible with our functional WHERE logic processor. "
                               f"Droping all parts except for '{o[0]}' during comparison")
            return getattr(o[0], name, default)
        else:
            return getattr(o, name, default)
    return _


class OpName:
    AND = 'AND'
    OR = 'OR'
    NOT = 'NOT'
    EQ = 'EQ'
    NEQ = 'NEQ'
    IS = 'IS'
    LIKE = 'LIKE'
    GT = 'GT'
    GTE = 'GTE'
    LT = 'LT'
    LTE = 'LTE'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    STAR = 'STAR'
    DIV = 'DIV'
    MOD = 'MOD'
    attr = 'attr'


name_operator_map = {
    OpName.AND:AND,
    OpName.OR:OR,
    OpName.NOT:NOT,
    OpName.EQ:EQ,
    OpName.NEQ:NEQ,
    OpName.IS:IS,
    OpName.LIKE:LIKE,
    OpName.GT:GT,
    OpName.GTE:GTE,
    OpName.LT:LT,
    OpName.LTE:LTE,
    OpName.PLUS:PLUS,
    OpName.MINUS:MINUS,
    OpName.STAR:STAR,
    OpName.DIV:DIV,
    OpName.MOD:MOD,
    OpName.attr:attr,
}


operator_name_map = {
    fn: name
    for name, fn in name_operator_map.items()
}


OperatorName = str  # OP_NAME if it was (str, enum.Enum), but that produces ugly output structures
OperatorSchemaLiteral = Tuple[Literal['@literalValue'], Any]
# it's actually a List that's returned, but Python typing system does not? allow
# expressing a list with defined items inside in their order.
# have to use Tuple to specify order of things, but return type is actually list
# This structure is supposed to natively serializable to and from JSON>
OperatorSchema = Union[
    Tuple[OperatorName, 'OperatorSchema', Optional['OperatorSchema']],
    OperatorSchemaLiteral
]


LITERAL = '@literalValue'


def schema_literal(o) -> OperatorSchemaLiteral:
    return [LITERAL, o]


def schema_stanza(operator_name, *args) -> OperatorSchema:
    aa = []
    for a in args:
        # lists usually dont make sense as literals, so checking is just being overly safe
        # however, `WHERE a IN ('a','b','c')` clause produces a tuple-like literal,
        # first element in which MAY be value 'literal'
        # This tuple, if encoded as list object will break this code.

        # We don't support IN yet, but when we do, think about ^ this case and change
        # literal tuple marker value to something that would be
        # (a) serializable to JSON, yet
        # (b) impossible to collide with first element in SQL IN array.

        # TODO: ^ account for WHERE IN literal value collision.
        if isinstance(a, (list, tuple)) and len(a) > 1 and (a[0] == LITERAL or a[0] in name_operator_map):
            # This is already encoded stanza, pass through as is
            aa.append(a)
        else:
            aa.append(schema_literal(a))
    return [operator_name, *aa]


def schema_to_callable(schema: OperatorSchema):
    if not schema:
        return lambda o: True

    fn_name, *args = schema
    if fn_name == LITERAL:
        # only one value possible
        return args[0]
    else:
        fn = name_operator_map[fn_name]
        return fn(*(
            schema_to_callable(arg)
            for arg in args
        ))


class _Any:
    # used for comparing / finding stanzas in where schema when
    # you want to match the structure but not some literal values
    def __eq__(self, other):
        return True
Any = _Any()


def schema_extract_top_level(schema_fragment: OperatorSchema, schema: OperatorSchema):
    # when underlying function call requires a parameter
    # we need to extract it from sql and ensure it's specified in unambigous way
    # ambiguous for arg need_this_id:
    #  where a = 'orange' or (date < now()-3 or need_this_id = '1234')
    # UNambiguous for arg need_this_id:
    #  where a = 'orange' AND need_this_id = '1234'
    # In other words, condition we are looking to extract does not have to be the only one in
    # the clause, but just have to participate in unambiguously top-level AND or just be by itself.
    # This means we'll traverse down recursive ANDs until we find NON-AND and that NON-AND must equal our fragment.

    if schema_fragment == schema:
        return schema

    if not schema:
        return

    if schema[0] == OpName.AND:
        for predicate in schema[1:]:
            v = schema_extract_top_level(schema_fragment, predicate)
            if v:
                return v


@dataclass
class _Example:
    col1: str
    col2: int
    col3: str

_example_clause = AND(
    NOT(
        EQ(
            attr('col1'),
            'dirt'  # <- demonstrates non-callable, literal
        )
    ),
    GT(
        attr('col2'),
        5  # <- demonstrates non-callable, literal
    ),
    LIKE(
        attr('col3'),
        '%super.match.com'
    ),
    True # <- demonstrates non-callable, literal
)

assert False == _example_clause(_Example(col1='dirt', col2=7, col3='this is super.match.com')) # not asdf
assert False == _example_clause(_Example(col1='dirt', col2=3, col3='this is super.match.com')) # col2 < 5
assert False == _example_clause(_Example(col1='gold', col2=7, col3='this is super.MISmatch.com')) # col3 issue
assert False == _example_clause(_Example(col1='gold', col2=7, col3='this is super.match.com trailing thing here')) # col3 issue
assert True == _example_clause(_Example(col1='gold', col2=7, col3='this is super.match.com'))

# nesting ands just ot test "find fragment" code
_example_schema = [
    'AND',
    [
        'AND',
        [LITERAL, True],
        [
            'EQ',
            ['attr',
                [LITERAL, 'col1']
            ],
            [LITERAL, 'gold'],
        ]
    ],
    [LITERAL, True]
]

assert False == schema_to_callable(_example_schema)(_Example(col1='dirt', col2=0, col3=''))
assert True == schema_to_callable(_example_schema)(_Example(col1='gold', col2=0, col3=''))

_example_schema_exact_equal = schema_stanza(
    OpName.EQ,
    schema_stanza(OpName.attr, 'col1'),
    schema_literal('gold')
)

_example_schema_FUZZY_equal = schema_stanza(
    OpName.EQ,
    schema_stanza(OpName.attr, 'col1'),
    schema_literal(Any)
)

assert _example_schema_exact_equal == schema_extract_top_level(_example_schema_FUZZY_equal, _example_schema)
assert None == schema_extract_top_level(_example_schema_FUZZY_equal, schema_stanza(
    OpName.OR, # <- OR is the issue.. creates ambiguity about which branch is difinitive
    schema_stanza(
        OpName.EQ, # <- while this guy
        schema_stanza(OpName.attr, 'col1'),
        schema_literal('a')
    ),
    schema_stanza(
        OpName.EQ, # <- and this guy in isolation would have matched.
        schema_stanza(OpName.attr, 'col1'),
        schema_literal('b')
    )
))

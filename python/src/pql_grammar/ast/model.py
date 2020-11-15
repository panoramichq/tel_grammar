from dataclasses import dataclass
from decimal import Decimal
from typing import (
    Any,
    List,
    Optional,
    Tuple,
    Union,
)


# filled on the bottom
inventory = {}


class Node:
    pass

@dataclass
class Expr(Node):
    """ arithmetic operation like 'a > b' in Pre-fix notation"""
    operator: str
    # some operations are unary. there will be only one arg
    # most others are left-right, so len would be 2.
    # rarely there will be len more than 2.
    args: List[Any]

@dataclass
class Literal(Node):
    value: Union[int,float,str,Decimal]
    raw_value: str

@dataclass
class Taxon(Node):
    slug: str
    namespace: Optional[str] = None
    is_optional: Optional[bool] = False
    tag: Optional[str] = None

@dataclass
class Function(Node):
    function_name: str
    # Note, we supported named args.
    # args is a list of lists
    # Outer list is list of arg_name,arg_value pairs
    # If first value in pair list is Null, no arg name was provided.
    # fn(arg='value',arg2=2)
    # [['arg','value'],['arg2',2]]
    # fn('value',2)
    # [[null,'value'],[null,2]]
    args: Optional[List[List[Any]]] = None

ColumnValue = Union[Expr,Function,Taxon,Literal]

@dataclass
class Column(Node):
    value: ColumnValue
    type_cast: Optional[Function] = None
    alias: Optional[Taxon] = None

@dataclass
class Table(Node):
    value: str
    alias: Optional[str] = None

@dataclass
class SelectStmt(Node):
    columns: List[Column]
    from_clause: Optional[List[Table]] = None
    where_clause: Optional[Expr] = None

@dataclass
class SetStmt(Node):
    key: str
    value: str


inventory.update({
    k : v
    for k, v in dict(locals()).items()
    if type(v) is type and issubclass(v, Node)
})

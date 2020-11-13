from dataclasses import dataclass, fields
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
class TelExpr(Node):
    raw_value: str

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
    # support named args.
    # each tuple is a pair of arg_name=arg_value in order of occurrence.
    args: Optional[List[Tuple[Optional[str],str]]] = None

ColumnValue = Union[TelExpr,Function,Taxon,Literal]

@dataclass
class Column(Node):
    value: ColumnValue
    type_cast: Optional[Function] = None
    alias: Optional[Taxon] = None

@dataclass
class SelectStmt(Node):
    columns: List[Column]
    where_clause: Optional[Expr]


def ast_diff(a, b, path=None):
    if not path:
        path = []

    if type(a) != type(b):
        raise Exception(f"Types of {a} and {b} are not same {type(a)} != {type(b)} for path {path}")

    path += [type(a).__name__]

    if isinstance(a, Node):
        for f in fields(a):
            ast_diff(getattr(a, f.name), getattr(b, f.name), path + [f.name])
    elif isinstance(a, (list,tuple)):
        if len(a) != len(b):
            raise Exception(f"Lengths are different for {a} and {b} for path {path}")
        for i, (x,y) in enumerate(zip(a, b)):
            ast_diff(x,y, path + [i])
    else:
        if a != b:
            raise Exception(f"Values of {a} and {b} are not same for path {path}")


inventory.update({
    k : v
    for k, v in dict(locals()).items()
    if type(v) is type and issubclass(v, Node)
})

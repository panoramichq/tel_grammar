"""
- Intentionally minimalistic set of nodes to express AST of SQL-like statements and expressions
- Intentionally "frozen" (immutable) to prevent attempts to modify in-place and to allow set-like and eq operations

"""
# fmt: off

from dataclasses import dataclass
from decimal import Decimal
from typing import (
    Any,
    Optional,
    Tuple,
    Union,
)


# filled on the bottom
inventory = {}


class Node:
    pass


@dataclass(eq=True, frozen=True)
class Expr(Node):
    """ arithmetic operation like 'a > b' in Pre-fix notation"""
    operator: str
    # some operations are unary. there will be only one arg
    # most others are left-right, so len would be 2.
    # rarely there will be len more than 2.
    args: Tuple


@dataclass(eq=True, frozen=True)
class Literal(Node):
    value: Union[int,float,str,Decimal]
    raw_value: str


@dataclass(eq=True, frozen=True)
class Taxon(Node):
    slug: str
    namespace: Optional[str] = None
    is_optional: Optional[bool] = False
    tag: Optional[str] = None

    @property
    def value(self):
        is_optional = '?' if self.is_optional else ''
        namespace = self.namespace + '|' if self.namespace else ''
        slug = self.slug
        tag = ':' + self.tag if self.tag else ''
        return f'{is_optional}{namespace}{slug}{tag}'


CallArgs = Tuple[Optional[str],Any]


@dataclass(eq=True, frozen=True)
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
    args: Optional[Tuple[CallArgs, ...]] = None


inventory.update({
    k : v
    for k, v in dict(locals()).items()
    if type(v) is type and issubclass(v, Node)
})

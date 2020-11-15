from dataclasses import fields
from typing import Callable, Iterator, Any
from . import model as ast


def ast_diff(a, b, path=None):
    if not path:
        path = []

    if type(a) != type(b):
        raise Exception(f"Types of {a} and {b} are not same {type(a)} != {type(b)} for path {path}")

    path += [type(a).__name__]

    if isinstance(a, ast.Node):
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

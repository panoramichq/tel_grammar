from dataclasses import fields
from typing import List, Tuple, Any
from . import model as ast


AST_NODE_MARKER = '__type__'


def from_json(o: dict):

    if isinstance(o, dict) and AST_NODE_MARKER in o:
        name = o[AST_NODE_MARKER]
        N = ast.inventory.get(name)
        if not N:
            raise NotImplementedError(f'Renderer for node type "{name}" is not implemented.')

        return N(**{
            k: from_json(v)
            for k, v in o.items()
            if k != AST_NODE_MARKER
        })

    if isinstance(o, (list, tuple)):
        return [
            from_json(v)
            for v in o
        ]

    if isinstance(o, dict):
        return {
            k: from_json(v)
            for k, v in o.items()
        }

    return o

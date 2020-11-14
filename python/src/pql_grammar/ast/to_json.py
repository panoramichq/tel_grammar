from dataclasses import fields
from . import model as ast


TYPE_ATTRIBUTE = '__typename'  # GraphQL style


def node_to_tuples(n: ast.Node):
    return [
        (TYPE_ATTRIBUTE, n.__class__.__name__)
    ] + [
        (field.name, getattr(n, field.name))
        for field in fields(n)
    ]


def to_json(o):

    if isinstance(o, ast.Node):
        return {
            k: to_json(v)
            for k, v in node_to_tuples(o)
            if not (v is None)  # <-- diff from to_data_tuple
        }

    if isinstance(o, (list, tuple)):
        return [
            to_json(v)
            for v in o
            # if not (v is None)  # <-- diff from to_data_tuple
        ]

    if isinstance(o, dict):
        return {
            k: to_json(v)
            for k, v in o.items()
            if not (v is None)  # <-- diff from to_data_tuple
        }

    return o

# fmt: off

from . import model as ast


TYPE_ATTRIBUTE = '__typename'  # GraphQL style


def from_json(o: dict):

    if isinstance(o, dict) and TYPE_ATTRIBUTE in o:
        name = o[TYPE_ATTRIBUTE]
        N = ast.inventory.get(name)
        if not N:
            raise NotImplementedError(f'Renderer for node type "{name}" is not implemented.')

        try:
            return N(**{
                k: from_json(v)
                for k, v in o.items()
                if k != TYPE_ATTRIBUTE
            })
        except TypeError as ex:
            raise TypeError(f"'{ex}' While processing {N} {o}")

    if isinstance(o, (list, tuple)):
        return tuple([
            from_json(v)
            for v in o
        ])

    if isinstance(o, dict):
        return {
            k: from_json(v)
            for k, v in o.items()
        }

    return o

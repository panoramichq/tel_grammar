# fmt: off

from typing import List
from . import model as ast


FIRST=0
SECOND=1
LAST=-1

INDENT = ' ' * 4


# populated further below, at the end of this file on module init.
renderer_map = {}


class Node:
    def __init__(self, n):
        self.n = n

    def __str__(self):
        raise NotImplementedError(f'Renderer for "{self.n}" is not implemented.')


class Expr(Node):
    n: ast.Expr
    def __str__(self):
        op = self.n.operator
        if len(self.n.args) == 1:
            right = self.n.args[FIRST]
            # could be something like 'NOT' which needs padding
            padding = '' if op in ('+','-') else ' '
            return f'{op}{padding}{to_r(right)}'
        else:
            left = self.n.args[FIRST]
            right = self.n.args[SECOND]
            return f'({to_r(left)} {op} {to_r(right)})'


class Literal(Node):
    n: ast.Literal
    def __str__(self):
        return self.n.raw_value


class Taxon(Node):
    n: ast.Taxon
    def __str__(self):
        n = self.n
        is_optional = '?' if n.is_optional else ''
        namespace = n.namespace + '|' if n.namespace else ''
        slug = n.slug
        tag = ':' + n.tag if n.tag else ''
        return f'{is_optional}{namespace}{slug}{tag}'


class Function(Node):
    n: ast.Function
    def __str__(self):
        fn = self.n.function_name
        # args are string pairs, not parsed deeper at all.
        args = ','.join([
            f'{n}={to_r(v)}' if n else f'{to_r(v)}'
            for n, v in (self.n.args or [])
        ])
        return f'{fn}({args})'


class Column(Node):
    n: ast.Column
    def __str__(self):
        n = self.n
        value = f'{to_r(n.value)}'
        type_cast = f'::{to_r(n.type_cast)}' if n.type_cast else ''
        if type_cast and (value[FIRST] != '(' or value[LAST] != ')'):
            value = f'({value})'
        alias = f' AS {to_r(n.alias)}' if n.alias else ''
        return f'{value}{type_cast}{alias}'


class Table(Node):
    n: ast.Table
    def __str__(self):
        n = self.n
        value = n.value
        alias = f' AS {n.alias}' if n.alias else ''
        return f'{value}{alias}'


class SelectStmt(Node):
    n: ast.SelectStmt
    def __str__(self):
        n = self.n
        select_str = 'SELECT\n' + INDENT + (',\n' + INDENT).join(map(str, map(Column, n.columns))) + '\n'
        from_str = 'FROM\n' + INDENT + (',\n' + INDENT).join(map(str, map(Table, n.from_clause))) + '\n'
        where_str = 'WHERE\n' + INDENT + str(to_r(n.where_clause)) + '\n'
        return select_str + from_str + where_str + ';\n'


def to_r(n: ast.Node):
    if isinstance(n, ast.Node):
        return renderer_map.get(type(n), Node)(n)
    return str(n)


def to_pql(o: List[ast.Node]):
    if not isinstance(o, (list, tuple)):
        raise AttributeError(f"Argument must be a list of statements.")
    return '\n'.join([
        str(to_r(e))
        for e in o
    ])


renderer_map.update({
    getattr(ast, k) : v
    for k, v in dict(locals()).items()
    if type(v) is type and issubclass(v, Node) and hasattr(ast, k)
})

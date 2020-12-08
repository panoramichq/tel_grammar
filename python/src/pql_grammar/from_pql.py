# fmt: off

from antlr4 import (
    CommonTokenStream,
    InputStream,
    ParserRuleContext,
    RecognitionException,
    Recognizer,
    Token,
)

from typing import Type

from .antlr.PqlLexer import PqlLexer
from .antlr.PqlParser import PqlParser

from . import model as ast
from .antlr_tel_to_ast_visitor import ParseError, TelVisitor, TelErrorListener


def from_tel(tel: str, cls:Type[TelVisitor] = TelVisitor) -> ast.Node:
    inp_stream = InputStream(tel)
    error_listener = TelErrorListener()
    lexer = PqlLexer(inp_stream)
    lexer.removeErrorListeners()  # default is PrintToConsole
    lexer.addErrorListener(error_listener)
    stream = CommonTokenStream(lexer)
    parser = PqlParser(stream)
    parser.removeErrorListeners()  # default is PrintToConsole
    parser.addErrorListener(error_listener)
    tree = parser.parseTel()
    return cls().visit(tree)

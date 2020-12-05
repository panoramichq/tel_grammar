# Generated from grammar/PqlParser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PqlParser import PqlParser
else:
    from PqlParser import PqlParser

# This class defines a complete generic visitor for a parse tree produced by PqlParser.

class PqlParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PqlParser#parseTel.
    def visitParseTel(self, ctx:PqlParser.ParseTelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PqlParser#expr.
    def visitExpr(self, ctx:PqlParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PqlParser#fn.
    def visitFn(self, ctx:PqlParser.FnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PqlParser#exprList.
    def visitExprList(self, ctx:PqlParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PqlParser#taxon.
    def visitTaxon(self, ctx:PqlParser.TaxonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PqlParser#identifierMultipart.
    def visitIdentifierMultipart(self, ctx:PqlParser.IdentifierMultipartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PqlParser#literalValue.
    def visitLiteralValue(self, ctx:PqlParser.LiteralValueContext):
        return self.visitChildren(ctx)



del PqlParser
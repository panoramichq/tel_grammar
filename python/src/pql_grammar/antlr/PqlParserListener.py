# Generated from grammar/PqlParser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PqlParser import PqlParser
else:
    from PqlParser import PqlParser

# This class defines a complete listener for a parse tree produced by PqlParser.
class PqlParserListener(ParseTreeListener):

    # Enter a parse tree produced by PqlParser#parseTel.
    def enterParseTel(self, ctx:PqlParser.ParseTelContext):
        pass

    # Exit a parse tree produced by PqlParser#parseTel.
    def exitParseTel(self, ctx:PqlParser.ParseTelContext):
        pass


    # Enter a parse tree produced by PqlParser#expr.
    def enterExpr(self, ctx:PqlParser.ExprContext):
        pass

    # Exit a parse tree produced by PqlParser#expr.
    def exitExpr(self, ctx:PqlParser.ExprContext):
        pass


    # Enter a parse tree produced by PqlParser#exprList.
    def enterExprList(self, ctx:PqlParser.ExprListContext):
        pass

    # Exit a parse tree produced by PqlParser#exprList.
    def exitExprList(self, ctx:PqlParser.ExprListContext):
        pass


    # Enter a parse tree produced by PqlParser#fn.
    def enterFn(self, ctx:PqlParser.FnContext):
        pass

    # Exit a parse tree produced by PqlParser#fn.
    def exitFn(self, ctx:PqlParser.FnContext):
        pass


    # Enter a parse tree produced by PqlParser#fnArgs.
    def enterFnArgs(self, ctx:PqlParser.FnArgsContext):
        pass

    # Exit a parse tree produced by PqlParser#fnArgs.
    def exitFnArgs(self, ctx:PqlParser.FnArgsContext):
        pass


    # Enter a parse tree produced by PqlParser#fnArg.
    def enterFnArg(self, ctx:PqlParser.FnArgContext):
        pass

    # Exit a parse tree produced by PqlParser#fnArg.
    def exitFnArg(self, ctx:PqlParser.FnArgContext):
        pass


    # Enter a parse tree produced by PqlParser#taxon.
    def enterTaxon(self, ctx:PqlParser.TaxonContext):
        pass

    # Exit a parse tree produced by PqlParser#taxon.
    def exitTaxon(self, ctx:PqlParser.TaxonContext):
        pass


    # Enter a parse tree produced by PqlParser#identifierMultipart.
    def enterIdentifierMultipart(self, ctx:PqlParser.IdentifierMultipartContext):
        pass

    # Exit a parse tree produced by PqlParser#identifierMultipart.
    def exitIdentifierMultipart(self, ctx:PqlParser.IdentifierMultipartContext):
        pass


    # Enter a parse tree produced by PqlParser#literalValue.
    def enterLiteralValue(self, ctx:PqlParser.LiteralValueContext):
        pass

    # Exit a parse tree produced by PqlParser#literalValue.
    def exitLiteralValue(self, ctx:PqlParser.LiteralValueContext):
        pass



del PqlParser
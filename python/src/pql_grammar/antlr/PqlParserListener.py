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


    # Enter a parse tree produced by PqlParser#parsePql.
    def enterParsePql(self, ctx:PqlParser.ParsePqlContext):
        pass

    # Exit a parse tree produced by PqlParser#parsePql.
    def exitParsePql(self, ctx:PqlParser.ParsePqlContext):
        pass


    # Enter a parse tree produced by PqlParser#sqlStmtList.
    def enterSqlStmtList(self, ctx:PqlParser.SqlStmtListContext):
        pass

    # Exit a parse tree produced by PqlParser#sqlStmtList.
    def exitSqlStmtList(self, ctx:PqlParser.SqlStmtListContext):
        pass


    # Enter a parse tree produced by PqlParser#sqlStmt.
    def enterSqlStmt(self, ctx:PqlParser.SqlStmtContext):
        pass

    # Exit a parse tree produced by PqlParser#sqlStmt.
    def exitSqlStmt(self, ctx:PqlParser.SqlStmtContext):
        pass


    # Enter a parse tree produced by PqlParser#setStmt.
    def enterSetStmt(self, ctx:PqlParser.SetStmtContext):
        pass

    # Exit a parse tree produced by PqlParser#setStmt.
    def exitSetStmt(self, ctx:PqlParser.SetStmtContext):
        pass


    # Enter a parse tree produced by PqlParser#selectStmt.
    def enterSelectStmt(self, ctx:PqlParser.SelectStmtContext):
        pass

    # Exit a parse tree produced by PqlParser#selectStmt.
    def exitSelectStmt(self, ctx:PqlParser.SelectStmtContext):
        pass


    # Enter a parse tree produced by PqlParser#selectClause.
    def enterSelectClause(self, ctx:PqlParser.SelectClauseContext):
        pass

    # Exit a parse tree produced by PqlParser#selectClause.
    def exitSelectClause(self, ctx:PqlParser.SelectClauseContext):
        pass


    # Enter a parse tree produced by PqlParser#columns.
    def enterColumns(self, ctx:PqlParser.ColumnsContext):
        pass

    # Exit a parse tree produced by PqlParser#columns.
    def exitColumns(self, ctx:PqlParser.ColumnsContext):
        pass


    # Enter a parse tree produced by PqlParser#fromClause.
    def enterFromClause(self, ctx:PqlParser.FromClauseContext):
        pass

    # Exit a parse tree produced by PqlParser#fromClause.
    def exitFromClause(self, ctx:PqlParser.FromClauseContext):
        pass


    # Enter a parse tree produced by PqlParser#tables.
    def enterTables(self, ctx:PqlParser.TablesContext):
        pass

    # Exit a parse tree produced by PqlParser#tables.
    def exitTables(self, ctx:PqlParser.TablesContext):
        pass


    # Enter a parse tree produced by PqlParser#whereClause.
    def enterWhereClause(self, ctx:PqlParser.WhereClauseContext):
        pass

    # Exit a parse tree produced by PqlParser#whereClause.
    def exitWhereClause(self, ctx:PqlParser.WhereClauseContext):
        pass


    # Enter a parse tree produced by PqlParser#orderByClause.
    def enterOrderByClause(self, ctx:PqlParser.OrderByClauseContext):
        pass

    # Exit a parse tree produced by PqlParser#orderByClause.
    def exitOrderByClause(self, ctx:PqlParser.OrderByClauseContext):
        pass


    # Enter a parse tree produced by PqlParser#orderExpr.
    def enterOrderExpr(self, ctx:PqlParser.OrderExprContext):
        pass

    # Exit a parse tree produced by PqlParser#orderExpr.
    def exitOrderExpr(self, ctx:PqlParser.OrderExprContext):
        pass


    # Enter a parse tree produced by PqlParser#limitClause.
    def enterLimitClause(self, ctx:PqlParser.LimitClauseContext):
        pass

    # Exit a parse tree produced by PqlParser#limitClause.
    def exitLimitClause(self, ctx:PqlParser.LimitClauseContext):
        pass


    # Enter a parse tree produced by PqlParser#expr.
    def enterExpr(self, ctx:PqlParser.ExprContext):
        pass

    # Exit a parse tree produced by PqlParser#expr.
    def exitExpr(self, ctx:PqlParser.ExprContext):
        pass


    # Enter a parse tree produced by PqlParser#function.
    def enterFunction(self, ctx:PqlParser.FunctionContext):
        pass

    # Exit a parse tree produced by PqlParser#function.
    def exitFunction(self, ctx:PqlParser.FunctionContext):
        pass


    # Enter a parse tree produced by PqlParser#exprList.
    def enterExprList(self, ctx:PqlParser.ExprListContext):
        pass

    # Exit a parse tree produced by PqlParser#exprList.
    def exitExprList(self, ctx:PqlParser.ExprListContext):
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
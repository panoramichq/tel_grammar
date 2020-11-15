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


    # Visit a parse tree produced by PqlParser#parsePql.
    def visitParsePql(self, ctx:PqlParser.ParsePqlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PqlParser#sqlStmtList.
    def visitSqlStmtList(self, ctx:PqlParser.SqlStmtListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PqlParser#sqlStmt.
    def visitSqlStmt(self, ctx:PqlParser.SqlStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PqlParser#setStmt.
    def visitSetStmt(self, ctx:PqlParser.SetStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PqlParser#selectStmt.
    def visitSelectStmt(self, ctx:PqlParser.SelectStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PqlParser#selectClause.
    def visitSelectClause(self, ctx:PqlParser.SelectClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PqlParser#columns.
    def visitColumns(self, ctx:PqlParser.ColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PqlParser#fromClause.
    def visitFromClause(self, ctx:PqlParser.FromClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PqlParser#tables.
    def visitTables(self, ctx:PqlParser.TablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PqlParser#whereClause.
    def visitWhereClause(self, ctx:PqlParser.WhereClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PqlParser#orderByClause.
    def visitOrderByClause(self, ctx:PqlParser.OrderByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PqlParser#orderExpr.
    def visitOrderExpr(self, ctx:PqlParser.OrderExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PqlParser#limitClause.
    def visitLimitClause(self, ctx:PqlParser.LimitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PqlParser#expr.
    def visitExpr(self, ctx:PqlParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PqlParser#function.
    def visitFunction(self, ctx:PqlParser.FunctionContext):
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
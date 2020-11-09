// Generated from grammar/PqlParser.g4 by ANTLR 4.8
// jshint ignore: start
var antlr4 = require('antlr4/index');

// This class defines a complete listener for a parse tree produced by PqlParser.
function PqlParserListener() {
	antlr4.tree.ParseTreeListener.call(this);
	return this;
}

PqlParserListener.prototype = Object.create(antlr4.tree.ParseTreeListener.prototype);
PqlParserListener.prototype.constructor = PqlParserListener;

// Enter a parse tree produced by PqlParser#parseTel.
PqlParserListener.prototype.enterParseTel = function(ctx) {
};

// Exit a parse tree produced by PqlParser#parseTel.
PqlParserListener.prototype.exitParseTel = function(ctx) {
};


// Enter a parse tree produced by PqlParser#parsePql.
PqlParserListener.prototype.enterParsePql = function(ctx) {
};

// Exit a parse tree produced by PqlParser#parsePql.
PqlParserListener.prototype.exitParsePql = function(ctx) {
};


// Enter a parse tree produced by PqlParser#sqlStmtList.
PqlParserListener.prototype.enterSqlStmtList = function(ctx) {
};

// Exit a parse tree produced by PqlParser#sqlStmtList.
PqlParserListener.prototype.exitSqlStmtList = function(ctx) {
};


// Enter a parse tree produced by PqlParser#sqlStmt.
PqlParserListener.prototype.enterSqlStmt = function(ctx) {
};

// Exit a parse tree produced by PqlParser#sqlStmt.
PqlParserListener.prototype.exitSqlStmt = function(ctx) {
};


// Enter a parse tree produced by PqlParser#selectStmt.
PqlParserListener.prototype.enterSelectStmt = function(ctx) {
};

// Exit a parse tree produced by PqlParser#selectStmt.
PqlParserListener.prototype.exitSelectStmt = function(ctx) {
};


// Enter a parse tree produced by PqlParser#columns.
PqlParserListener.prototype.enterColumns = function(ctx) {
};

// Exit a parse tree produced by PqlParser#columns.
PqlParserListener.prototype.exitColumns = function(ctx) {
};


// Enter a parse tree produced by PqlParser#whereClause.
PqlParserListener.prototype.enterWhereClause = function(ctx) {
};

// Exit a parse tree produced by PqlParser#whereClause.
PqlParserListener.prototype.exitWhereClause = function(ctx) {
};


// Enter a parse tree produced by PqlParser#orderByClause.
PqlParserListener.prototype.enterOrderByClause = function(ctx) {
};

// Exit a parse tree produced by PqlParser#orderByClause.
PqlParserListener.prototype.exitOrderByClause = function(ctx) {
};


// Enter a parse tree produced by PqlParser#orderExpr.
PqlParserListener.prototype.enterOrderExpr = function(ctx) {
};

// Exit a parse tree produced by PqlParser#orderExpr.
PqlParserListener.prototype.exitOrderExpr = function(ctx) {
};


// Enter a parse tree produced by PqlParser#limitClause.
PqlParserListener.prototype.enterLimitClause = function(ctx) {
};

// Exit a parse tree produced by PqlParser#limitClause.
PqlParserListener.prototype.exitLimitClause = function(ctx) {
};


// Enter a parse tree produced by PqlParser#expr.
PqlParserListener.prototype.enterExpr = function(ctx) {
};

// Exit a parse tree produced by PqlParser#expr.
PqlParserListener.prototype.exitExpr = function(ctx) {
};


// Enter a parse tree produced by PqlParser#taxon.
PqlParserListener.prototype.enterTaxon = function(ctx) {
};

// Exit a parse tree produced by PqlParser#taxon.
PqlParserListener.prototype.exitTaxon = function(ctx) {
};


// Enter a parse tree produced by PqlParser#identifierMultipart.
PqlParserListener.prototype.enterIdentifierMultipart = function(ctx) {
};

// Exit a parse tree produced by PqlParser#identifierMultipart.
PqlParserListener.prototype.exitIdentifierMultipart = function(ctx) {
};


// Enter a parse tree produced by PqlParser#literalValue.
PqlParserListener.prototype.enterLiteralValue = function(ctx) {
};

// Exit a parse tree produced by PqlParser#literalValue.
PqlParserListener.prototype.exitLiteralValue = function(ctx) {
};



exports.PqlParserListener = PqlParserListener;
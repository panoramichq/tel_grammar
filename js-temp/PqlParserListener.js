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


// Enter a parse tree produced by PqlParser#expr.
PqlParserListener.prototype.enterExpr = function(ctx) {
};

// Exit a parse tree produced by PqlParser#expr.
PqlParserListener.prototype.exitExpr = function(ctx) {
};


// Enter a parse tree produced by PqlParser#exprList.
PqlParserListener.prototype.enterExprList = function(ctx) {
};

// Exit a parse tree produced by PqlParser#exprList.
PqlParserListener.prototype.exitExprList = function(ctx) {
};


// Enter a parse tree produced by PqlParser#fn.
PqlParserListener.prototype.enterFn = function(ctx) {
};

// Exit a parse tree produced by PqlParser#fn.
PqlParserListener.prototype.exitFn = function(ctx) {
};


// Enter a parse tree produced by PqlParser#fnArgs.
PqlParserListener.prototype.enterFnArgs = function(ctx) {
};

// Exit a parse tree produced by PqlParser#fnArgs.
PqlParserListener.prototype.exitFnArgs = function(ctx) {
};


// Enter a parse tree produced by PqlParser#fnArg.
PqlParserListener.prototype.enterFnArg = function(ctx) {
};

// Exit a parse tree produced by PqlParser#fnArg.
PqlParserListener.prototype.exitFnArg = function(ctx) {
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
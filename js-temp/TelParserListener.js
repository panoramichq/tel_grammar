// Generated from grammar/TelParser.g4 by ANTLR 4.8
// jshint ignore: start
var antlr4 = require('antlr4/index');

// This class defines a complete listener for a parse tree produced by TelParser.
function TelParserListener() {
	antlr4.tree.ParseTreeListener.call(this);
	return this;
}

TelParserListener.prototype = Object.create(antlr4.tree.ParseTreeListener.prototype);
TelParserListener.prototype.constructor = TelParserListener;

// Enter a parse tree produced by TelParser#parse.
TelParserListener.prototype.enterParse = function(ctx) {
};

// Exit a parse tree produced by TelParser#parse.
TelParserListener.prototype.exitParse = function(ctx) {
};


// Enter a parse tree produced by TelParser#expr.
TelParserListener.prototype.enterExpr = function(ctx) {
};

// Exit a parse tree produced by TelParser#expr.
TelParserListener.prototype.exitExpr = function(ctx) {
};


// Enter a parse tree produced by TelParser#isNotNull.
TelParserListener.prototype.enterIsNotNull = function(ctx) {
};

// Exit a parse tree produced by TelParser#isNotNull.
TelParserListener.prototype.exitIsNotNull = function(ctx) {
};


// Enter a parse tree produced by TelParser#isNull.
TelParserListener.prototype.enterIsNull = function(ctx) {
};

// Exit a parse tree produced by TelParser#isNull.
TelParserListener.prototype.exitIsNull = function(ctx) {
};


// Enter a parse tree produced by TelParser#taxon.
TelParserListener.prototype.enterTaxon = function(ctx) {
};

// Exit a parse tree produced by TelParser#taxon.
TelParserListener.prototype.exitTaxon = function(ctx) {
};


// Enter a parse tree produced by TelParser#identifierMultipart.
TelParserListener.prototype.enterIdentifierMultipart = function(ctx) {
};

// Exit a parse tree produced by TelParser#identifierMultipart.
TelParserListener.prototype.exitIdentifierMultipart = function(ctx) {
};


// Enter a parse tree produced by TelParser#literalValue.
TelParserListener.prototype.enterLiteralValue = function(ctx) {
};

// Exit a parse tree produced by TelParser#literalValue.
TelParserListener.prototype.exitLiteralValue = function(ctx) {
};



exports.TelParserListener = TelParserListener;
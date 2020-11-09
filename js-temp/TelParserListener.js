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


// Enter a parse tree produced by TelParser#nullTestExpr.
TelParserListener.prototype.enterNullTestExpr = function(ctx) {
};

// Exit a parse tree produced by TelParser#nullTestExpr.
TelParserListener.prototype.exitNullTestExpr = function(ctx) {
};


// Enter a parse tree produced by TelParser#notExpr.
TelParserListener.prototype.enterNotExpr = function(ctx) {
};

// Exit a parse tree produced by TelParser#notExpr.
TelParserListener.prototype.exitNotExpr = function(ctx) {
};


// Enter a parse tree produced by TelParser#logicalExpr.
TelParserListener.prototype.enterLogicalExpr = function(ctx) {
};

// Exit a parse tree produced by TelParser#logicalExpr.
TelParserListener.prototype.exitLogicalExpr = function(ctx) {
};


// Enter a parse tree produced by TelParser#multiplicationExpr.
TelParserListener.prototype.enterMultiplicationExpr = function(ctx) {
};

// Exit a parse tree produced by TelParser#multiplicationExpr.
TelParserListener.prototype.exitMultiplicationExpr = function(ctx) {
};


// Enter a parse tree produced by TelParser#atomExpr.
TelParserListener.prototype.enterAtomExpr = function(ctx) {
};

// Exit a parse tree produced by TelParser#atomExpr.
TelParserListener.prototype.exitAtomExpr = function(ctx) {
};


// Enter a parse tree produced by TelParser#additiveExpr.
TelParserListener.prototype.enterAdditiveExpr = function(ctx) {
};

// Exit a parse tree produced by TelParser#additiveExpr.
TelParserListener.prototype.exitAdditiveExpr = function(ctx) {
};


// Enter a parse tree produced by TelParser#bracketExpr.
TelParserListener.prototype.enterBracketExpr = function(ctx) {
};

// Exit a parse tree produced by TelParser#bracketExpr.
TelParserListener.prototype.exitBracketExpr = function(ctx) {
};


// Enter a parse tree produced by TelParser#numberAtom.
TelParserListener.prototype.enterNumberAtom = function(ctx) {
};

// Exit a parse tree produced by TelParser#numberAtom.
TelParserListener.prototype.exitNumberAtom = function(ctx) {
};


// Enter a parse tree produced by TelParser#booleanAtom.
TelParserListener.prototype.enterBooleanAtom = function(ctx) {
};

// Exit a parse tree produced by TelParser#booleanAtom.
TelParserListener.prototype.exitBooleanAtom = function(ctx) {
};


// Enter a parse tree produced by TelParser#singleQuotedAtom.
TelParserListener.prototype.enterSingleQuotedAtom = function(ctx) {
};

// Exit a parse tree produced by TelParser#singleQuotedAtom.
TelParserListener.prototype.exitSingleQuotedAtom = function(ctx) {
};


// Enter a parse tree produced by TelParser#stringConstantAtom.
TelParserListener.prototype.enterStringConstantAtom = function(ctx) {
};

// Exit a parse tree produced by TelParser#stringConstantAtom.
TelParserListener.prototype.exitStringConstantAtom = function(ctx) {
};


// Enter a parse tree produced by TelParser#fnExpr.
TelParserListener.prototype.enterFnExpr = function(ctx) {
};

// Exit a parse tree produced by TelParser#fnExpr.
TelParserListener.prototype.exitFnExpr = function(ctx) {
};


// Enter a parse tree produced by TelParser#taxonSlugAtom.
TelParserListener.prototype.enterTaxonSlugAtom = function(ctx) {
};

// Exit a parse tree produced by TelParser#taxonSlugAtom.
TelParserListener.prototype.exitTaxonSlugAtom = function(ctx) {
};


// Enter a parse tree produced by TelParser#fn.
TelParserListener.prototype.enterFn = function(ctx) {
};

// Exit a parse tree produced by TelParser#fn.
TelParserListener.prototype.exitFn = function(ctx) {
};


// Enter a parse tree produced by TelParser#taxon.
TelParserListener.prototype.enterTaxon = function(ctx) {
};

// Exit a parse tree produced by TelParser#taxon.
TelParserListener.prototype.exitTaxon = function(ctx) {
};



exports.TelParserListener = TelParserListener;
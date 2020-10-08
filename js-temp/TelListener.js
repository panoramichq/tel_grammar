// Generated from grammar/Tel.g4 by ANTLR 4.8
// jshint ignore: start
var antlr4 = require('antlr4/index');

// This class defines a complete listener for a parse tree produced by TelParser.
function TelListener() {
	antlr4.tree.ParseTreeListener.call(this);
	return this;
}

TelListener.prototype = Object.create(antlr4.tree.ParseTreeListener.prototype);
TelListener.prototype.constructor = TelListener;

// Enter a parse tree produced by TelParser#fn.
TelListener.prototype.enterFn = function(ctx) {
};

// Exit a parse tree produced by TelParser#fn.
TelListener.prototype.exitFn = function(ctx) {
};


// Enter a parse tree produced by TelParser#taxon.
TelListener.prototype.enterTaxon = function(ctx) {
};

// Exit a parse tree produced by TelParser#taxon.
TelListener.prototype.exitTaxon = function(ctx) {
};


// Enter a parse tree produced by TelParser#taxon_expr.
TelListener.prototype.enterTaxon_expr = function(ctx) {
};

// Exit a parse tree produced by TelParser#taxon_expr.
TelListener.prototype.exitTaxon_expr = function(ctx) {
};


// Enter a parse tree produced by TelParser#parse.
TelListener.prototype.enterParse = function(ctx) {
};

// Exit a parse tree produced by TelParser#parse.
TelListener.prototype.exitParse = function(ctx) {
};


// Enter a parse tree produced by TelParser#nullTestExpr.
TelListener.prototype.enterNullTestExpr = function(ctx) {
};

// Exit a parse tree produced by TelParser#nullTestExpr.
TelListener.prototype.exitNullTestExpr = function(ctx) {
};


// Enter a parse tree produced by TelParser#notExpr.
TelListener.prototype.enterNotExpr = function(ctx) {
};

// Exit a parse tree produced by TelParser#notExpr.
TelListener.prototype.exitNotExpr = function(ctx) {
};


// Enter a parse tree produced by TelParser#logicalExpr.
TelListener.prototype.enterLogicalExpr = function(ctx) {
};

// Exit a parse tree produced by TelParser#logicalExpr.
TelListener.prototype.exitLogicalExpr = function(ctx) {
};


// Enter a parse tree produced by TelParser#multiplicationExpr.
TelListener.prototype.enterMultiplicationExpr = function(ctx) {
};

// Exit a parse tree produced by TelParser#multiplicationExpr.
TelListener.prototype.exitMultiplicationExpr = function(ctx) {
};


// Enter a parse tree produced by TelParser#atomExpr.
TelListener.prototype.enterAtomExpr = function(ctx) {
};

// Exit a parse tree produced by TelParser#atomExpr.
TelListener.prototype.exitAtomExpr = function(ctx) {
};


// Enter a parse tree produced by TelParser#additiveExpr.
TelListener.prototype.enterAdditiveExpr = function(ctx) {
};

// Exit a parse tree produced by TelParser#additiveExpr.
TelListener.prototype.exitAdditiveExpr = function(ctx) {
};


// Enter a parse tree produced by TelParser#bracketExpr.
TelListener.prototype.enterBracketExpr = function(ctx) {
};

// Exit a parse tree produced by TelParser#bracketExpr.
TelListener.prototype.exitBracketExpr = function(ctx) {
};


// Enter a parse tree produced by TelParser#numberAtom.
TelListener.prototype.enterNumberAtom = function(ctx) {
};

// Exit a parse tree produced by TelParser#numberAtom.
TelListener.prototype.exitNumberAtom = function(ctx) {
};


// Enter a parse tree produced by TelParser#fnExpr.
TelListener.prototype.enterFnExpr = function(ctx) {
};

// Exit a parse tree produced by TelParser#fnExpr.
TelListener.prototype.exitFnExpr = function(ctx) {
};


// Enter a parse tree produced by TelParser#booleanAtom.
TelListener.prototype.enterBooleanAtom = function(ctx) {
};

// Exit a parse tree produced by TelParser#booleanAtom.
TelListener.prototype.exitBooleanAtom = function(ctx) {
};


// Enter a parse tree produced by TelParser#taxonSlugAtom.
TelListener.prototype.enterTaxonSlugAtom = function(ctx) {
};

// Exit a parse tree produced by TelParser#taxonSlugAtom.
TelListener.prototype.exitTaxonSlugAtom = function(ctx) {
};


// Enter a parse tree produced by TelParser#singleQuotedAtom.
TelListener.prototype.enterSingleQuotedAtom = function(ctx) {
};

// Exit a parse tree produced by TelParser#singleQuotedAtom.
TelListener.prototype.exitSingleQuotedAtom = function(ctx) {
};


// Enter a parse tree produced by TelParser#stringConstantAtom.
TelListener.prototype.enterStringConstantAtom = function(ctx) {
};

// Exit a parse tree produced by TelParser#stringConstantAtom.
TelListener.prototype.exitStringConstantAtom = function(ctx) {
};



exports.TelListener = TelListener;
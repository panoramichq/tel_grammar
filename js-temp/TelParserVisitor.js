// Generated from grammar/TelParser.g4 by ANTLR 4.8
// jshint ignore: start
var antlr4 = require('antlr4/index');

// This class defines a complete generic visitor for a parse tree produced by TelParser.

function TelParserVisitor() {
	antlr4.tree.ParseTreeVisitor.call(this);
	return this;
}

TelParserVisitor.prototype = Object.create(antlr4.tree.ParseTreeVisitor.prototype);
TelParserVisitor.prototype.constructor = TelParserVisitor;

// Visit a parse tree produced by TelParser#parse.
TelParserVisitor.prototype.visitParse = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#nullTestExpr.
TelParserVisitor.prototype.visitNullTestExpr = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#notExpr.
TelParserVisitor.prototype.visitNotExpr = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#logicalExpr.
TelParserVisitor.prototype.visitLogicalExpr = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#multiplicationExpr.
TelParserVisitor.prototype.visitMultiplicationExpr = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#atomExpr.
TelParserVisitor.prototype.visitAtomExpr = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#additiveExpr.
TelParserVisitor.prototype.visitAdditiveExpr = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#bracketExpr.
TelParserVisitor.prototype.visitBracketExpr = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#numberAtom.
TelParserVisitor.prototype.visitNumberAtom = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#booleanAtom.
TelParserVisitor.prototype.visitBooleanAtom = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#singleQuotedAtom.
TelParserVisitor.prototype.visitSingleQuotedAtom = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#stringConstantAtom.
TelParserVisitor.prototype.visitStringConstantAtom = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#fnExpr.
TelParserVisitor.prototype.visitFnExpr = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#taxonSlugAtom.
TelParserVisitor.prototype.visitTaxonSlugAtom = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#fn.
TelParserVisitor.prototype.visitFn = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#taxon.
TelParserVisitor.prototype.visitTaxon = function(ctx) {
  return this.visitChildren(ctx);
};



exports.TelParserVisitor = TelParserVisitor;
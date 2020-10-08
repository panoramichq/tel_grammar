// Generated from grammar/Tel.g4 by ANTLR 4.8
// jshint ignore: start
var antlr4 = require('antlr4/index');

// This class defines a complete generic visitor for a parse tree produced by TelParser.

function TelVisitor() {
	antlr4.tree.ParseTreeVisitor.call(this);
	return this;
}

TelVisitor.prototype = Object.create(antlr4.tree.ParseTreeVisitor.prototype);
TelVisitor.prototype.constructor = TelVisitor;

// Visit a parse tree produced by TelParser#fn.
TelVisitor.prototype.visitFn = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#taxon.
TelVisitor.prototype.visitTaxon = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#taxon_expr.
TelVisitor.prototype.visitTaxon_expr = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#parse.
TelVisitor.prototype.visitParse = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#nullTestExpr.
TelVisitor.prototype.visitNullTestExpr = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#notExpr.
TelVisitor.prototype.visitNotExpr = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#logicalExpr.
TelVisitor.prototype.visitLogicalExpr = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#multiplicationExpr.
TelVisitor.prototype.visitMultiplicationExpr = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#atomExpr.
TelVisitor.prototype.visitAtomExpr = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#additiveExpr.
TelVisitor.prototype.visitAdditiveExpr = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#bracketExpr.
TelVisitor.prototype.visitBracketExpr = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#numberAtom.
TelVisitor.prototype.visitNumberAtom = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#fnExpr.
TelVisitor.prototype.visitFnExpr = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#booleanAtom.
TelVisitor.prototype.visitBooleanAtom = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#taxonSlugAtom.
TelVisitor.prototype.visitTaxonSlugAtom = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#singleQuotedAtom.
TelVisitor.prototype.visitSingleQuotedAtom = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#stringConstantAtom.
TelVisitor.prototype.visitStringConstantAtom = function(ctx) {
  return this.visitChildren(ctx);
};



exports.TelVisitor = TelVisitor;
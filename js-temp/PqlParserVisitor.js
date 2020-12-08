// Generated from grammar/PqlParser.g4 by ANTLR 4.8
// jshint ignore: start
var antlr4 = require('antlr4/index');

// This class defines a complete generic visitor for a parse tree produced by PqlParser.

function PqlParserVisitor() {
	antlr4.tree.ParseTreeVisitor.call(this);
	return this;
}

PqlParserVisitor.prototype = Object.create(antlr4.tree.ParseTreeVisitor.prototype);
PqlParserVisitor.prototype.constructor = PqlParserVisitor;

// Visit a parse tree produced by PqlParser#parseTel.
PqlParserVisitor.prototype.visitParseTel = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by PqlParser#expr.
PqlParserVisitor.prototype.visitExpr = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by PqlParser#exprList.
PqlParserVisitor.prototype.visitExprList = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by PqlParser#fn.
PqlParserVisitor.prototype.visitFn = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by PqlParser#fnArgs.
PqlParserVisitor.prototype.visitFnArgs = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by PqlParser#fnArg.
PqlParserVisitor.prototype.visitFnArg = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by PqlParser#taxon.
PqlParserVisitor.prototype.visitTaxon = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by PqlParser#identifierMultipart.
PqlParserVisitor.prototype.visitIdentifierMultipart = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by PqlParser#literalValue.
PqlParserVisitor.prototype.visitLiteralValue = function(ctx) {
  return this.visitChildren(ctx);
};



exports.PqlParserVisitor = PqlParserVisitor;
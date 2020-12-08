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


// Visit a parse tree produced by TelParser#expr.
TelParserVisitor.prototype.visitExpr = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#isNotNull.
TelParserVisitor.prototype.visitIsNotNull = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#isNull.
TelParserVisitor.prototype.visitIsNull = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#taxon.
TelParserVisitor.prototype.visitTaxon = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#identifierMultipart.
TelParserVisitor.prototype.visitIdentifierMultipart = function(ctx) {
  return this.visitChildren(ctx);
};


// Visit a parse tree produced by TelParser#literalValue.
TelParserVisitor.prototype.visitLiteralValue = function(ctx) {
  return this.visitChildren(ctx);
};



exports.TelParserVisitor = TelParserVisitor;
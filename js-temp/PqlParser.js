// Generated from grammar/PqlParser.g4 by ANTLR 4.8
// jshint ignore: start
var antlr4 = require('antlr4/index');
var PqlParserListener = require('./PqlParserListener').PqlParserListener;
var PqlParserVisitor = require('./PqlParserVisitor').PqlParserVisitor;

var grammarFileName = "PqlParser.g4";


var serializedATN = ["\u0003\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964",
    "\u0003:\u00b2\u0004\u0002\t\u0002\u0004\u0003\t\u0003\u0004\u0004\t",
    "\u0004\u0004\u0005\t\u0005\u0004\u0006\t\u0006\u0004\u0007\t\u0007\u0004",
    "\b\t\b\u0004\t\t\t\u0004\n\t\n\u0004\u000b\t\u000b\u0004\f\t\f\u0004",
    "\r\t\r\u0004\u000e\t\u000e\u0004\u000f\t\u000f\u0003\u0002\u0003\u0002",
    "\u0003\u0002\u0003\u0003\u0007\u0003#\n\u0003\f\u0003\u000e\u0003&\u000b",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0004\u0007\u0004+\n\u0004\f\u0004",
    "\u000e\u0004.\u000b\u0004\u0003\u0004\u0003\u0004\u0006\u00042\n\u0004",
    "\r\u0004\u000e\u00043\u0003\u0004\u0007\u00047\n\u0004\f\u0004\u000e",
    "\u0004:\u000b\u0004\u0003\u0004\u0007\u0004=\n\u0004\f\u0004\u000e\u0004",
    "@\u000b\u0004\u0003\u0005\u0003\u0005\u0003\u0006\u0003\u0006\u0003",
    "\u0006\u0005\u0006G\n\u0006\u0003\u0006\u0005\u0006J\n\u0006\u0003\u0006",
    "\u0005\u0006M\n\u0006\u0003\u0007\u0003\u0007\u0003\u0007\u0007\u0007",
    "R\n\u0007\f\u0007\u000e\u0007U\u000b\u0007\u0003\b\u0003\b\u0003\b\u0003",
    "\t\u0003\t\u0003\t\u0003\t\u0003\t\u0007\t_\n\t\f\t\u000e\tb\u000b\t",
    "\u0003\n\u0003\n\u0005\nf\n\n\u0003\u000b\u0003\u000b\u0003\u000b\u0003",
    "\f\u0003\f\u0003\f\u0003\f\u0003\f\u0003\f\u0003\f\u0003\f\u0003\f\u0003",
    "\f\u0003\f\u0003\f\u0003\f\u0007\fx\n\f\f\f\u000e\f{\u000b\f\u0005\f",
    "}\n\f\u0003\f\u0003\f\u0003\f\u0005\f\u0082\n\f\u0003\f\u0003\f\u0003",
    "\f\u0003\f\u0003\f\u0003\f\u0003\f\u0003\f\u0003\f\u0003\f\u0003\f\u0003",
    "\f\u0003\f\u0003\f\u0003\f\u0003\f\u0003\f\u0003\f\u0007\f\u0096\n\f",
    "\f\f\u000e\f\u0099\u000b\f\u0003\r\u0005\r\u009c\n\r\u0003\r\u0003\r",
    "\u0003\r\u0005\r\u00a1\n\r\u0003\r\u0003\r\u0003\r\u0005\r\u00a6\n\r",
    "\u0003\u000e\u0003\u000e\u0003\u000e\u0007\u000e\u00ab\n\u000e\f\u000e",
    "\u000e\u000e\u00ae\u000b\u000e\u0003\u000f\u0003\u000f\u0003\u000f\u0002",
    "\u0003\u0016\u0010\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016",
    "\u0018\u001a\u001c\u0002\u000b\u0004\u0002  \"\"\u0005\u0002\u0016\u0016",
    "\u001a\u001a((\u0005\u0002\u0013\u0013\u0017\u0017\u001c\u001c\u0004",
    "\u0002\u0016\u0016\u001a\u001a\u0004\u0002\u0007\b\u0014\u0015\u0006",
    "\u0002\u0006\u0006\t\n\u000f\u000f$$\u0004\u0002\u0005\u0005\u001f\u001f",
    "\u0004\u0002\u000b\u000b++\u0007\u0002##**..0144\u0002\u00be\u0002\u001e",
    "\u0003\u0002\u0002\u0002\u0004$\u0003\u0002\u0002\u0002\u0006,\u0003",
    "\u0002\u0002\u0002\bA\u0003\u0002\u0002\u0002\nC\u0003\u0002\u0002\u0002",
    "\fN\u0003\u0002\u0002\u0002\u000eV\u0003\u0002\u0002\u0002\u0010Y\u0003",
    "\u0002\u0002\u0002\u0012c\u0003\u0002\u0002\u0002\u0014g\u0003\u0002",
    "\u0002\u0002\u0016\u0081\u0003\u0002\u0002\u0002\u0018\u009b\u0003\u0002",
    "\u0002\u0002\u001a\u00a7\u0003\u0002\u0002\u0002\u001c\u00af\u0003\u0002",
    "\u0002\u0002\u001e\u001f\u0005\u0016\f\u0002\u001f \u0007\u0002\u0002",
    "\u0003 \u0003\u0003\u0002\u0002\u0002!#\u0005\u0006\u0004\u0002\"!\u0003",
    "\u0002\u0002\u0002#&\u0003\u0002\u0002\u0002$\"\u0003\u0002\u0002\u0002",
    "$%\u0003\u0002\u0002\u0002%\'\u0003\u0002\u0002\u0002&$\u0003\u0002",
    "\u0002\u0002\'(\u0007\u0002\u0002\u0003(\u0005\u0003\u0002\u0002\u0002",
    ")+\u0007\u001b\u0002\u0002*)\u0003\u0002\u0002\u0002+.\u0003\u0002\u0002",
    "\u0002,*\u0003\u0002\u0002\u0002,-\u0003\u0002\u0002\u0002-/\u0003\u0002",
    "\u0002\u0002.,\u0003\u0002\u0002\u0002/8\u0005\b\u0005\u000202\u0007",
    "\u001b\u0002\u000210\u0003\u0002\u0002\u000223\u0003\u0002\u0002\u0002",
    "31\u0003\u0002\u0002\u000234\u0003\u0002\u0002\u000245\u0003\u0002\u0002",
    "\u000257\u0005\b\u0005\u000261\u0003\u0002\u0002\u00027:\u0003\u0002",
    "\u0002\u000286\u0003\u0002\u0002\u000289\u0003\u0002\u0002\u00029>\u0003",
    "\u0002\u0002\u0002:8\u0003\u0002\u0002\u0002;=\u0007\u001b\u0002\u0002",
    "<;\u0003\u0002\u0002\u0002=@\u0003\u0002\u0002\u0002><\u0003\u0002\u0002",
    "\u0002>?\u0003\u0002\u0002\u0002?\u0007\u0003\u0002\u0002\u0002@>\u0003",
    "\u0002\u0002\u0002AB\u0005\n\u0006\u0002B\t\u0003\u0002\u0002\u0002",
    "CD\u0007-\u0002\u0002DF\u0005\f\u0007\u0002EG\u0005\u000e\b\u0002FE",
    "\u0003\u0002\u0002\u0002FG\u0003\u0002\u0002\u0002GI\u0003\u0002\u0002",
    "\u0002HJ\u0005\u0010\t\u0002IH\u0003\u0002\u0002\u0002IJ\u0003\u0002",
    "\u0002\u0002JL\u0003\u0002\u0002\u0002KM\u0005\u0014\u000b\u0002LK\u0003",
    "\u0002\u0002\u0002LM\u0003\u0002\u0002\u0002M\u000b\u0003\u0002\u0002",
    "\u0002NS\u0005\u0016\f\u0002OP\u0007\u0011\u0002\u0002PR\u0005\u0016",
    "\f\u0002QO\u0003\u0002\u0002\u0002RU\u0003\u0002\u0002\u0002SQ\u0003",
    "\u0002\u0002\u0002ST\u0003\u0002\u0002\u0002T\r\u0003\u0002\u0002\u0002",
    "US\u0003\u0002\u0002\u0002VW\u0007/\u0002\u0002WX\u0005\u0016\f\u0002",
    "X\u000f\u0003\u0002\u0002\u0002YZ\u0007,\u0002\u0002Z[\u0007!\u0002",
    "\u0002[`\u0005\u0012\n\u0002\\]\u0007\u0011\u0002\u0002]_\u0005\u0012",
    "\n\u0002^\\\u0003\u0002\u0002\u0002_b\u0003\u0002\u0002\u0002`^\u0003",
    "\u0002\u0002\u0002`a\u0003\u0002\u0002\u0002a\u0011\u0003\u0002\u0002",
    "\u0002b`\u0003\u0002\u0002\u0002ce\u0005\u0016\f\u0002df\t\u0002\u0002",
    "\u0002ed\u0003\u0002\u0002\u0002ef\u0003\u0002\u0002\u0002f\u0013\u0003",
    "\u0002\u0002\u0002gh\u0007\'\u0002\u0002hi\u0005\u0016\f\u0002i\u0015",
    "\u0003\u0002\u0002\u0002jk\b\f\u0001\u0002kl\t\u0003\u0002\u0002l\u0082",
    "\u0005\u0016\f\rmn\u0007\u0018\u0002\u0002no\u0005\u0016\f\u0002op\u0007",
    "\u0010\u0002\u0002p\u0082\u0003\u0002\u0002\u0002q\u0082\u0005\u001c",
    "\u000f\u0002rs\u0005\u001a\u000e\u0002s|\u0007\u0018\u0002\u0002ty\u0005",
    "\u0016\f\u0002uv\u0007\u0011\u0002\u0002vx\u0005\u0016\f\u0002wu\u0003",
    "\u0002\u0002\u0002x{\u0003\u0002\u0002\u0002yw\u0003\u0002\u0002\u0002",
    "yz\u0003\u0002\u0002\u0002z}\u0003\u0002\u0002\u0002{y\u0003\u0002\u0002",
    "\u0002|t\u0003\u0002\u0002\u0002|}\u0003\u0002\u0002\u0002}~\u0003\u0002",
    "\u0002\u0002~\u007f\u0007\u0010\u0002\u0002\u007f\u0082\u0003\u0002",
    "\u0002\u0002\u0080\u0082\u0005\u0018\r\u0002\u0081j\u0003\u0002\u0002",
    "\u0002\u0081m\u0003\u0002\u0002\u0002\u0081q\u0003\u0002\u0002\u0002",
    "\u0081r\u0003\u0002\u0002\u0002\u0081\u0080\u0003\u0002\u0002\u0002",
    "\u0082\u0097\u0003\u0002\u0002\u0002\u0083\u0084\f\f\u0002\u0002\u0084",
    "\u0085\t\u0004\u0002\u0002\u0085\u0096\u0005\u0016\f\r\u0086\u0087\f",
    "\u000b\u0002\u0002\u0087\u0088\t\u0005\u0002\u0002\u0088\u0096\u0005",
    "\u0016\f\f\u0089\u008a\f\n\u0002\u0002\u008a\u008b\t\u0006\u0002\u0002",
    "\u008b\u0096\u0005\u0016\f\u000b\u008c\u008d\f\t\u0002\u0002\u008d\u008e",
    "\t\u0007\u0002\u0002\u008e\u0096\u0005\u0016\f\n\u008f\u0090\f\b\u0002",
    "\u0002\u0090\u0091\t\b\u0002\u0002\u0091\u0096\u0005\u0016\f\t\u0092",
    "\u0093\f\u0007\u0002\u0002\u0093\u0094\t\t\u0002\u0002\u0094\u0096\u0005",
    "\u0016\f\b\u0095\u0083\u0003\u0002\u0002\u0002\u0095\u0086\u0003\u0002",
    "\u0002\u0002\u0095\u0089\u0003\u0002\u0002\u0002\u0095\u008c\u0003\u0002",
    "\u0002\u0002\u0095\u008f\u0003\u0002\u0002\u0002\u0095\u0092\u0003\u0002",
    "\u0002\u0002\u0096\u0099\u0003\u0002\u0002\u0002\u0097\u0095\u0003\u0002",
    "\u0002\u0002\u0097\u0098\u0003\u0002\u0002\u0002\u0098\u0017\u0003\u0002",
    "\u0002\u0002\u0099\u0097\u0003\u0002\u0002\u0002\u009a\u009c\u0007\u0004",
    "\u0002\u0002\u009b\u009a\u0003\u0002\u0002\u0002\u009b\u009c\u0003\u0002",
    "\u0002\u0002\u009c\u00a0\u0003\u0002\u0002\u0002\u009d\u009e\u0005\u001a",
    "\u000e\u0002\u009e\u009f\u0007\u0019\u0002\u0002\u009f\u00a1\u0003\u0002",
    "\u0002\u0002\u00a0\u009d\u0003\u0002\u0002\u0002\u00a0\u00a1\u0003\u0002",
    "\u0002\u0002\u00a1\u00a2\u0003\u0002\u0002\u0002\u00a2\u00a5\u0005\u001a",
    "\u000e\u0002\u00a3\u00a4\u0007\u0003\u0002\u0002\u00a4\u00a6\u0005\u001a",
    "\u000e\u0002\u00a5\u00a3\u0003\u0002\u0002\u0002\u00a5\u00a6\u0003\u0002",
    "\u0002\u0002\u00a6\u0019\u0003\u0002\u0002\u0002\u00a7\u00ac\u0007:",
    "\u0002\u0002\u00a8\u00a9\u0007\u0012\u0002\u0002\u00a9\u00ab\u0007:",
    "\u0002\u0002\u00aa\u00a8\u0003\u0002\u0002\u0002\u00ab\u00ae\u0003\u0002",
    "\u0002\u0002\u00ac\u00aa\u0003\u0002\u0002\u0002\u00ac\u00ad\u0003\u0002",
    "\u0002\u0002\u00ad\u001b\u0003\u0002\u0002\u0002\u00ae\u00ac\u0003\u0002",
    "\u0002\u0002\u00af\u00b0\t\n\u0002\u0002\u00b0\u001d\u0003\u0002\u0002",
    "\u0002\u0016$,38>FILS`ey|\u0081\u0095\u0097\u009b\u00a0\u00a5\u00ac"].join("");


var atn = new antlr4.atn.ATNDeserializer().deserialize(serializedATN);

var decisionsToDFA = atn.decisionToState.map( function(ds, index) { return new antlr4.dfa.DFA(ds, index); });

var sharedContextCache = new antlr4.PredictionContextCache();

var literalNames = [ null, "':'", "'?'", "'&&'", "'=='", "'>='", "'<='", 
                     "'!='", "'<>'", "'||'", "'<<'", "'>>'", "'&'", "'='", 
                     "')'", "','", "'.'", "'/'", "'>'", "'<'", "'-'", "'%'", 
                     "'('", "'|'", "'+'", "';'", "'*'", "'~'", "'_'" ];

var symbolicNames = [ null, "TAXON_TAG_DELIMITER", "TAXON_OPTIONAL_OPERATOR", 
                      "AND", "EQ", "GT_EQ", "LT_EQ", "NOT_EQ1", "NOT_EQ2", 
                      "OR", "SHIFT_LEFT", "SHIFT_RIGHT", "AMP", "ASSIGN", 
                      "CLOSE_PAREN", "COMMA", "DOT", "FORWARD_SLASH", "GT", 
                      "LT", "MINUS", "MOD", "OPEN_PAREN", "PIPE", "PLUS", 
                      "SCOL", "STAR", "TILDE", "UNDER", "K_AND", "K_ASC", 
                      "K_BY", "K_DESC", "K_FALSE", "K_IS", "K_ISNULL", "K_LIKE", 
                      "K_LIMIT", "K_NOT", "K_NOTNULL", "K_NULL", "K_OR", 
                      "K_ORDER", "K_SELECT", "K_TRUE", "K_WHERE", "NUMERIC_LITERAL", 
                      "DOUBLE_QUOTED_STRING", "DOUBLE_QUOTED_STRING_TEL", 
                      "DOUBLE_QUOTED_STRING_SQL", "SINGLE_QUOTED_STRING", 
                      "SINGLE_QUOTED_STRING_TEL", "SINGLE_QUOTED_STRING_SQL", 
                      "SINGLE_LINE_COMMENT", "MULTILINE_COMMENT", "SPACES", 
                      "WORD" ];

var ruleNames =  [ "parseTel", "parsePql", "sqlStmtList", "sqlStmt", "selectStmt", 
                   "columns", "whereClause", "orderByClause", "orderExpr", 
                   "limitClause", "expr", "taxon", "identifierMultipart", 
                   "literalValue" ];

function PqlParser (input) {
	antlr4.Parser.call(this, input);
    this._interp = new antlr4.atn.ParserATNSimulator(this, atn, decisionsToDFA, sharedContextCache);
    this.ruleNames = ruleNames;
    this.literalNames = literalNames;
    this.symbolicNames = symbolicNames;
    return this;
}

PqlParser.prototype = Object.create(antlr4.Parser.prototype);
PqlParser.prototype.constructor = PqlParser;

Object.defineProperty(PqlParser.prototype, "atn", {
	get : function() {
		return atn;
	}
});

PqlParser.EOF = antlr4.Token.EOF;
PqlParser.TAXON_TAG_DELIMITER = 1;
PqlParser.TAXON_OPTIONAL_OPERATOR = 2;
PqlParser.AND = 3;
PqlParser.EQ = 4;
PqlParser.GT_EQ = 5;
PqlParser.LT_EQ = 6;
PqlParser.NOT_EQ1 = 7;
PqlParser.NOT_EQ2 = 8;
PqlParser.OR = 9;
PqlParser.SHIFT_LEFT = 10;
PqlParser.SHIFT_RIGHT = 11;
PqlParser.AMP = 12;
PqlParser.ASSIGN = 13;
PqlParser.CLOSE_PAREN = 14;
PqlParser.COMMA = 15;
PqlParser.DOT = 16;
PqlParser.FORWARD_SLASH = 17;
PqlParser.GT = 18;
PqlParser.LT = 19;
PqlParser.MINUS = 20;
PqlParser.MOD = 21;
PqlParser.OPEN_PAREN = 22;
PqlParser.PIPE = 23;
PqlParser.PLUS = 24;
PqlParser.SCOL = 25;
PqlParser.STAR = 26;
PqlParser.TILDE = 27;
PqlParser.UNDER = 28;
PqlParser.K_AND = 29;
PqlParser.K_ASC = 30;
PqlParser.K_BY = 31;
PqlParser.K_DESC = 32;
PqlParser.K_FALSE = 33;
PqlParser.K_IS = 34;
PqlParser.K_ISNULL = 35;
PqlParser.K_LIKE = 36;
PqlParser.K_LIMIT = 37;
PqlParser.K_NOT = 38;
PqlParser.K_NOTNULL = 39;
PqlParser.K_NULL = 40;
PqlParser.K_OR = 41;
PqlParser.K_ORDER = 42;
PqlParser.K_SELECT = 43;
PqlParser.K_TRUE = 44;
PqlParser.K_WHERE = 45;
PqlParser.NUMERIC_LITERAL = 46;
PqlParser.DOUBLE_QUOTED_STRING = 47;
PqlParser.DOUBLE_QUOTED_STRING_TEL = 48;
PqlParser.DOUBLE_QUOTED_STRING_SQL = 49;
PqlParser.SINGLE_QUOTED_STRING = 50;
PqlParser.SINGLE_QUOTED_STRING_TEL = 51;
PqlParser.SINGLE_QUOTED_STRING_SQL = 52;
PqlParser.SINGLE_LINE_COMMENT = 53;
PqlParser.MULTILINE_COMMENT = 54;
PqlParser.SPACES = 55;
PqlParser.WORD = 56;

PqlParser.RULE_parseTel = 0;
PqlParser.RULE_parsePql = 1;
PqlParser.RULE_sqlStmtList = 2;
PqlParser.RULE_sqlStmt = 3;
PqlParser.RULE_selectStmt = 4;
PqlParser.RULE_columns = 5;
PqlParser.RULE_whereClause = 6;
PqlParser.RULE_orderByClause = 7;
PqlParser.RULE_orderExpr = 8;
PqlParser.RULE_limitClause = 9;
PqlParser.RULE_expr = 10;
PqlParser.RULE_taxon = 11;
PqlParser.RULE_identifierMultipart = 12;
PqlParser.RULE_literalValue = 13;


function ParseTelContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = PqlParser.RULE_parseTel;
    return this;
}

ParseTelContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
ParseTelContext.prototype.constructor = ParseTelContext;

ParseTelContext.prototype.expr = function() {
    return this.getTypedRuleContext(ExprContext,0);
};

ParseTelContext.prototype.EOF = function() {
    return this.getToken(PqlParser.EOF, 0);
};

ParseTelContext.prototype.enterRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.enterParseTel(this);
	}
};

ParseTelContext.prototype.exitRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.exitParseTel(this);
	}
};

ParseTelContext.prototype.accept = function(visitor) {
    if ( visitor instanceof PqlParserVisitor ) {
        return visitor.visitParseTel(this);
    } else {
        return visitor.visitChildren(this);
    }
};




PqlParser.ParseTelContext = ParseTelContext;

PqlParser.prototype.parseTel = function() {

    var localctx = new ParseTelContext(this, this._ctx, this.state);
    this.enterRule(localctx, 0, PqlParser.RULE_parseTel);
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 28;
        this.expr(0);
        this.state = 29;
        this.match(PqlParser.EOF);
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};


function ParsePqlContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = PqlParser.RULE_parsePql;
    return this;
}

ParsePqlContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
ParsePqlContext.prototype.constructor = ParsePqlContext;

ParsePqlContext.prototype.EOF = function() {
    return this.getToken(PqlParser.EOF, 0);
};

ParsePqlContext.prototype.sqlStmtList = function(i) {
    if(i===undefined) {
        i = null;
    }
    if(i===null) {
        return this.getTypedRuleContexts(SqlStmtListContext);
    } else {
        return this.getTypedRuleContext(SqlStmtListContext,i);
    }
};

ParsePqlContext.prototype.enterRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.enterParsePql(this);
	}
};

ParsePqlContext.prototype.exitRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.exitParsePql(this);
	}
};

ParsePqlContext.prototype.accept = function(visitor) {
    if ( visitor instanceof PqlParserVisitor ) {
        return visitor.visitParsePql(this);
    } else {
        return visitor.visitChildren(this);
    }
};




PqlParser.ParsePqlContext = ParsePqlContext;

PqlParser.prototype.parsePql = function() {

    var localctx = new ParsePqlContext(this, this._ctx, this.state);
    this.enterRule(localctx, 2, PqlParser.RULE_parsePql);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 34;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        while(_la===PqlParser.SCOL || _la===PqlParser.K_SELECT) {
            this.state = 31;
            this.sqlStmtList();
            this.state = 36;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
        }
        this.state = 37;
        this.match(PqlParser.EOF);
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};


function SqlStmtListContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = PqlParser.RULE_sqlStmtList;
    return this;
}

SqlStmtListContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
SqlStmtListContext.prototype.constructor = SqlStmtListContext;

SqlStmtListContext.prototype.sqlStmt = function(i) {
    if(i===undefined) {
        i = null;
    }
    if(i===null) {
        return this.getTypedRuleContexts(SqlStmtContext);
    } else {
        return this.getTypedRuleContext(SqlStmtContext,i);
    }
};

SqlStmtListContext.prototype.SCOL = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(PqlParser.SCOL);
    } else {
        return this.getToken(PqlParser.SCOL, i);
    }
};


SqlStmtListContext.prototype.enterRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.enterSqlStmtList(this);
	}
};

SqlStmtListContext.prototype.exitRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.exitSqlStmtList(this);
	}
};

SqlStmtListContext.prototype.accept = function(visitor) {
    if ( visitor instanceof PqlParserVisitor ) {
        return visitor.visitSqlStmtList(this);
    } else {
        return visitor.visitChildren(this);
    }
};




PqlParser.SqlStmtListContext = SqlStmtListContext;

PqlParser.prototype.sqlStmtList = function() {

    var localctx = new SqlStmtListContext(this, this._ctx, this.state);
    this.enterRule(localctx, 4, PqlParser.RULE_sqlStmtList);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 42;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        while(_la===PqlParser.SCOL) {
            this.state = 39;
            this.match(PqlParser.SCOL);
            this.state = 44;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
        }
        this.state = 45;
        this.sqlStmt();
        this.state = 54;
        this._errHandler.sync(this);
        var _alt = this._interp.adaptivePredict(this._input,3,this._ctx)
        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
            if(_alt===1) {
                this.state = 47; 
                this._errHandler.sync(this);
                _la = this._input.LA(1);
                do {
                    this.state = 46;
                    this.match(PqlParser.SCOL);
                    this.state = 49; 
                    this._errHandler.sync(this);
                    _la = this._input.LA(1);
                } while(_la===PqlParser.SCOL);
                this.state = 51;
                this.sqlStmt(); 
            }
            this.state = 56;
            this._errHandler.sync(this);
            _alt = this._interp.adaptivePredict(this._input,3,this._ctx);
        }

        this.state = 60;
        this._errHandler.sync(this);
        var _alt = this._interp.adaptivePredict(this._input,4,this._ctx)
        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
            if(_alt===1) {
                this.state = 57;
                this.match(PqlParser.SCOL); 
            }
            this.state = 62;
            this._errHandler.sync(this);
            _alt = this._interp.adaptivePredict(this._input,4,this._ctx);
        }

    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};


function SqlStmtContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = PqlParser.RULE_sqlStmt;
    return this;
}

SqlStmtContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
SqlStmtContext.prototype.constructor = SqlStmtContext;

SqlStmtContext.prototype.selectStmt = function() {
    return this.getTypedRuleContext(SelectStmtContext,0);
};

SqlStmtContext.prototype.enterRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.enterSqlStmt(this);
	}
};

SqlStmtContext.prototype.exitRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.exitSqlStmt(this);
	}
};

SqlStmtContext.prototype.accept = function(visitor) {
    if ( visitor instanceof PqlParserVisitor ) {
        return visitor.visitSqlStmt(this);
    } else {
        return visitor.visitChildren(this);
    }
};




PqlParser.SqlStmtContext = SqlStmtContext;

PqlParser.prototype.sqlStmt = function() {

    var localctx = new SqlStmtContext(this, this._ctx, this.state);
    this.enterRule(localctx, 6, PqlParser.RULE_sqlStmt);
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 63;
        this.selectStmt();
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};


function SelectStmtContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = PqlParser.RULE_selectStmt;
    return this;
}

SelectStmtContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
SelectStmtContext.prototype.constructor = SelectStmtContext;

SelectStmtContext.prototype.K_SELECT = function() {
    return this.getToken(PqlParser.K_SELECT, 0);
};

SelectStmtContext.prototype.columns = function() {
    return this.getTypedRuleContext(ColumnsContext,0);
};

SelectStmtContext.prototype.whereClause = function() {
    return this.getTypedRuleContext(WhereClauseContext,0);
};

SelectStmtContext.prototype.orderByClause = function() {
    return this.getTypedRuleContext(OrderByClauseContext,0);
};

SelectStmtContext.prototype.limitClause = function() {
    return this.getTypedRuleContext(LimitClauseContext,0);
};

SelectStmtContext.prototype.enterRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.enterSelectStmt(this);
	}
};

SelectStmtContext.prototype.exitRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.exitSelectStmt(this);
	}
};

SelectStmtContext.prototype.accept = function(visitor) {
    if ( visitor instanceof PqlParserVisitor ) {
        return visitor.visitSelectStmt(this);
    } else {
        return visitor.visitChildren(this);
    }
};




PqlParser.SelectStmtContext = SelectStmtContext;

PqlParser.prototype.selectStmt = function() {

    var localctx = new SelectStmtContext(this, this._ctx, this.state);
    this.enterRule(localctx, 8, PqlParser.RULE_selectStmt);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 65;
        this.match(PqlParser.K_SELECT);
        this.state = 66;
        this.columns();
        this.state = 68;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        if(_la===PqlParser.K_WHERE) {
            this.state = 67;
            this.whereClause();
        }

        this.state = 71;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        if(_la===PqlParser.K_ORDER) {
            this.state = 70;
            this.orderByClause();
        }

        this.state = 74;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        if(_la===PqlParser.K_LIMIT) {
            this.state = 73;
            this.limitClause();
        }

    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};


function ColumnsContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = PqlParser.RULE_columns;
    return this;
}

ColumnsContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
ColumnsContext.prototype.constructor = ColumnsContext;

ColumnsContext.prototype.expr = function(i) {
    if(i===undefined) {
        i = null;
    }
    if(i===null) {
        return this.getTypedRuleContexts(ExprContext);
    } else {
        return this.getTypedRuleContext(ExprContext,i);
    }
};

ColumnsContext.prototype.COMMA = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(PqlParser.COMMA);
    } else {
        return this.getToken(PqlParser.COMMA, i);
    }
};


ColumnsContext.prototype.enterRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.enterColumns(this);
	}
};

ColumnsContext.prototype.exitRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.exitColumns(this);
	}
};

ColumnsContext.prototype.accept = function(visitor) {
    if ( visitor instanceof PqlParserVisitor ) {
        return visitor.visitColumns(this);
    } else {
        return visitor.visitChildren(this);
    }
};




PqlParser.ColumnsContext = ColumnsContext;

PqlParser.prototype.columns = function() {

    var localctx = new ColumnsContext(this, this._ctx, this.state);
    this.enterRule(localctx, 10, PqlParser.RULE_columns);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 76;
        this.expr(0);
        this.state = 81;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        while(_la===PqlParser.COMMA) {
            this.state = 77;
            this.match(PqlParser.COMMA);
            this.state = 78;
            this.expr(0);
            this.state = 83;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
        }
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};


function WhereClauseContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = PqlParser.RULE_whereClause;
    return this;
}

WhereClauseContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
WhereClauseContext.prototype.constructor = WhereClauseContext;

WhereClauseContext.prototype.K_WHERE = function() {
    return this.getToken(PqlParser.K_WHERE, 0);
};

WhereClauseContext.prototype.expr = function() {
    return this.getTypedRuleContext(ExprContext,0);
};

WhereClauseContext.prototype.enterRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.enterWhereClause(this);
	}
};

WhereClauseContext.prototype.exitRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.exitWhereClause(this);
	}
};

WhereClauseContext.prototype.accept = function(visitor) {
    if ( visitor instanceof PqlParserVisitor ) {
        return visitor.visitWhereClause(this);
    } else {
        return visitor.visitChildren(this);
    }
};




PqlParser.WhereClauseContext = WhereClauseContext;

PqlParser.prototype.whereClause = function() {

    var localctx = new WhereClauseContext(this, this._ctx, this.state);
    this.enterRule(localctx, 12, PqlParser.RULE_whereClause);
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 84;
        this.match(PqlParser.K_WHERE);
        this.state = 85;
        this.expr(0);
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};


function OrderByClauseContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = PqlParser.RULE_orderByClause;
    return this;
}

OrderByClauseContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
OrderByClauseContext.prototype.constructor = OrderByClauseContext;

OrderByClauseContext.prototype.K_ORDER = function() {
    return this.getToken(PqlParser.K_ORDER, 0);
};

OrderByClauseContext.prototype.K_BY = function() {
    return this.getToken(PqlParser.K_BY, 0);
};

OrderByClauseContext.prototype.orderExpr = function(i) {
    if(i===undefined) {
        i = null;
    }
    if(i===null) {
        return this.getTypedRuleContexts(OrderExprContext);
    } else {
        return this.getTypedRuleContext(OrderExprContext,i);
    }
};

OrderByClauseContext.prototype.COMMA = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(PqlParser.COMMA);
    } else {
        return this.getToken(PqlParser.COMMA, i);
    }
};


OrderByClauseContext.prototype.enterRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.enterOrderByClause(this);
	}
};

OrderByClauseContext.prototype.exitRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.exitOrderByClause(this);
	}
};

OrderByClauseContext.prototype.accept = function(visitor) {
    if ( visitor instanceof PqlParserVisitor ) {
        return visitor.visitOrderByClause(this);
    } else {
        return visitor.visitChildren(this);
    }
};




PqlParser.OrderByClauseContext = OrderByClauseContext;

PqlParser.prototype.orderByClause = function() {

    var localctx = new OrderByClauseContext(this, this._ctx, this.state);
    this.enterRule(localctx, 14, PqlParser.RULE_orderByClause);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 87;
        this.match(PqlParser.K_ORDER);
        this.state = 88;
        this.match(PqlParser.K_BY);
        this.state = 89;
        this.orderExpr();
        this.state = 94;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        while(_la===PqlParser.COMMA) {
            this.state = 90;
            this.match(PqlParser.COMMA);
            this.state = 91;
            this.orderExpr();
            this.state = 96;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
        }
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};


function OrderExprContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = PqlParser.RULE_orderExpr;
    return this;
}

OrderExprContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
OrderExprContext.prototype.constructor = OrderExprContext;

OrderExprContext.prototype.expr = function() {
    return this.getTypedRuleContext(ExprContext,0);
};

OrderExprContext.prototype.K_ASC = function() {
    return this.getToken(PqlParser.K_ASC, 0);
};

OrderExprContext.prototype.K_DESC = function() {
    return this.getToken(PqlParser.K_DESC, 0);
};

OrderExprContext.prototype.enterRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.enterOrderExpr(this);
	}
};

OrderExprContext.prototype.exitRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.exitOrderExpr(this);
	}
};

OrderExprContext.prototype.accept = function(visitor) {
    if ( visitor instanceof PqlParserVisitor ) {
        return visitor.visitOrderExpr(this);
    } else {
        return visitor.visitChildren(this);
    }
};




PqlParser.OrderExprContext = OrderExprContext;

PqlParser.prototype.orderExpr = function() {

    var localctx = new OrderExprContext(this, this._ctx, this.state);
    this.enterRule(localctx, 16, PqlParser.RULE_orderExpr);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 97;
        this.expr(0);
        this.state = 99;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        if(_la===PqlParser.K_ASC || _la===PqlParser.K_DESC) {
            this.state = 98;
            _la = this._input.LA(1);
            if(!(_la===PqlParser.K_ASC || _la===PqlParser.K_DESC)) {
            this._errHandler.recoverInline(this);
            }
            else {
            	this._errHandler.reportMatch(this);
                this.consume();
            }
        }

    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};


function LimitClauseContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = PqlParser.RULE_limitClause;
    this.limit = null; // ExprContext
    return this;
}

LimitClauseContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
LimitClauseContext.prototype.constructor = LimitClauseContext;

LimitClauseContext.prototype.K_LIMIT = function() {
    return this.getToken(PqlParser.K_LIMIT, 0);
};

LimitClauseContext.prototype.expr = function() {
    return this.getTypedRuleContext(ExprContext,0);
};

LimitClauseContext.prototype.enterRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.enterLimitClause(this);
	}
};

LimitClauseContext.prototype.exitRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.exitLimitClause(this);
	}
};

LimitClauseContext.prototype.accept = function(visitor) {
    if ( visitor instanceof PqlParserVisitor ) {
        return visitor.visitLimitClause(this);
    } else {
        return visitor.visitChildren(this);
    }
};




PqlParser.LimitClauseContext = LimitClauseContext;

PqlParser.prototype.limitClause = function() {

    var localctx = new LimitClauseContext(this, this._ctx, this.state);
    this.enterRule(localctx, 18, PqlParser.RULE_limitClause);
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 101;
        this.match(PqlParser.K_LIMIT);
        this.state = 102;
        localctx.limit = this.expr(0);
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};


function ExprContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = PqlParser.RULE_expr;
    this.left = null; // ExprContext
    this.unary_operator = null; // Token
    this.right = null; // ExprContext
    this.inner = null; // ExprContext
    this.function_name = null; // IdentifierMultipartContext
    this.operator = null; // Token
    return this;
}

ExprContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
ExprContext.prototype.constructor = ExprContext;

ExprContext.prototype.expr = function(i) {
    if(i===undefined) {
        i = null;
    }
    if(i===null) {
        return this.getTypedRuleContexts(ExprContext);
    } else {
        return this.getTypedRuleContext(ExprContext,i);
    }
};

ExprContext.prototype.MINUS = function() {
    return this.getToken(PqlParser.MINUS, 0);
};

ExprContext.prototype.PLUS = function() {
    return this.getToken(PqlParser.PLUS, 0);
};

ExprContext.prototype.K_NOT = function() {
    return this.getToken(PqlParser.K_NOT, 0);
};

ExprContext.prototype.OPEN_PAREN = function() {
    return this.getToken(PqlParser.OPEN_PAREN, 0);
};

ExprContext.prototype.CLOSE_PAREN = function() {
    return this.getToken(PqlParser.CLOSE_PAREN, 0);
};

ExprContext.prototype.literalValue = function() {
    return this.getTypedRuleContext(LiteralValueContext,0);
};

ExprContext.prototype.identifierMultipart = function() {
    return this.getTypedRuleContext(IdentifierMultipartContext,0);
};

ExprContext.prototype.COMMA = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(PqlParser.COMMA);
    } else {
        return this.getToken(PqlParser.COMMA, i);
    }
};


ExprContext.prototype.taxon = function() {
    return this.getTypedRuleContext(TaxonContext,0);
};

ExprContext.prototype.STAR = function() {
    return this.getToken(PqlParser.STAR, 0);
};

ExprContext.prototype.FORWARD_SLASH = function() {
    return this.getToken(PqlParser.FORWARD_SLASH, 0);
};

ExprContext.prototype.MOD = function() {
    return this.getToken(PqlParser.MOD, 0);
};

ExprContext.prototype.LT = function() {
    return this.getToken(PqlParser.LT, 0);
};

ExprContext.prototype.LT_EQ = function() {
    return this.getToken(PqlParser.LT_EQ, 0);
};

ExprContext.prototype.GT = function() {
    return this.getToken(PqlParser.GT, 0);
};

ExprContext.prototype.GT_EQ = function() {
    return this.getToken(PqlParser.GT_EQ, 0);
};

ExprContext.prototype.ASSIGN = function() {
    return this.getToken(PqlParser.ASSIGN, 0);
};

ExprContext.prototype.EQ = function() {
    return this.getToken(PqlParser.EQ, 0);
};

ExprContext.prototype.NOT_EQ1 = function() {
    return this.getToken(PqlParser.NOT_EQ1, 0);
};

ExprContext.prototype.NOT_EQ2 = function() {
    return this.getToken(PqlParser.NOT_EQ2, 0);
};

ExprContext.prototype.K_IS = function() {
    return this.getToken(PqlParser.K_IS, 0);
};

ExprContext.prototype.K_AND = function() {
    return this.getToken(PqlParser.K_AND, 0);
};

ExprContext.prototype.AND = function() {
    return this.getToken(PqlParser.AND, 0);
};

ExprContext.prototype.K_OR = function() {
    return this.getToken(PqlParser.K_OR, 0);
};

ExprContext.prototype.OR = function() {
    return this.getToken(PqlParser.OR, 0);
};

ExprContext.prototype.enterRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.enterExpr(this);
	}
};

ExprContext.prototype.exitRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.exitExpr(this);
	}
};

ExprContext.prototype.accept = function(visitor) {
    if ( visitor instanceof PqlParserVisitor ) {
        return visitor.visitExpr(this);
    } else {
        return visitor.visitChildren(this);
    }
};



PqlParser.prototype.expr = function(_p) {
	if(_p===undefined) {
	    _p = 0;
	}
    var _parentctx = this._ctx;
    var _parentState = this.state;
    var localctx = new ExprContext(this, this._ctx, _parentState);
    var _prevctx = localctx;
    var _startState = 20;
    this.enterRecursionRule(localctx, 20, PqlParser.RULE_expr, _p);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 127;
        this._errHandler.sync(this);
        var la_ = this._interp.adaptivePredict(this._input,13,this._ctx);
        switch(la_) {
        case 1:
            this.state = 105;
            localctx.unary_operator = this._input.LT(1);
            _la = this._input.LA(1);
            if(!(((((_la - 20)) & ~0x1f) == 0 && ((1 << (_la - 20)) & ((1 << (PqlParser.MINUS - 20)) | (1 << (PqlParser.PLUS - 20)) | (1 << (PqlParser.K_NOT - 20)))) !== 0))) {
                localctx.unary_operator = this._errHandler.recoverInline(this);
            }
            else {
            	this._errHandler.reportMatch(this);
                this.consume();
            }
            this.state = 106;
            localctx.right = this.expr(11);
            break;

        case 2:
            this.state = 107;
            this.match(PqlParser.OPEN_PAREN);
            this.state = 108;
            localctx.inner = this.expr(0);
            this.state = 109;
            this.match(PqlParser.CLOSE_PAREN);
            break;

        case 3:
            this.state = 111;
            this.literalValue();
            break;

        case 4:
            this.state = 112;
            localctx.function_name = this.identifierMultipart();
            this.state = 113;
            this.match(PqlParser.OPEN_PAREN);
            this.state = 122;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
            if((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << PqlParser.TAXON_OPTIONAL_OPERATOR) | (1 << PqlParser.MINUS) | (1 << PqlParser.OPEN_PAREN) | (1 << PqlParser.PLUS))) !== 0) || ((((_la - 33)) & ~0x1f) == 0 && ((1 << (_la - 33)) & ((1 << (PqlParser.K_FALSE - 33)) | (1 << (PqlParser.K_NOT - 33)) | (1 << (PqlParser.K_NULL - 33)) | (1 << (PqlParser.K_TRUE - 33)) | (1 << (PqlParser.NUMERIC_LITERAL - 33)) | (1 << (PqlParser.DOUBLE_QUOTED_STRING - 33)) | (1 << (PqlParser.SINGLE_QUOTED_STRING - 33)) | (1 << (PqlParser.WORD - 33)))) !== 0)) {
                this.state = 114;
                this.expr(0);
                this.state = 119;
                this._errHandler.sync(this);
                _la = this._input.LA(1);
                while(_la===PqlParser.COMMA) {
                    this.state = 115;
                    this.match(PqlParser.COMMA);
                    this.state = 116;
                    this.expr(0);
                    this.state = 121;
                    this._errHandler.sync(this);
                    _la = this._input.LA(1);
                }
            }

            this.state = 124;
            this.match(PqlParser.CLOSE_PAREN);
            break;

        case 5:
            this.state = 126;
            this.taxon();
            break;

        }
        this._ctx.stop = this._input.LT(-1);
        this.state = 149;
        this._errHandler.sync(this);
        var _alt = this._interp.adaptivePredict(this._input,15,this._ctx)
        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
            if(_alt===1) {
                if(this._parseListeners!==null) {
                    this.triggerExitRuleEvent();
                }
                _prevctx = localctx;
                this.state = 147;
                this._errHandler.sync(this);
                var la_ = this._interp.adaptivePredict(this._input,14,this._ctx);
                switch(la_) {
                case 1:
                    localctx = new ExprContext(this, _parentctx, _parentState);
                    localctx.left = _prevctx;
                    this.pushNewRecursionContext(localctx, _startState, PqlParser.RULE_expr);
                    this.state = 129;
                    if (!( this.precpred(this._ctx, 10))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 10)");
                    }
                    this.state = 130;
                    localctx.operator = this._input.LT(1);
                    _la = this._input.LA(1);
                    if(!((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << PqlParser.FORWARD_SLASH) | (1 << PqlParser.MOD) | (1 << PqlParser.STAR))) !== 0))) {
                        localctx.operator = this._errHandler.recoverInline(this);
                    }
                    else {
                    	this._errHandler.reportMatch(this);
                        this.consume();
                    }
                    this.state = 131;
                    localctx.right = this.expr(11);
                    break;

                case 2:
                    localctx = new ExprContext(this, _parentctx, _parentState);
                    localctx.left = _prevctx;
                    this.pushNewRecursionContext(localctx, _startState, PqlParser.RULE_expr);
                    this.state = 132;
                    if (!( this.precpred(this._ctx, 9))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 9)");
                    }
                    this.state = 133;
                    localctx.operator = this._input.LT(1);
                    _la = this._input.LA(1);
                    if(!(_la===PqlParser.MINUS || _la===PqlParser.PLUS)) {
                        localctx.operator = this._errHandler.recoverInline(this);
                    }
                    else {
                    	this._errHandler.reportMatch(this);
                        this.consume();
                    }
                    this.state = 134;
                    localctx.right = this.expr(10);
                    break;

                case 3:
                    localctx = new ExprContext(this, _parentctx, _parentState);
                    localctx.left = _prevctx;
                    this.pushNewRecursionContext(localctx, _startState, PqlParser.RULE_expr);
                    this.state = 135;
                    if (!( this.precpred(this._ctx, 8))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 8)");
                    }
                    this.state = 136;
                    localctx.operator = this._input.LT(1);
                    _la = this._input.LA(1);
                    if(!((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << PqlParser.GT_EQ) | (1 << PqlParser.LT_EQ) | (1 << PqlParser.GT) | (1 << PqlParser.LT))) !== 0))) {
                        localctx.operator = this._errHandler.recoverInline(this);
                    }
                    else {
                    	this._errHandler.reportMatch(this);
                        this.consume();
                    }
                    this.state = 137;
                    localctx.right = this.expr(9);
                    break;

                case 4:
                    localctx = new ExprContext(this, _parentctx, _parentState);
                    localctx.left = _prevctx;
                    this.pushNewRecursionContext(localctx, _startState, PqlParser.RULE_expr);
                    this.state = 138;
                    if (!( this.precpred(this._ctx, 7))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 7)");
                    }
                    this.state = 139;
                    localctx.operator = this._input.LT(1);
                    _la = this._input.LA(1);
                    if(!(((((_la - 4)) & ~0x1f) == 0 && ((1 << (_la - 4)) & ((1 << (PqlParser.EQ - 4)) | (1 << (PqlParser.NOT_EQ1 - 4)) | (1 << (PqlParser.NOT_EQ2 - 4)) | (1 << (PqlParser.ASSIGN - 4)) | (1 << (PqlParser.K_IS - 4)))) !== 0))) {
                        localctx.operator = this._errHandler.recoverInline(this);
                    }
                    else {
                    	this._errHandler.reportMatch(this);
                        this.consume();
                    }
                    this.state = 140;
                    localctx.right = this.expr(8);
                    break;

                case 5:
                    localctx = new ExprContext(this, _parentctx, _parentState);
                    localctx.left = _prevctx;
                    this.pushNewRecursionContext(localctx, _startState, PqlParser.RULE_expr);
                    this.state = 141;
                    if (!( this.precpred(this._ctx, 6))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 6)");
                    }
                    this.state = 142;
                    localctx.operator = this._input.LT(1);
                    _la = this._input.LA(1);
                    if(!(_la===PqlParser.AND || _la===PqlParser.K_AND)) {
                        localctx.operator = this._errHandler.recoverInline(this);
                    }
                    else {
                    	this._errHandler.reportMatch(this);
                        this.consume();
                    }
                    this.state = 143;
                    localctx.right = this.expr(7);
                    break;

                case 6:
                    localctx = new ExprContext(this, _parentctx, _parentState);
                    localctx.left = _prevctx;
                    this.pushNewRecursionContext(localctx, _startState, PqlParser.RULE_expr);
                    this.state = 144;
                    if (!( this.precpred(this._ctx, 5))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 5)");
                    }
                    this.state = 145;
                    localctx.operator = this._input.LT(1);
                    _la = this._input.LA(1);
                    if(!(_la===PqlParser.OR || _la===PqlParser.K_OR)) {
                        localctx.operator = this._errHandler.recoverInline(this);
                    }
                    else {
                    	this._errHandler.reportMatch(this);
                        this.consume();
                    }
                    this.state = 146;
                    localctx.right = this.expr(6);
                    break;

                } 
            }
            this.state = 151;
            this._errHandler.sync(this);
            _alt = this._interp.adaptivePredict(this._input,15,this._ctx);
        }

    } catch( error) {
        if(error instanceof antlr4.error.RecognitionException) {
	        localctx.exception = error;
	        this._errHandler.reportError(this, error);
	        this._errHandler.recover(this, error);
	    } else {
	    	throw error;
	    }
    } finally {
        this.unrollRecursionContexts(_parentctx)
    }
    return localctx;
};


function TaxonContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = PqlParser.RULE_taxon;
    this.namespace = null; // IdentifierMultipartContext
    this.slug = null; // IdentifierMultipartContext
    this.tag = null; // IdentifierMultipartContext
    return this;
}

TaxonContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
TaxonContext.prototype.constructor = TaxonContext;

TaxonContext.prototype.identifierMultipart = function(i) {
    if(i===undefined) {
        i = null;
    }
    if(i===null) {
        return this.getTypedRuleContexts(IdentifierMultipartContext);
    } else {
        return this.getTypedRuleContext(IdentifierMultipartContext,i);
    }
};

TaxonContext.prototype.TAXON_OPTIONAL_OPERATOR = function() {
    return this.getToken(PqlParser.TAXON_OPTIONAL_OPERATOR, 0);
};

TaxonContext.prototype.PIPE = function() {
    return this.getToken(PqlParser.PIPE, 0);
};

TaxonContext.prototype.TAXON_TAG_DELIMITER = function() {
    return this.getToken(PqlParser.TAXON_TAG_DELIMITER, 0);
};

TaxonContext.prototype.enterRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.enterTaxon(this);
	}
};

TaxonContext.prototype.exitRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.exitTaxon(this);
	}
};

TaxonContext.prototype.accept = function(visitor) {
    if ( visitor instanceof PqlParserVisitor ) {
        return visitor.visitTaxon(this);
    } else {
        return visitor.visitChildren(this);
    }
};




PqlParser.TaxonContext = TaxonContext;

PqlParser.prototype.taxon = function() {

    var localctx = new TaxonContext(this, this._ctx, this.state);
    this.enterRule(localctx, 22, PqlParser.RULE_taxon);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 153;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        if(_la===PqlParser.TAXON_OPTIONAL_OPERATOR) {
            this.state = 152;
            this.match(PqlParser.TAXON_OPTIONAL_OPERATOR);
        }

        this.state = 158;
        this._errHandler.sync(this);
        var la_ = this._interp.adaptivePredict(this._input,17,this._ctx);
        if(la_===1) {
            this.state = 155;
            localctx.namespace = this.identifierMultipart();
            this.state = 156;
            this.match(PqlParser.PIPE);

        }
        this.state = 160;
        localctx.slug = this.identifierMultipart();
        this.state = 163;
        this._errHandler.sync(this);
        var la_ = this._interp.adaptivePredict(this._input,18,this._ctx);
        if(la_===1) {
            this.state = 161;
            this.match(PqlParser.TAXON_TAG_DELIMITER);
            this.state = 162;
            localctx.tag = this.identifierMultipart();

        }
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};


function IdentifierMultipartContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = PqlParser.RULE_identifierMultipart;
    return this;
}

IdentifierMultipartContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
IdentifierMultipartContext.prototype.constructor = IdentifierMultipartContext;

IdentifierMultipartContext.prototype.WORD = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(PqlParser.WORD);
    } else {
        return this.getToken(PqlParser.WORD, i);
    }
};


IdentifierMultipartContext.prototype.DOT = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(PqlParser.DOT);
    } else {
        return this.getToken(PqlParser.DOT, i);
    }
};


IdentifierMultipartContext.prototype.enterRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.enterIdentifierMultipart(this);
	}
};

IdentifierMultipartContext.prototype.exitRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.exitIdentifierMultipart(this);
	}
};

IdentifierMultipartContext.prototype.accept = function(visitor) {
    if ( visitor instanceof PqlParserVisitor ) {
        return visitor.visitIdentifierMultipart(this);
    } else {
        return visitor.visitChildren(this);
    }
};




PqlParser.IdentifierMultipartContext = IdentifierMultipartContext;

PqlParser.prototype.identifierMultipart = function() {

    var localctx = new IdentifierMultipartContext(this, this._ctx, this.state);
    this.enterRule(localctx, 24, PqlParser.RULE_identifierMultipart);
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 165;
        this.match(PqlParser.WORD);
        this.state = 170;
        this._errHandler.sync(this);
        var _alt = this._interp.adaptivePredict(this._input,19,this._ctx)
        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
            if(_alt===1) {
                this.state = 166;
                this.match(PqlParser.DOT);
                this.state = 167;
                this.match(PqlParser.WORD); 
            }
            this.state = 172;
            this._errHandler.sync(this);
            _alt = this._interp.adaptivePredict(this._input,19,this._ctx);
        }

    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};


function LiteralValueContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = PqlParser.RULE_literalValue;
    return this;
}

LiteralValueContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
LiteralValueContext.prototype.constructor = LiteralValueContext;

LiteralValueContext.prototype.NUMERIC_LITERAL = function() {
    return this.getToken(PqlParser.NUMERIC_LITERAL, 0);
};

LiteralValueContext.prototype.DOUBLE_QUOTED_STRING = function() {
    return this.getToken(PqlParser.DOUBLE_QUOTED_STRING, 0);
};

LiteralValueContext.prototype.SINGLE_QUOTED_STRING = function() {
    return this.getToken(PqlParser.SINGLE_QUOTED_STRING, 0);
};

LiteralValueContext.prototype.K_NULL = function() {
    return this.getToken(PqlParser.K_NULL, 0);
};

LiteralValueContext.prototype.K_TRUE = function() {
    return this.getToken(PqlParser.K_TRUE, 0);
};

LiteralValueContext.prototype.K_FALSE = function() {
    return this.getToken(PqlParser.K_FALSE, 0);
};

LiteralValueContext.prototype.enterRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.enterLiteralValue(this);
	}
};

LiteralValueContext.prototype.exitRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.exitLiteralValue(this);
	}
};

LiteralValueContext.prototype.accept = function(visitor) {
    if ( visitor instanceof PqlParserVisitor ) {
        return visitor.visitLiteralValue(this);
    } else {
        return visitor.visitChildren(this);
    }
};




PqlParser.LiteralValueContext = LiteralValueContext;

PqlParser.prototype.literalValue = function() {

    var localctx = new LiteralValueContext(this, this._ctx, this.state);
    this.enterRule(localctx, 26, PqlParser.RULE_literalValue);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 173;
        _la = this._input.LA(1);
        if(!(((((_la - 33)) & ~0x1f) == 0 && ((1 << (_la - 33)) & ((1 << (PqlParser.K_FALSE - 33)) | (1 << (PqlParser.K_NULL - 33)) | (1 << (PqlParser.K_TRUE - 33)) | (1 << (PqlParser.NUMERIC_LITERAL - 33)) | (1 << (PqlParser.DOUBLE_QUOTED_STRING - 33)) | (1 << (PqlParser.SINGLE_QUOTED_STRING - 33)))) !== 0))) {
        this._errHandler.recoverInline(this);
        }
        else {
        	this._errHandler.reportMatch(this);
            this.consume();
        }
    } catch (re) {
    	if(re instanceof antlr4.error.RecognitionException) {
	        localctx.exception = re;
	        this._errHandler.reportError(this, re);
	        this._errHandler.recover(this, re);
	    } else {
	    	throw re;
	    }
    } finally {
        this.exitRule();
    }
    return localctx;
};


PqlParser.prototype.sempred = function(localctx, ruleIndex, predIndex) {
	switch(ruleIndex) {
	case 10:
			return this.expr_sempred(localctx, predIndex);
    default:
        throw "No predicate with index:" + ruleIndex;
   }
};

PqlParser.prototype.expr_sempred = function(localctx, predIndex) {
	switch(predIndex) {
		case 0:
			return this.precpred(this._ctx, 10);
		case 1:
			return this.precpred(this._ctx, 9);
		case 2:
			return this.precpred(this._ctx, 8);
		case 3:
			return this.precpred(this._ctx, 7);
		case 4:
			return this.precpred(this._ctx, 6);
		case 5:
			return this.precpred(this._ctx, 5);
		default:
			throw "No predicate with index:" + predIndex;
	}
};


exports.PqlParser = PqlParser;

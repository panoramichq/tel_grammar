// Generated from grammar/TelParser.g4 by ANTLR 4.8
// jshint ignore: start
var antlr4 = require('antlr4/index');
var TelParserListener = require('./TelParserListener').TelParserListener;
var TelParserVisitor = require('./TelParserVisitor').TelParserVisitor;

var grammarFileName = "TelParser.g4";


var serializedATN = ["\u0003\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964",
    "\u0003>p\u0004\u0002\t\u0002\u0004\u0003\t\u0003\u0004\u0004\t\u0004",
    "\u0004\u0005\t\u0005\u0004\u0006\t\u0006\u0004\u0007\t\u0007\u0004\b",
    "\t\b\u0003\u0002\u0003\u0002\u0003\u0002\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0007",
    "\u0003\u001c\n\u0003\f\u0003\u000e\u0003\u001f\u000b\u0003\u0005\u0003",
    "!\n\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0005\u0003+\n\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0005\u0003B\n\u0003\u0007\u0003D\n\u0003\f",
    "\u0003\u000e\u0003G\u000b\u0003\u0003\u0004\u0005\u0004J\n\u0004\u0003",
    "\u0004\u0003\u0004\u0005\u0004N\n\u0004\u0003\u0004\u0003\u0004\u0005",
    "\u0004R\n\u0004\u0003\u0005\u0003\u0005\u0003\u0005\u0005\u0005W\n\u0005",
    "\u0003\u0006\u0005\u0006Z\n\u0006\u0003\u0006\u0003\u0006\u0003\u0006",
    "\u0005\u0006_\n\u0006\u0003\u0006\u0003\u0006\u0003\u0006\u0005\u0006",
    "d\n\u0006\u0003\u0007\u0003\u0007\u0003\u0007\u0007\u0007i\n\u0007\f",
    "\u0007\u000e\u0007l\u000b\u0007\u0003\b\u0003\b\u0003\b\u0002\u0003",
    "\u0004\t\u0002\u0004\u0006\b\n\f\u000e\u0002\n\u0005\u0002\u0019\u0019",
    "\u001e\u001e,,\u0004\u0002\u0014\u0014\u001a\u001b\u0004\u0002\u0019",
    "\u0019\u001e\u001e\u0004\u0002\t\n\u0017\u0018\u0005\u0002\b\b\u000b",
    "\f\u0011\u0011\u0004\u0002\u0007\u0007##\u0004\u0002\r\r//\u0007\u0002",
    "\'\'..224588\u0002~\u0002\u0010\u0003\u0002\u0002\u0002\u0004*\u0003",
    "\u0002\u0002\u0002\u0006Q\u0003\u0002\u0002\u0002\bV\u0003\u0002\u0002",
    "\u0002\nY\u0003\u0002\u0002\u0002\fe\u0003\u0002\u0002\u0002\u000em",
    "\u0003\u0002\u0002\u0002\u0010\u0011\u0005\u0004\u0003\u0002\u0011\u0012",
    "\u0007\u0002\u0002\u0003\u0012\u0003\u0003\u0002\u0002\u0002\u0013\u0014",
    "\b\u0003\u0001\u0002\u0014\u0015\t\u0002\u0002\u0002\u0015+\u0005\u0004",
    "\u0003\u000e\u0016\u0017\u0005\f\u0007\u0002\u0017 \u0007\u001c\u0002",
    "\u0002\u0018\u001d\u0005\u0004\u0003\u0002\u0019\u001a\u0007\u0013\u0002",
    "\u0002\u001a\u001c\u0005\u0004\u0003\u0002\u001b\u0019\u0003\u0002\u0002",
    "\u0002\u001c\u001f\u0003\u0002\u0002\u0002\u001d\u001b\u0003\u0002\u0002",
    "\u0002\u001d\u001e\u0003\u0002\u0002\u0002\u001e!\u0003\u0002\u0002",
    "\u0002\u001f\u001d\u0003\u0002\u0002\u0002 \u0018\u0003\u0002\u0002",
    "\u0002 !\u0003\u0002\u0002\u0002!\"\u0003\u0002\u0002\u0002\"#\u0007",
    "\u0012\u0002\u0002#+\u0003\u0002\u0002\u0002$%\u0007\u001c\u0002\u0002",
    "%&\u0005\u0004\u0003\u0002&\'\u0007\u0012\u0002\u0002\'+\u0003\u0002",
    "\u0002\u0002(+\u0005\n\u0006\u0002)+\u0005\u000e\b\u0002*\u0013\u0003",
    "\u0002\u0002\u0002*\u0016\u0003\u0002\u0002\u0002*$\u0003\u0002\u0002",
    "\u0002*(\u0003\u0002\u0002\u0002*)\u0003\u0002\u0002\u0002+E\u0003\u0002",
    "\u0002\u0002,-\f\u000b\u0002\u0002-.\t\u0003\u0002\u0002.D\u0005\u0004",
    "\u0003\f/0\f\n\u0002\u000201\t\u0004\u0002\u00021D\u0005\u0004\u0003",
    "\u000b23\f\t\u0002\u000234\t\u0005\u0002\u00024D\u0005\u0004\u0003\n",
    "56\f\b\u0002\u000267\t\u0006\u0002\u00027D\u0005\u0004\u0003\t89\f\u0007",
    "\u0002\u00029:\t\u0007\u0002\u0002:D\u0005\u0004\u0003\b;<\f\u0006\u0002",
    "\u0002<=\t\b\u0002\u0002=D\u0005\u0004\u0003\u0007>A\f\f\u0002\u0002",
    "?B\u0005\b\u0005\u0002@B\u0005\u0006\u0004\u0002A?\u0003\u0002\u0002",
    "\u0002A@\u0003\u0002\u0002\u0002BD\u0003\u0002\u0002\u0002C,\u0003\u0002",
    "\u0002\u0002C/\u0003\u0002\u0002\u0002C2\u0003\u0002\u0002\u0002C5\u0003",
    "\u0002\u0002\u0002C8\u0003\u0002\u0002\u0002C;\u0003\u0002\u0002\u0002",
    "C>\u0003\u0002\u0002\u0002DG\u0003\u0002\u0002\u0002EC\u0003\u0002\u0002",
    "\u0002EF\u0003\u0002\u0002\u0002F\u0005\u0003\u0002\u0002\u0002GE\u0003",
    "\u0002\u0002\u0002HJ\u0007(\u0002\u0002IH\u0003\u0002\u0002\u0002IJ",
    "\u0003\u0002\u0002\u0002JK\u0003\u0002\u0002\u0002KR\u0007-\u0002\u0002",
    "LN\u0007(\u0002\u0002ML\u0003\u0002\u0002\u0002MN\u0003\u0002\u0002",
    "\u0002NO\u0003\u0002\u0002\u0002OP\u0007,\u0002\u0002PR\u0007.\u0002",
    "\u0002QI\u0003\u0002\u0002\u0002QM\u0003\u0002\u0002\u0002R\u0007\u0003",
    "\u0002\u0002\u0002SW\u0007)\u0002\u0002TU\u0007(\u0002\u0002UW\u0007",
    ".\u0002\u0002VS\u0003\u0002\u0002\u0002VT\u0003\u0002\u0002\u0002W\t",
    "\u0003\u0002\u0002\u0002XZ\u0007\u0005\u0002\u0002YX\u0003\u0002\u0002",
    "\u0002YZ\u0003\u0002\u0002\u0002Z^\u0003\u0002\u0002\u0002[\\\u0005",
    "\f\u0007\u0002\\]\u0007\u0003\u0002\u0002]_\u0003\u0002\u0002\u0002",
    "^[\u0003\u0002\u0002\u0002^_\u0003\u0002\u0002\u0002_`\u0003\u0002\u0002",
    "\u0002`c\u0005\f\u0007\u0002ab\u0007\u0004\u0002\u0002bd\u0005\f\u0007",
    "\u0002ca\u0003\u0002\u0002\u0002cd\u0003\u0002\u0002\u0002d\u000b\u0003",
    "\u0002\u0002\u0002ej\u0007>\u0002\u0002fg\u0007\u0015\u0002\u0002gi",
    "\u0007>\u0002\u0002hf\u0003\u0002\u0002\u0002il\u0003\u0002\u0002\u0002",
    "jh\u0003\u0002\u0002\u0002jk\u0003\u0002\u0002\u0002k\r\u0003\u0002",
    "\u0002\u0002lj\u0003\u0002\u0002\u0002mn\t\t\u0002\u0002n\u000f\u0003",
    "\u0002\u0002\u0002\u0010\u001d *ACEIMQVY^cj"].join("");


var atn = new antlr4.atn.ATNDeserializer().deserialize(serializedATN);

var decisionsToDFA = atn.decisionToState.map( function(ds, index) { return new antlr4.dfa.DFA(ds, index); });

var sharedContextCache = new antlr4.PredictionContextCache();

var literalNames = [ null, null, "':'", "'?'", null, "'&&'", "'=='", "'>='", 
                     "'<='", "'!='", "'<>'", "'||'", "'<<'", "'>>'", "'&'", 
                     "'='", "')'", "','", null, "'.'", "'/'", "'>'", "'<'", 
                     "'-'", "'%'", null, "'('", "'|'", "'+'", "';'", "'*'", 
                     "'~'", "'_'" ];

var symbolicNames = [ null, "TAXON_NAMESPACE_DELIMITER", "TAXON_TAG_DELIMITER", 
                      "TAXON_OPTIONAL_OPERATOR", "IDENTIFIER_TEL", "AND", 
                      "EQ", "GT_EQ", "LT_EQ", "NOT_EQ1", "NOT_EQ2", "OR", 
                      "SHIFT_LEFT", "SHIFT_RIGHT", "AMP", "ASSIGN", "CLOSE_PAREN", 
                      "COMMA", "DIV", "DOT", "FORWARD_SLASH", "GT", "LT", 
                      "MINUS", "MOD", "MULT", "OPEN_PAREN", "PIPE", "PLUS", 
                      "SCOL", "STAR", "TILDE", "UNDER", "K_AND", "K_ASC", 
                      "K_BY", "K_DESC", "K_FALSE", "K_IS", "K_ISNULL", "K_LIKE", 
                      "K_LIMIT", "K_NOT", "K_NOTNULL", "K_NULL", "K_OR", 
                      "K_ORDER", "K_SELECT", "K_TRUE", "K_WHERE", "NUMERIC_LITERAL", 
                      "DOUBLE_QUOTED_STRING", "DOUBLE_QUOTED_STRING_TEL", 
                      "DOUBLE_QUOTED_STRING_SQL", "SINGLE_QUOTED_STRING", 
                      "SINGLE_QUOTED_STRING_TEL", "SINGLE_QUOTED_STRING_SQL", 
                      "SINGLE_LINE_COMMENT", "MULTILINE_COMMENT", "SPACES", 
                      "IDENTIFIER" ];

var ruleNames =  [ "parse", "expr", "isNotNull", "isNull", "taxon", "identifierMultipart", 
                   "literalValue" ];

function TelParser (input) {
	antlr4.Parser.call(this, input);
    this._interp = new antlr4.atn.ParserATNSimulator(this, atn, decisionsToDFA, sharedContextCache);
    this.ruleNames = ruleNames;
    this.literalNames = literalNames;
    this.symbolicNames = symbolicNames;
    return this;
}

TelParser.prototype = Object.create(antlr4.Parser.prototype);
TelParser.prototype.constructor = TelParser;

Object.defineProperty(TelParser.prototype, "atn", {
	get : function() {
		return atn;
	}
});

TelParser.EOF = antlr4.Token.EOF;
TelParser.TAXON_NAMESPACE_DELIMITER = 1;
TelParser.TAXON_TAG_DELIMITER = 2;
TelParser.TAXON_OPTIONAL_OPERATOR = 3;
TelParser.IDENTIFIER_TEL = 4;
TelParser.AND = 5;
TelParser.EQ = 6;
TelParser.GT_EQ = 7;
TelParser.LT_EQ = 8;
TelParser.NOT_EQ1 = 9;
TelParser.NOT_EQ2 = 10;
TelParser.OR = 11;
TelParser.SHIFT_LEFT = 12;
TelParser.SHIFT_RIGHT = 13;
TelParser.AMP = 14;
TelParser.ASSIGN = 15;
TelParser.CLOSE_PAREN = 16;
TelParser.COMMA = 17;
TelParser.DIV = 18;
TelParser.DOT = 19;
TelParser.FORWARD_SLASH = 20;
TelParser.GT = 21;
TelParser.LT = 22;
TelParser.MINUS = 23;
TelParser.MOD = 24;
TelParser.MULT = 25;
TelParser.OPEN_PAREN = 26;
TelParser.PIPE = 27;
TelParser.PLUS = 28;
TelParser.SCOL = 29;
TelParser.STAR = 30;
TelParser.TILDE = 31;
TelParser.UNDER = 32;
TelParser.K_AND = 33;
TelParser.K_ASC = 34;
TelParser.K_BY = 35;
TelParser.K_DESC = 36;
TelParser.K_FALSE = 37;
TelParser.K_IS = 38;
TelParser.K_ISNULL = 39;
TelParser.K_LIKE = 40;
TelParser.K_LIMIT = 41;
TelParser.K_NOT = 42;
TelParser.K_NOTNULL = 43;
TelParser.K_NULL = 44;
TelParser.K_OR = 45;
TelParser.K_ORDER = 46;
TelParser.K_SELECT = 47;
TelParser.K_TRUE = 48;
TelParser.K_WHERE = 49;
TelParser.NUMERIC_LITERAL = 50;
TelParser.DOUBLE_QUOTED_STRING = 51;
TelParser.DOUBLE_QUOTED_STRING_TEL = 52;
TelParser.DOUBLE_QUOTED_STRING_SQL = 53;
TelParser.SINGLE_QUOTED_STRING = 54;
TelParser.SINGLE_QUOTED_STRING_TEL = 55;
TelParser.SINGLE_QUOTED_STRING_SQL = 56;
TelParser.SINGLE_LINE_COMMENT = 57;
TelParser.MULTILINE_COMMENT = 58;
TelParser.SPACES = 59;
TelParser.IDENTIFIER = 60;

TelParser.RULE_parse = 0;
TelParser.RULE_expr = 1;
TelParser.RULE_isNotNull = 2;
TelParser.RULE_isNull = 3;
TelParser.RULE_taxon = 4;
TelParser.RULE_identifierMultipart = 5;
TelParser.RULE_literalValue = 6;


function ParseContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = TelParser.RULE_parse;
    return this;
}

ParseContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
ParseContext.prototype.constructor = ParseContext;

ParseContext.prototype.expr = function() {
    return this.getTypedRuleContext(ExprContext,0);
};

ParseContext.prototype.EOF = function() {
    return this.getToken(TelParser.EOF, 0);
};

ParseContext.prototype.enterRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.enterParse(this);
	}
};

ParseContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.exitParse(this);
	}
};

ParseContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelParserVisitor ) {
        return visitor.visitParse(this);
    } else {
        return visitor.visitChildren(this);
    }
};




TelParser.ParseContext = ParseContext;

TelParser.prototype.parse = function() {

    var localctx = new ParseContext(this, this._ctx, this.state);
    this.enterRule(localctx, 0, TelParser.RULE_parse);
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 14;
        this.expr(0);
        this.state = 15;
        this.match(TelParser.EOF);
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
    this.ruleIndex = TelParser.RULE_expr;
    this.left = null; // ExprContext
    this.unary_operator = null; // Token
    this.right = null; // ExprContext
    this.function_name = null; // IdentifierMultipartContext
    this.arguments = null; // ExprContext
    this.operator = null; // Token
    this.is_null = null; // IsNullContext
    this.is_not_null = null; // IsNotNullContext
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
    return this.getToken(TelParser.MINUS, 0);
};

ExprContext.prototype.PLUS = function() {
    return this.getToken(TelParser.PLUS, 0);
};

ExprContext.prototype.K_NOT = function() {
    return this.getToken(TelParser.K_NOT, 0);
};

ExprContext.prototype.OPEN_PAREN = function() {
    return this.getToken(TelParser.OPEN_PAREN, 0);
};

ExprContext.prototype.CLOSE_PAREN = function() {
    return this.getToken(TelParser.CLOSE_PAREN, 0);
};

ExprContext.prototype.identifierMultipart = function() {
    return this.getTypedRuleContext(IdentifierMultipartContext,0);
};

ExprContext.prototype.COMMA = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(TelParser.COMMA);
    } else {
        return this.getToken(TelParser.COMMA, i);
    }
};


ExprContext.prototype.taxon = function() {
    return this.getTypedRuleContext(TaxonContext,0);
};

ExprContext.prototype.literalValue = function() {
    return this.getTypedRuleContext(LiteralValueContext,0);
};

ExprContext.prototype.MULT = function() {
    return this.getToken(TelParser.MULT, 0);
};

ExprContext.prototype.DIV = function() {
    return this.getToken(TelParser.DIV, 0);
};

ExprContext.prototype.MOD = function() {
    return this.getToken(TelParser.MOD, 0);
};

ExprContext.prototype.LT = function() {
    return this.getToken(TelParser.LT, 0);
};

ExprContext.prototype.LT_EQ = function() {
    return this.getToken(TelParser.LT_EQ, 0);
};

ExprContext.prototype.GT = function() {
    return this.getToken(TelParser.GT, 0);
};

ExprContext.prototype.GT_EQ = function() {
    return this.getToken(TelParser.GT_EQ, 0);
};

ExprContext.prototype.ASSIGN = function() {
    return this.getToken(TelParser.ASSIGN, 0);
};

ExprContext.prototype.EQ = function() {
    return this.getToken(TelParser.EQ, 0);
};

ExprContext.prototype.NOT_EQ1 = function() {
    return this.getToken(TelParser.NOT_EQ1, 0);
};

ExprContext.prototype.NOT_EQ2 = function() {
    return this.getToken(TelParser.NOT_EQ2, 0);
};

ExprContext.prototype.K_AND = function() {
    return this.getToken(TelParser.K_AND, 0);
};

ExprContext.prototype.AND = function() {
    return this.getToken(TelParser.AND, 0);
};

ExprContext.prototype.K_OR = function() {
    return this.getToken(TelParser.K_OR, 0);
};

ExprContext.prototype.OR = function() {
    return this.getToken(TelParser.OR, 0);
};

ExprContext.prototype.isNull = function() {
    return this.getTypedRuleContext(IsNullContext,0);
};

ExprContext.prototype.isNotNull = function() {
    return this.getTypedRuleContext(IsNotNullContext,0);
};

ExprContext.prototype.enterRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.enterExpr(this);
	}
};

ExprContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.exitExpr(this);
	}
};

ExprContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelParserVisitor ) {
        return visitor.visitExpr(this);
    } else {
        return visitor.visitChildren(this);
    }
};



TelParser.prototype.expr = function(_p) {
	if(_p===undefined) {
	    _p = 0;
	}
    var _parentctx = this._ctx;
    var _parentState = this.state;
    var localctx = new ExprContext(this, this._ctx, _parentState);
    var _prevctx = localctx;
    var _startState = 2;
    this.enterRecursionRule(localctx, 2, TelParser.RULE_expr, _p);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 40;
        this._errHandler.sync(this);
        var la_ = this._interp.adaptivePredict(this._input,2,this._ctx);
        switch(la_) {
        case 1:
            this.state = 18;
            localctx.unary_operator = this._input.LT(1);
            _la = this._input.LA(1);
            if(!(((((_la - 23)) & ~0x1f) == 0 && ((1 << (_la - 23)) & ((1 << (TelParser.MINUS - 23)) | (1 << (TelParser.PLUS - 23)) | (1 << (TelParser.K_NOT - 23)))) !== 0))) {
                localctx.unary_operator = this._errHandler.recoverInline(this);
            }
            else {
            	this._errHandler.reportMatch(this);
                this.consume();
            }
            this.state = 19;
            localctx.right = this.expr(12);
            break;

        case 2:
            this.state = 20;
            localctx.function_name = this.identifierMultipart();
            this.state = 21;
            this.match(TelParser.OPEN_PAREN);
            this.state = 30;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
            if((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << TelParser.TAXON_OPTIONAL_OPERATOR) | (1 << TelParser.MINUS) | (1 << TelParser.OPEN_PAREN) | (1 << TelParser.PLUS))) !== 0) || ((((_la - 37)) & ~0x1f) == 0 && ((1 << (_la - 37)) & ((1 << (TelParser.K_FALSE - 37)) | (1 << (TelParser.K_NOT - 37)) | (1 << (TelParser.K_NULL - 37)) | (1 << (TelParser.K_TRUE - 37)) | (1 << (TelParser.NUMERIC_LITERAL - 37)) | (1 << (TelParser.DOUBLE_QUOTED_STRING - 37)) | (1 << (TelParser.SINGLE_QUOTED_STRING - 37)) | (1 << (TelParser.IDENTIFIER - 37)))) !== 0)) {
                this.state = 22;
                localctx.arguments = this.expr(0);
                this.state = 27;
                this._errHandler.sync(this);
                _la = this._input.LA(1);
                while(_la===TelParser.COMMA) {
                    this.state = 23;
                    this.match(TelParser.COMMA);
                    this.state = 24;
                    localctx.arguments = this.expr(0);
                    this.state = 29;
                    this._errHandler.sync(this);
                    _la = this._input.LA(1);
                }
            }

            this.state = 32;
            this.match(TelParser.CLOSE_PAREN);
            break;

        case 3:
            this.state = 34;
            this.match(TelParser.OPEN_PAREN);
            this.state = 35;
            this.expr(0);
            this.state = 36;
            this.match(TelParser.CLOSE_PAREN);
            break;

        case 4:
            this.state = 38;
            this.taxon();
            break;

        case 5:
            this.state = 39;
            this.literalValue();
            break;

        }
        this._ctx.stop = this._input.LT(-1);
        this.state = 67;
        this._errHandler.sync(this);
        var _alt = this._interp.adaptivePredict(this._input,5,this._ctx)
        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
            if(_alt===1) {
                if(this._parseListeners!==null) {
                    this.triggerExitRuleEvent();
                }
                _prevctx = localctx;
                this.state = 65;
                this._errHandler.sync(this);
                var la_ = this._interp.adaptivePredict(this._input,4,this._ctx);
                switch(la_) {
                case 1:
                    localctx = new ExprContext(this, _parentctx, _parentState);
                    localctx.left = _prevctx;
                    this.pushNewRecursionContext(localctx, _startState, TelParser.RULE_expr);
                    this.state = 42;
                    if (!( this.precpred(this._ctx, 9))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 9)");
                    }
                    this.state = 43;
                    localctx.operator = this._input.LT(1);
                    _la = this._input.LA(1);
                    if(!((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << TelParser.DIV) | (1 << TelParser.MOD) | (1 << TelParser.MULT))) !== 0))) {
                        localctx.operator = this._errHandler.recoverInline(this);
                    }
                    else {
                    	this._errHandler.reportMatch(this);
                        this.consume();
                    }
                    this.state = 44;
                    localctx.right = this.expr(10);
                    break;

                case 2:
                    localctx = new ExprContext(this, _parentctx, _parentState);
                    localctx.left = _prevctx;
                    this.pushNewRecursionContext(localctx, _startState, TelParser.RULE_expr);
                    this.state = 45;
                    if (!( this.precpred(this._ctx, 8))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 8)");
                    }
                    this.state = 46;
                    localctx.operator = this._input.LT(1);
                    _la = this._input.LA(1);
                    if(!(_la===TelParser.MINUS || _la===TelParser.PLUS)) {
                        localctx.operator = this._errHandler.recoverInline(this);
                    }
                    else {
                    	this._errHandler.reportMatch(this);
                        this.consume();
                    }
                    this.state = 47;
                    localctx.right = this.expr(9);
                    break;

                case 3:
                    localctx = new ExprContext(this, _parentctx, _parentState);
                    localctx.left = _prevctx;
                    this.pushNewRecursionContext(localctx, _startState, TelParser.RULE_expr);
                    this.state = 48;
                    if (!( this.precpred(this._ctx, 7))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 7)");
                    }
                    this.state = 49;
                    localctx.operator = this._input.LT(1);
                    _la = this._input.LA(1);
                    if(!((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << TelParser.GT_EQ) | (1 << TelParser.LT_EQ) | (1 << TelParser.GT) | (1 << TelParser.LT))) !== 0))) {
                        localctx.operator = this._errHandler.recoverInline(this);
                    }
                    else {
                    	this._errHandler.reportMatch(this);
                        this.consume();
                    }
                    this.state = 50;
                    localctx.right = this.expr(8);
                    break;

                case 4:
                    localctx = new ExprContext(this, _parentctx, _parentState);
                    localctx.left = _prevctx;
                    this.pushNewRecursionContext(localctx, _startState, TelParser.RULE_expr);
                    this.state = 51;
                    if (!( this.precpred(this._ctx, 6))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 6)");
                    }
                    this.state = 52;
                    localctx.operator = this._input.LT(1);
                    _la = this._input.LA(1);
                    if(!((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << TelParser.EQ) | (1 << TelParser.NOT_EQ1) | (1 << TelParser.NOT_EQ2) | (1 << TelParser.ASSIGN))) !== 0))) {
                        localctx.operator = this._errHandler.recoverInline(this);
                    }
                    else {
                    	this._errHandler.reportMatch(this);
                        this.consume();
                    }
                    this.state = 53;
                    localctx.right = this.expr(7);
                    break;

                case 5:
                    localctx = new ExprContext(this, _parentctx, _parentState);
                    localctx.left = _prevctx;
                    this.pushNewRecursionContext(localctx, _startState, TelParser.RULE_expr);
                    this.state = 54;
                    if (!( this.precpred(this._ctx, 5))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 5)");
                    }
                    this.state = 55;
                    localctx.operator = this._input.LT(1);
                    _la = this._input.LA(1);
                    if(!(_la===TelParser.AND || _la===TelParser.K_AND)) {
                        localctx.operator = this._errHandler.recoverInline(this);
                    }
                    else {
                    	this._errHandler.reportMatch(this);
                        this.consume();
                    }
                    this.state = 56;
                    localctx.right = this.expr(6);
                    break;

                case 6:
                    localctx = new ExprContext(this, _parentctx, _parentState);
                    localctx.left = _prevctx;
                    this.pushNewRecursionContext(localctx, _startState, TelParser.RULE_expr);
                    this.state = 57;
                    if (!( this.precpred(this._ctx, 4))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 4)");
                    }
                    this.state = 58;
                    localctx.operator = this._input.LT(1);
                    _la = this._input.LA(1);
                    if(!(_la===TelParser.OR || _la===TelParser.K_OR)) {
                        localctx.operator = this._errHandler.recoverInline(this);
                    }
                    else {
                    	this._errHandler.reportMatch(this);
                        this.consume();
                    }
                    this.state = 59;
                    localctx.right = this.expr(5);
                    break;

                case 7:
                    localctx = new ExprContext(this, _parentctx, _parentState);
                    localctx.left = _prevctx;
                    this.pushNewRecursionContext(localctx, _startState, TelParser.RULE_expr);
                    this.state = 60;
                    if (!( this.precpred(this._ctx, 10))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 10)");
                    }
                    this.state = 63;
                    this._errHandler.sync(this);
                    var la_ = this._interp.adaptivePredict(this._input,3,this._ctx);
                    switch(la_) {
                    case 1:
                        this.state = 61;
                        localctx.is_null = this.isNull();
                        break;

                    case 2:
                        this.state = 62;
                        localctx.is_not_null = this.isNotNull();
                        break;

                    }
                    break;

                } 
            }
            this.state = 69;
            this._errHandler.sync(this);
            _alt = this._interp.adaptivePredict(this._input,5,this._ctx);
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


function IsNotNullContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = TelParser.RULE_isNotNull;
    return this;
}

IsNotNullContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
IsNotNullContext.prototype.constructor = IsNotNullContext;

IsNotNullContext.prototype.K_NOTNULL = function() {
    return this.getToken(TelParser.K_NOTNULL, 0);
};

IsNotNullContext.prototype.K_IS = function() {
    return this.getToken(TelParser.K_IS, 0);
};

IsNotNullContext.prototype.K_NOT = function() {
    return this.getToken(TelParser.K_NOT, 0);
};

IsNotNullContext.prototype.K_NULL = function() {
    return this.getToken(TelParser.K_NULL, 0);
};

IsNotNullContext.prototype.enterRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.enterIsNotNull(this);
	}
};

IsNotNullContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.exitIsNotNull(this);
	}
};

IsNotNullContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelParserVisitor ) {
        return visitor.visitIsNotNull(this);
    } else {
        return visitor.visitChildren(this);
    }
};




TelParser.IsNotNullContext = IsNotNullContext;

TelParser.prototype.isNotNull = function() {

    var localctx = new IsNotNullContext(this, this._ctx, this.state);
    this.enterRule(localctx, 4, TelParser.RULE_isNotNull);
    var _la = 0; // Token type
    try {
        this.state = 79;
        this._errHandler.sync(this);
        var la_ = this._interp.adaptivePredict(this._input,8,this._ctx);
        switch(la_) {
        case 1:
            this.enterOuterAlt(localctx, 1);
            this.state = 71;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
            if(_la===TelParser.K_IS) {
                this.state = 70;
                this.match(TelParser.K_IS);
            }

            this.state = 73;
            this.match(TelParser.K_NOTNULL);
            break;

        case 2:
            this.enterOuterAlt(localctx, 2);
            this.state = 75;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
            if(_la===TelParser.K_IS) {
                this.state = 74;
                this.match(TelParser.K_IS);
            }

            this.state = 77;
            this.match(TelParser.K_NOT);
            this.state = 78;
            this.match(TelParser.K_NULL);
            break;

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


function IsNullContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = TelParser.RULE_isNull;
    return this;
}

IsNullContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
IsNullContext.prototype.constructor = IsNullContext;

IsNullContext.prototype.K_ISNULL = function() {
    return this.getToken(TelParser.K_ISNULL, 0);
};

IsNullContext.prototype.K_IS = function() {
    return this.getToken(TelParser.K_IS, 0);
};

IsNullContext.prototype.K_NULL = function() {
    return this.getToken(TelParser.K_NULL, 0);
};

IsNullContext.prototype.enterRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.enterIsNull(this);
	}
};

IsNullContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.exitIsNull(this);
	}
};

IsNullContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelParserVisitor ) {
        return visitor.visitIsNull(this);
    } else {
        return visitor.visitChildren(this);
    }
};




TelParser.IsNullContext = IsNullContext;

TelParser.prototype.isNull = function() {

    var localctx = new IsNullContext(this, this._ctx, this.state);
    this.enterRule(localctx, 6, TelParser.RULE_isNull);
    try {
        this.state = 84;
        this._errHandler.sync(this);
        switch(this._input.LA(1)) {
        case TelParser.K_ISNULL:
            this.enterOuterAlt(localctx, 1);
            this.state = 81;
            this.match(TelParser.K_ISNULL);
            break;
        case TelParser.K_IS:
            this.enterOuterAlt(localctx, 2);
            this.state = 82;
            this.match(TelParser.K_IS);
            this.state = 83;
            this.match(TelParser.K_NULL);
            break;
        default:
            throw new antlr4.error.NoViableAltException(this);
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


function TaxonContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = TelParser.RULE_taxon;
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
    return this.getToken(TelParser.TAXON_OPTIONAL_OPERATOR, 0);
};

TaxonContext.prototype.TAXON_NAMESPACE_DELIMITER = function() {
    return this.getToken(TelParser.TAXON_NAMESPACE_DELIMITER, 0);
};

TaxonContext.prototype.TAXON_TAG_DELIMITER = function() {
    return this.getToken(TelParser.TAXON_TAG_DELIMITER, 0);
};

TaxonContext.prototype.enterRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.enterTaxon(this);
	}
};

TaxonContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.exitTaxon(this);
	}
};

TaxonContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelParserVisitor ) {
        return visitor.visitTaxon(this);
    } else {
        return visitor.visitChildren(this);
    }
};




TelParser.TaxonContext = TaxonContext;

TelParser.prototype.taxon = function() {

    var localctx = new TaxonContext(this, this._ctx, this.state);
    this.enterRule(localctx, 8, TelParser.RULE_taxon);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 87;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        if(_la===TelParser.TAXON_OPTIONAL_OPERATOR) {
            this.state = 86;
            this.match(TelParser.TAXON_OPTIONAL_OPERATOR);
        }

        this.state = 92;
        this._errHandler.sync(this);
        var la_ = this._interp.adaptivePredict(this._input,11,this._ctx);
        if(la_===1) {
            this.state = 89;
            localctx.namespace = this.identifierMultipart();
            this.state = 90;
            this.match(TelParser.TAXON_NAMESPACE_DELIMITER);

        }
        this.state = 94;
        localctx.slug = this.identifierMultipart();
        this.state = 97;
        this._errHandler.sync(this);
        var la_ = this._interp.adaptivePredict(this._input,12,this._ctx);
        if(la_===1) {
            this.state = 95;
            this.match(TelParser.TAXON_TAG_DELIMITER);
            this.state = 96;
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
    this.ruleIndex = TelParser.RULE_identifierMultipart;
    this.parts = null; // Token
    return this;
}

IdentifierMultipartContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
IdentifierMultipartContext.prototype.constructor = IdentifierMultipartContext;

IdentifierMultipartContext.prototype.IDENTIFIER = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(TelParser.IDENTIFIER);
    } else {
        return this.getToken(TelParser.IDENTIFIER, i);
    }
};


IdentifierMultipartContext.prototype.DOT = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(TelParser.DOT);
    } else {
        return this.getToken(TelParser.DOT, i);
    }
};


IdentifierMultipartContext.prototype.enterRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.enterIdentifierMultipart(this);
	}
};

IdentifierMultipartContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.exitIdentifierMultipart(this);
	}
};

IdentifierMultipartContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelParserVisitor ) {
        return visitor.visitIdentifierMultipart(this);
    } else {
        return visitor.visitChildren(this);
    }
};




TelParser.IdentifierMultipartContext = IdentifierMultipartContext;

TelParser.prototype.identifierMultipart = function() {

    var localctx = new IdentifierMultipartContext(this, this._ctx, this.state);
    this.enterRule(localctx, 10, TelParser.RULE_identifierMultipart);
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 99;
        localctx.parts = this.match(TelParser.IDENTIFIER);
        this.state = 104;
        this._errHandler.sync(this);
        var _alt = this._interp.adaptivePredict(this._input,13,this._ctx)
        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
            if(_alt===1) {
                this.state = 100;
                this.match(TelParser.DOT);
                this.state = 101;
                localctx.parts = this.match(TelParser.IDENTIFIER); 
            }
            this.state = 106;
            this._errHandler.sync(this);
            _alt = this._interp.adaptivePredict(this._input,13,this._ctx);
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
    this.ruleIndex = TelParser.RULE_literalValue;
    return this;
}

LiteralValueContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
LiteralValueContext.prototype.constructor = LiteralValueContext;

LiteralValueContext.prototype.NUMERIC_LITERAL = function() {
    return this.getToken(TelParser.NUMERIC_LITERAL, 0);
};

LiteralValueContext.prototype.DOUBLE_QUOTED_STRING = function() {
    return this.getToken(TelParser.DOUBLE_QUOTED_STRING, 0);
};

LiteralValueContext.prototype.SINGLE_QUOTED_STRING = function() {
    return this.getToken(TelParser.SINGLE_QUOTED_STRING, 0);
};

LiteralValueContext.prototype.K_NULL = function() {
    return this.getToken(TelParser.K_NULL, 0);
};

LiteralValueContext.prototype.K_TRUE = function() {
    return this.getToken(TelParser.K_TRUE, 0);
};

LiteralValueContext.prototype.K_FALSE = function() {
    return this.getToken(TelParser.K_FALSE, 0);
};

LiteralValueContext.prototype.enterRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.enterLiteralValue(this);
	}
};

LiteralValueContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.exitLiteralValue(this);
	}
};

LiteralValueContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelParserVisitor ) {
        return visitor.visitLiteralValue(this);
    } else {
        return visitor.visitChildren(this);
    }
};




TelParser.LiteralValueContext = LiteralValueContext;

TelParser.prototype.literalValue = function() {

    var localctx = new LiteralValueContext(this, this._ctx, this.state);
    this.enterRule(localctx, 12, TelParser.RULE_literalValue);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 107;
        _la = this._input.LA(1);
        if(!(((((_la - 37)) & ~0x1f) == 0 && ((1 << (_la - 37)) & ((1 << (TelParser.K_FALSE - 37)) | (1 << (TelParser.K_NULL - 37)) | (1 << (TelParser.K_TRUE - 37)) | (1 << (TelParser.NUMERIC_LITERAL - 37)) | (1 << (TelParser.DOUBLE_QUOTED_STRING - 37)) | (1 << (TelParser.SINGLE_QUOTED_STRING - 37)))) !== 0))) {
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


TelParser.prototype.sempred = function(localctx, ruleIndex, predIndex) {
	switch(ruleIndex) {
	case 1:
			return this.expr_sempred(localctx, predIndex);
    default:
        throw "No predicate with index:" + ruleIndex;
   }
};

TelParser.prototype.expr_sempred = function(localctx, predIndex) {
	switch(predIndex) {
		case 0:
			return this.precpred(this._ctx, 9);
		case 1:
			return this.precpred(this._ctx, 8);
		case 2:
			return this.precpred(this._ctx, 7);
		case 3:
			return this.precpred(this._ctx, 6);
		case 4:
			return this.precpred(this._ctx, 5);
		case 5:
			return this.precpred(this._ctx, 4);
		case 6:
			return this.precpred(this._ctx, 10);
		default:
			throw "No predicate with index:" + predIndex;
	}
};


exports.TelParser = TelParser;

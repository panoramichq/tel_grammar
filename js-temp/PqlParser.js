// Generated from grammar/PqlParser.g4 by ANTLR 4.8
// jshint ignore: start
var antlr4 = require('antlr4/index');
var PqlParserListener = require('./PqlParserListener').PqlParserListener;
var PqlParserVisitor = require('./PqlParserVisitor').PqlParserVisitor;

var grammarFileName = "PqlParser.g4";


var serializedATN = ["\u0003\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964",
    "\u00035r\u0004\u0002\t\u0002\u0004\u0003\t\u0003\u0004\u0004\t\u0004",
    "\u0004\u0005\t\u0005\u0004\u0006\t\u0006\u0004\u0007\t\u0007\u0004\b",
    "\t\b\u0003\u0002\u0003\u0002\u0003\u0002\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0005\u0003\u001e\n\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0005\u0003.\n\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0005\u0003:\n\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0005\u0003@\n\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0007\u0003G\n\u0003\f\u0003\u000e\u0003J\u000b\u0003\u0003",
    "\u0004\u0003\u0004\u0003\u0004\u0005\u0004O\n\u0004\u0003\u0004\u0003",
    "\u0004\u0003\u0005\u0003\u0005\u0003\u0005\u0007\u0005V\n\u0005\f\u0005",
    "\u000e\u0005Y\u000b\u0005\u0003\u0006\u0005\u0006\\\n\u0006\u0003\u0006",
    "\u0003\u0006\u0003\u0006\u0005\u0006a\n\u0006\u0003\u0006\u0003\u0006",
    "\u0003\u0006\u0005\u0006f\n\u0006\u0003\u0007\u0003\u0007\u0003\u0007",
    "\u0007\u0007k\n\u0007\f\u0007\u000e\u0007n\u000b\u0007\u0003\b\u0003",
    "\b\u0003\b\u0002\u0003\u0004\t\u0002\u0004\u0006\b\n\f\u000e\u0002\n",
    "\u0005\u0002\u0015\u0015\u0019\u0019&&\u0005\u0002\u0012\u0012\u0016",
    "\u0016\u001c\u001c\u0004\u0002\u0015\u0015\u0019\u0019\u0004\u0002\u0005",
    "\u0006\u0013\u0014\u0006\u0002\u0004\u0004\u0007\b\r\r##\u0004\u0002",
    "\u0003\u0003\u001f\u001f\u0004\u0002\t\t))\u0006\u0002!!((*,//\u0002",
    "\u0080\u0002\u0010\u0003\u0002\u0002\u0002\u0004\u001d\u0003\u0002\u0002",
    "\u0002\u0006K\u0003\u0002\u0002\u0002\bR\u0003\u0002\u0002\u0002\n[",
    "\u0003\u0002\u0002\u0002\fg\u0003\u0002\u0002\u0002\u000eo\u0003\u0002",
    "\u0002\u0002\u0010\u0011\u0005\u0004\u0003\u0002\u0011\u0012\u0007\u0002",
    "\u0002\u0003\u0012\u0003\u0003\u0002\u0002\u0002\u0013\u0014\b\u0003",
    "\u0001\u0002\u0014\u0015\t\u0002\u0002\u0002\u0015\u001e\u0005\u0004",
    "\u0003\u0010\u0016\u0017\u0007\u0017\u0002\u0002\u0017\u0018\u0005\u0004",
    "\u0003\u0002\u0018\u0019\u0007\u000e\u0002\u0002\u0019\u001e\u0003\u0002",
    "\u0002\u0002\u001a\u001e\u0005\u000e\b\u0002\u001b\u001e\u0005\u0006",
    "\u0004\u0002\u001c\u001e\u0005\n\u0006\u0002\u001d\u0013\u0003\u0002",
    "\u0002\u0002\u001d\u0016\u0003\u0002\u0002\u0002\u001d\u001a\u0003\u0002",
    "\u0002\u0002\u001d\u001b\u0003\u0002\u0002\u0002\u001d\u001c\u0003\u0002",
    "\u0002\u0002\u001eH\u0003\u0002\u0002\u0002\u001f \f\u000f\u0002\u0002",
    " !\t\u0003\u0002\u0002!G\u0005\u0004\u0003\u0010\"#\f\u000e\u0002\u0002",
    "#$\t\u0004\u0002\u0002$G\u0005\u0004\u0003\u000f%&\f\r\u0002\u0002&",
    "\'\t\u0005\u0002\u0002\'G\u0005\u0004\u0003\u000e()\f\f\u0002\u0002",
    ")*\t\u0006\u0002\u0002*G\u0005\u0004\u0003\r+-\f\u000b\u0002\u0002,",
    ".\u0007&\u0002\u0002-,\u0003\u0002\u0002\u0002-.\u0003\u0002\u0002\u0002",
    "./\u0003\u0002\u0002\u0002/0\u0007%\u0002\u00020G\u0005\u0004\u0003",
    "\f12\f\t\u0002\u000223\t\u0007\u0002\u00023G\u0005\u0004\u0003\n45\f",
    "\b\u0002\u000256\t\b\u0002\u00026G\u0005\u0004\u0003\t79\f\u0007\u0002",
    "\u00028:\u0007&\u0002\u000298\u0003\u0002\u0002\u00029:\u0003\u0002",
    "\u0002\u0002:;\u0003\u0002\u0002\u0002;<\u0007 \u0002\u0002<G\u0005",
    "\u0004\u0003\b=?\f\n\u0002\u0002>@\u0007&\u0002\u0002?>\u0003\u0002",
    "\u0002\u0002?@\u0003\u0002\u0002\u0002@A\u0003\u0002\u0002\u0002AB\u0007",
    "\"\u0002\u0002BC\u0007\u0017\u0002\u0002CD\u0005\b\u0005\u0002DE\u0007",
    "\u000e\u0002\u0002EG\u0003\u0002\u0002\u0002F\u001f\u0003\u0002\u0002",
    "\u0002F\"\u0003\u0002\u0002\u0002F%\u0003\u0002\u0002\u0002F(\u0003",
    "\u0002\u0002\u0002F+\u0003\u0002\u0002\u0002F1\u0003\u0002\u0002\u0002",
    "F4\u0003\u0002\u0002\u0002F7\u0003\u0002\u0002\u0002F=\u0003\u0002\u0002",
    "\u0002GJ\u0003\u0002\u0002\u0002HF\u0003\u0002\u0002\u0002HI\u0003\u0002",
    "\u0002\u0002I\u0005\u0003\u0002\u0002\u0002JH\u0003\u0002\u0002\u0002",
    "KL\u0005\f\u0007\u0002LN\u0007\u0017\u0002\u0002MO\u0005\b\u0005\u0002",
    "NM\u0003\u0002\u0002\u0002NO\u0003\u0002\u0002\u0002OP\u0003\u0002\u0002",
    "\u0002PQ\u0007\u000e\u0002\u0002Q\u0007\u0003\u0002\u0002\u0002RW\u0005",
    "\u0004\u0003\u0002ST\u0007\u0010\u0002\u0002TV\u0005\u0004\u0003\u0002",
    "US\u0003\u0002\u0002\u0002VY\u0003\u0002\u0002\u0002WU\u0003\u0002\u0002",
    "\u0002WX\u0003\u0002\u0002\u0002X\t\u0003\u0002\u0002\u0002YW\u0003",
    "\u0002\u0002\u0002Z\\\u0007\u001a\u0002\u0002[Z\u0003\u0002\u0002\u0002",
    "[\\\u0003\u0002\u0002\u0002\\`\u0003\u0002\u0002\u0002]^\u0005\f\u0007",
    "\u0002^_\u0007\u0018\u0002\u0002_a\u0003\u0002\u0002\u0002`]\u0003\u0002",
    "\u0002\u0002`a\u0003\u0002\u0002\u0002ab\u0003\u0002\u0002\u0002be\u0005",
    "\f\u0007\u0002cd\u0007\u000f\u0002\u0002df\u0005\f\u0007\u0002ec\u0003",
    "\u0002\u0002\u0002ef\u0003\u0002\u0002\u0002f\u000b\u0003\u0002\u0002",
    "\u0002gl\u00075\u0002\u0002hi\u0007\u0011\u0002\u0002ik\u00075\u0002",
    "\u0002jh\u0003\u0002\u0002\u0002kn\u0003\u0002\u0002\u0002lj\u0003\u0002",
    "\u0002\u0002lm\u0003\u0002\u0002\u0002m\r\u0003\u0002\u0002\u0002nl",
    "\u0003\u0002\u0002\u0002op\t\t\u0002\u0002p\u000f\u0003\u0002\u0002",
    "\u0002\u000e\u001d-9?FHNW[`el"].join("");


var atn = new antlr4.atn.ATNDeserializer().deserialize(serializedATN);

var decisionsToDFA = atn.decisionToState.map( function(ds, index) { return new antlr4.dfa.DFA(ds, index); });

var sharedContextCache = new antlr4.PredictionContextCache();

var literalNames = [ null, "'&&'", "'=='", "'>='", "'<='", "'!='", "'<>'", 
                     "'||'", "'<<'", "'>>'", "'&'", "'='", "')'", "':'", 
                     "','", "'.'", "'/'", "'>'", "'<'", "'-'", "'%'", "'('", 
                     "'|'", "'+'", "'?'", "';'", "'*'", "'~'", "'_'" ];

var symbolicNames = [ null, "AND", "EQ", "GT_EQ", "LT_EQ", "NOT_EQ1", "NOT_EQ2", 
                      "OR", "SHIFT_LEFT", "SHIFT_RIGHT", "AMP", "ASSIGN", 
                      "CLOSE_PAREN", "COLON", "COMMA", "DOT", "FORWARD_SLASH", 
                      "GT", "LT", "MINUS", "MOD", "OPEN_PAREN", "PIPE", 
                      "PLUS", "QUESTION_MARK", "SCOL", "STAR", "TILDE", 
                      "UNDER", "K_AND", "K_BETWEEN", "K_FALSE", "K_IN", 
                      "K_IS", "K_ISNULL", "K_LIKE", "K_NOT", "K_NOTNULL", 
                      "K_NULL", "K_OR", "K_TRUE", "NUMERIC_LITERAL", "DOUBLE_QUOTED_STRING", 
                      "DOUBLE_QUOTED_STRING_TEL", "DOUBLE_QUOTED_STRING_SQL", 
                      "SINGLE_QUOTED_STRING", "SINGLE_QUOTED_STRING_TEL", 
                      "SINGLE_QUOTED_STRING_SQL", "SINGLE_LINE_COMMENT", 
                      "MULTILINE_COMMENT", "SPACES", "WORD" ];

var ruleNames =  [ "parseTel", "expr", "fn", "exprList", "taxon", "identifierMultipart", 
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
PqlParser.AND = 1;
PqlParser.EQ = 2;
PqlParser.GT_EQ = 3;
PqlParser.LT_EQ = 4;
PqlParser.NOT_EQ1 = 5;
PqlParser.NOT_EQ2 = 6;
PqlParser.OR = 7;
PqlParser.SHIFT_LEFT = 8;
PqlParser.SHIFT_RIGHT = 9;
PqlParser.AMP = 10;
PqlParser.ASSIGN = 11;
PqlParser.CLOSE_PAREN = 12;
PqlParser.COLON = 13;
PqlParser.COMMA = 14;
PqlParser.DOT = 15;
PqlParser.FORWARD_SLASH = 16;
PqlParser.GT = 17;
PqlParser.LT = 18;
PqlParser.MINUS = 19;
PqlParser.MOD = 20;
PqlParser.OPEN_PAREN = 21;
PqlParser.PIPE = 22;
PqlParser.PLUS = 23;
PqlParser.QUESTION_MARK = 24;
PqlParser.SCOL = 25;
PqlParser.STAR = 26;
PqlParser.TILDE = 27;
PqlParser.UNDER = 28;
PqlParser.K_AND = 29;
PqlParser.K_BETWEEN = 30;
PqlParser.K_FALSE = 31;
PqlParser.K_IN = 32;
PqlParser.K_IS = 33;
PqlParser.K_ISNULL = 34;
PqlParser.K_LIKE = 35;
PqlParser.K_NOT = 36;
PqlParser.K_NOTNULL = 37;
PqlParser.K_NULL = 38;
PqlParser.K_OR = 39;
PqlParser.K_TRUE = 40;
PqlParser.NUMERIC_LITERAL = 41;
PqlParser.DOUBLE_QUOTED_STRING = 42;
PqlParser.DOUBLE_QUOTED_STRING_TEL = 43;
PqlParser.DOUBLE_QUOTED_STRING_SQL = 44;
PqlParser.SINGLE_QUOTED_STRING = 45;
PqlParser.SINGLE_QUOTED_STRING_TEL = 46;
PqlParser.SINGLE_QUOTED_STRING_SQL = 47;
PqlParser.SINGLE_LINE_COMMENT = 48;
PqlParser.MULTILINE_COMMENT = 49;
PqlParser.SPACES = 50;
PqlParser.WORD = 51;

PqlParser.RULE_parseTel = 0;
PqlParser.RULE_expr = 1;
PqlParser.RULE_fn = 2;
PqlParser.RULE_exprList = 3;
PqlParser.RULE_taxon = 4;
PqlParser.RULE_identifierMultipart = 5;
PqlParser.RULE_literalValue = 6;


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
        this.state = 14;
        this.expr(0);
        this.state = 15;
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
    this.operator = null; // Token
    this.is_negated = null; // Token
    this.right_list = null; // ExprListContext
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

ExprContext.prototype.fn = function() {
    return this.getTypedRuleContext(FnContext,0);
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

ExprContext.prototype.K_LIKE = function() {
    return this.getToken(PqlParser.K_LIKE, 0);
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

ExprContext.prototype.K_BETWEEN = function() {
    return this.getToken(PqlParser.K_BETWEEN, 0);
};

ExprContext.prototype.K_IN = function() {
    return this.getToken(PqlParser.K_IN, 0);
};

ExprContext.prototype.exprList = function() {
    return this.getTypedRuleContext(ExprListContext,0);
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
    var _startState = 2;
    this.enterRecursionRule(localctx, 2, PqlParser.RULE_expr, _p);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 27;
        this._errHandler.sync(this);
        var la_ = this._interp.adaptivePredict(this._input,0,this._ctx);
        switch(la_) {
        case 1:
            this.state = 18;
            localctx.unary_operator = this._input.LT(1);
            _la = this._input.LA(1);
            if(!(((((_la - 19)) & ~0x1f) == 0 && ((1 << (_la - 19)) & ((1 << (PqlParser.MINUS - 19)) | (1 << (PqlParser.PLUS - 19)) | (1 << (PqlParser.K_NOT - 19)))) !== 0))) {
                localctx.unary_operator = this._errHandler.recoverInline(this);
            }
            else {
            	this._errHandler.reportMatch(this);
                this.consume();
            }
            this.state = 19;
            localctx.right = this.expr(14);
            break;

        case 2:
            this.state = 20;
            this.match(PqlParser.OPEN_PAREN);
            this.state = 21;
            localctx.inner = this.expr(0);
            this.state = 22;
            this.match(PqlParser.CLOSE_PAREN);
            break;

        case 3:
            this.state = 24;
            this.literalValue();
            break;

        case 4:
            this.state = 25;
            this.fn();
            break;

        case 5:
            this.state = 26;
            this.taxon();
            break;

        }
        this._ctx.stop = this._input.LT(-1);
        this.state = 70;
        this._errHandler.sync(this);
        var _alt = this._interp.adaptivePredict(this._input,5,this._ctx)
        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
            if(_alt===1) {
                if(this._parseListeners!==null) {
                    this.triggerExitRuleEvent();
                }
                _prevctx = localctx;
                this.state = 68;
                this._errHandler.sync(this);
                var la_ = this._interp.adaptivePredict(this._input,4,this._ctx);
                switch(la_) {
                case 1:
                    localctx = new ExprContext(this, _parentctx, _parentState);
                    localctx.left = _prevctx;
                    this.pushNewRecursionContext(localctx, _startState, PqlParser.RULE_expr);
                    this.state = 29;
                    if (!( this.precpred(this._ctx, 13))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 13)");
                    }
                    this.state = 30;
                    localctx.operator = this._input.LT(1);
                    _la = this._input.LA(1);
                    if(!((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << PqlParser.FORWARD_SLASH) | (1 << PqlParser.MOD) | (1 << PqlParser.STAR))) !== 0))) {
                        localctx.operator = this._errHandler.recoverInline(this);
                    }
                    else {
                    	this._errHandler.reportMatch(this);
                        this.consume();
                    }
                    this.state = 31;
                    localctx.right = this.expr(14);
                    break;

                case 2:
                    localctx = new ExprContext(this, _parentctx, _parentState);
                    localctx.left = _prevctx;
                    this.pushNewRecursionContext(localctx, _startState, PqlParser.RULE_expr);
                    this.state = 32;
                    if (!( this.precpred(this._ctx, 12))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 12)");
                    }
                    this.state = 33;
                    localctx.operator = this._input.LT(1);
                    _la = this._input.LA(1);
                    if(!(_la===PqlParser.MINUS || _la===PqlParser.PLUS)) {
                        localctx.operator = this._errHandler.recoverInline(this);
                    }
                    else {
                    	this._errHandler.reportMatch(this);
                        this.consume();
                    }
                    this.state = 34;
                    localctx.right = this.expr(13);
                    break;

                case 3:
                    localctx = new ExprContext(this, _parentctx, _parentState);
                    localctx.left = _prevctx;
                    this.pushNewRecursionContext(localctx, _startState, PqlParser.RULE_expr);
                    this.state = 35;
                    if (!( this.precpred(this._ctx, 11))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 11)");
                    }
                    this.state = 36;
                    localctx.operator = this._input.LT(1);
                    _la = this._input.LA(1);
                    if(!((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << PqlParser.GT_EQ) | (1 << PqlParser.LT_EQ) | (1 << PqlParser.GT) | (1 << PqlParser.LT))) !== 0))) {
                        localctx.operator = this._errHandler.recoverInline(this);
                    }
                    else {
                    	this._errHandler.reportMatch(this);
                        this.consume();
                    }
                    this.state = 37;
                    localctx.right = this.expr(12);
                    break;

                case 4:
                    localctx = new ExprContext(this, _parentctx, _parentState);
                    localctx.left = _prevctx;
                    this.pushNewRecursionContext(localctx, _startState, PqlParser.RULE_expr);
                    this.state = 38;
                    if (!( this.precpred(this._ctx, 10))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 10)");
                    }
                    this.state = 39;
                    localctx.operator = this._input.LT(1);
                    _la = this._input.LA(1);
                    if(!(((((_la - 2)) & ~0x1f) == 0 && ((1 << (_la - 2)) & ((1 << (PqlParser.EQ - 2)) | (1 << (PqlParser.NOT_EQ1 - 2)) | (1 << (PqlParser.NOT_EQ2 - 2)) | (1 << (PqlParser.ASSIGN - 2)) | (1 << (PqlParser.K_IS - 2)))) !== 0))) {
                        localctx.operator = this._errHandler.recoverInline(this);
                    }
                    else {
                    	this._errHandler.reportMatch(this);
                        this.consume();
                    }
                    this.state = 40;
                    localctx.right = this.expr(11);
                    break;

                case 5:
                    localctx = new ExprContext(this, _parentctx, _parentState);
                    localctx.left = _prevctx;
                    this.pushNewRecursionContext(localctx, _startState, PqlParser.RULE_expr);
                    this.state = 41;
                    if (!( this.precpred(this._ctx, 9))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 9)");
                    }
                    this.state = 43;
                    this._errHandler.sync(this);
                    _la = this._input.LA(1);
                    if(_la===PqlParser.K_NOT) {
                        this.state = 42;
                        localctx.is_negated = this.match(PqlParser.K_NOT);
                    }

                    this.state = 45;
                    localctx.operator = this.match(PqlParser.K_LIKE);
                    this.state = 46;
                    localctx.right = this.expr(10);
                    break;

                case 6:
                    localctx = new ExprContext(this, _parentctx, _parentState);
                    localctx.left = _prevctx;
                    this.pushNewRecursionContext(localctx, _startState, PqlParser.RULE_expr);
                    this.state = 47;
                    if (!( this.precpred(this._ctx, 7))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 7)");
                    }
                    this.state = 48;
                    localctx.operator = this._input.LT(1);
                    _la = this._input.LA(1);
                    if(!(_la===PqlParser.AND || _la===PqlParser.K_AND)) {
                        localctx.operator = this._errHandler.recoverInline(this);
                    }
                    else {
                    	this._errHandler.reportMatch(this);
                        this.consume();
                    }
                    this.state = 49;
                    localctx.right = this.expr(8);
                    break;

                case 7:
                    localctx = new ExprContext(this, _parentctx, _parentState);
                    localctx.left = _prevctx;
                    this.pushNewRecursionContext(localctx, _startState, PqlParser.RULE_expr);
                    this.state = 50;
                    if (!( this.precpred(this._ctx, 6))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 6)");
                    }
                    this.state = 51;
                    localctx.operator = this._input.LT(1);
                    _la = this._input.LA(1);
                    if(!(_la===PqlParser.OR || _la===PqlParser.K_OR)) {
                        localctx.operator = this._errHandler.recoverInline(this);
                    }
                    else {
                    	this._errHandler.reportMatch(this);
                        this.consume();
                    }
                    this.state = 52;
                    localctx.right = this.expr(7);
                    break;

                case 8:
                    localctx = new ExprContext(this, _parentctx, _parentState);
                    localctx.left = _prevctx;
                    this.pushNewRecursionContext(localctx, _startState, PqlParser.RULE_expr);
                    this.state = 53;
                    if (!( this.precpred(this._ctx, 5))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 5)");
                    }
                    this.state = 55;
                    this._errHandler.sync(this);
                    _la = this._input.LA(1);
                    if(_la===PqlParser.K_NOT) {
                        this.state = 54;
                        localctx.is_negated = this.match(PqlParser.K_NOT);
                    }

                    this.state = 57;
                    localctx.operator = this.match(PqlParser.K_BETWEEN);
                    this.state = 58;
                    localctx.right = this.expr(6);
                    break;

                case 9:
                    localctx = new ExprContext(this, _parentctx, _parentState);
                    localctx.left = _prevctx;
                    this.pushNewRecursionContext(localctx, _startState, PqlParser.RULE_expr);
                    this.state = 59;
                    if (!( this.precpred(this._ctx, 8))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 8)");
                    }
                    this.state = 61;
                    this._errHandler.sync(this);
                    _la = this._input.LA(1);
                    if(_la===PqlParser.K_NOT) {
                        this.state = 60;
                        localctx.is_negated = this.match(PqlParser.K_NOT);
                    }

                    this.state = 63;
                    localctx.operator = this.match(PqlParser.K_IN);
                    this.state = 64;
                    this.match(PqlParser.OPEN_PAREN);
                    this.state = 65;
                    localctx.right_list = this.exprList();
                    this.state = 66;
                    this.match(PqlParser.CLOSE_PAREN);
                    break;

                } 
            }
            this.state = 72;
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


function FnContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = PqlParser.RULE_fn;
    this.function_name = null; // IdentifierMultipartContext
    this.arguments = null; // ExprListContext
    return this;
}

FnContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
FnContext.prototype.constructor = FnContext;

FnContext.prototype.OPEN_PAREN = function() {
    return this.getToken(PqlParser.OPEN_PAREN, 0);
};

FnContext.prototype.CLOSE_PAREN = function() {
    return this.getToken(PqlParser.CLOSE_PAREN, 0);
};

FnContext.prototype.identifierMultipart = function() {
    return this.getTypedRuleContext(IdentifierMultipartContext,0);
};

FnContext.prototype.exprList = function() {
    return this.getTypedRuleContext(ExprListContext,0);
};

FnContext.prototype.enterRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.enterFn(this);
	}
};

FnContext.prototype.exitRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.exitFn(this);
	}
};

FnContext.prototype.accept = function(visitor) {
    if ( visitor instanceof PqlParserVisitor ) {
        return visitor.visitFn(this);
    } else {
        return visitor.visitChildren(this);
    }
};




PqlParser.FnContext = FnContext;

PqlParser.prototype.fn = function() {

    var localctx = new FnContext(this, this._ctx, this.state);
    this.enterRule(localctx, 4, PqlParser.RULE_fn);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 73;
        localctx.function_name = this.identifierMultipart();
        this.state = 74;
        this.match(PqlParser.OPEN_PAREN);
        this.state = 76;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        if((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << PqlParser.MINUS) | (1 << PqlParser.OPEN_PAREN) | (1 << PqlParser.PLUS) | (1 << PqlParser.QUESTION_MARK) | (1 << PqlParser.K_FALSE))) !== 0) || ((((_la - 36)) & ~0x1f) == 0 && ((1 << (_la - 36)) & ((1 << (PqlParser.K_NOT - 36)) | (1 << (PqlParser.K_NULL - 36)) | (1 << (PqlParser.K_TRUE - 36)) | (1 << (PqlParser.NUMERIC_LITERAL - 36)) | (1 << (PqlParser.DOUBLE_QUOTED_STRING - 36)) | (1 << (PqlParser.SINGLE_QUOTED_STRING - 36)) | (1 << (PqlParser.WORD - 36)))) !== 0)) {
            this.state = 75;
            localctx.arguments = this.exprList();
        }

        this.state = 78;
        this.match(PqlParser.CLOSE_PAREN);
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


function ExprListContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = PqlParser.RULE_exprList;
    return this;
}

ExprListContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
ExprListContext.prototype.constructor = ExprListContext;

ExprListContext.prototype.expr = function(i) {
    if(i===undefined) {
        i = null;
    }
    if(i===null) {
        return this.getTypedRuleContexts(ExprContext);
    } else {
        return this.getTypedRuleContext(ExprContext,i);
    }
};

ExprListContext.prototype.COMMA = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(PqlParser.COMMA);
    } else {
        return this.getToken(PqlParser.COMMA, i);
    }
};


ExprListContext.prototype.enterRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.enterExprList(this);
	}
};

ExprListContext.prototype.exitRule = function(listener) {
    if(listener instanceof PqlParserListener ) {
        listener.exitExprList(this);
	}
};

ExprListContext.prototype.accept = function(visitor) {
    if ( visitor instanceof PqlParserVisitor ) {
        return visitor.visitExprList(this);
    } else {
        return visitor.visitChildren(this);
    }
};




PqlParser.ExprListContext = ExprListContext;

PqlParser.prototype.exprList = function() {

    var localctx = new ExprListContext(this, this._ctx, this.state);
    this.enterRule(localctx, 6, PqlParser.RULE_exprList);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 80;
        this.expr(0);
        this.state = 85;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        while(_la===PqlParser.COMMA) {
            this.state = 81;
            this.match(PqlParser.COMMA);
            this.state = 82;
            this.expr(0);
            this.state = 87;
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
    this.is_optional = null; // Token
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

TaxonContext.prototype.PIPE = function() {
    return this.getToken(PqlParser.PIPE, 0);
};

TaxonContext.prototype.COLON = function() {
    return this.getToken(PqlParser.COLON, 0);
};

TaxonContext.prototype.QUESTION_MARK = function() {
    return this.getToken(PqlParser.QUESTION_MARK, 0);
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
    this.enterRule(localctx, 8, PqlParser.RULE_taxon);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 89;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        if(_la===PqlParser.QUESTION_MARK) {
            this.state = 88;
            localctx.is_optional = this.match(PqlParser.QUESTION_MARK);
        }

        this.state = 94;
        this._errHandler.sync(this);
        var la_ = this._interp.adaptivePredict(this._input,9,this._ctx);
        if(la_===1) {
            this.state = 91;
            localctx.namespace = this.identifierMultipart();
            this.state = 92;
            this.match(PqlParser.PIPE);

        }
        this.state = 96;
        localctx.slug = this.identifierMultipart();
        this.state = 99;
        this._errHandler.sync(this);
        var la_ = this._interp.adaptivePredict(this._input,10,this._ctx);
        if(la_===1) {
            this.state = 97;
            this.match(PqlParser.COLON);
            this.state = 98;
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
    this.enterRule(localctx, 10, PqlParser.RULE_identifierMultipart);
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 101;
        this.match(PqlParser.WORD);
        this.state = 106;
        this._errHandler.sync(this);
        var _alt = this._interp.adaptivePredict(this._input,11,this._ctx)
        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
            if(_alt===1) {
                this.state = 102;
                this.match(PqlParser.DOT);
                this.state = 103;
                this.match(PqlParser.WORD); 
            }
            this.state = 108;
            this._errHandler.sync(this);
            _alt = this._interp.adaptivePredict(this._input,11,this._ctx);
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
    this.enterRule(localctx, 12, PqlParser.RULE_literalValue);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 109;
        _la = this._input.LA(1);
        if(!(((((_la - 31)) & ~0x1f) == 0 && ((1 << (_la - 31)) & ((1 << (PqlParser.K_FALSE - 31)) | (1 << (PqlParser.K_NULL - 31)) | (1 << (PqlParser.K_TRUE - 31)) | (1 << (PqlParser.NUMERIC_LITERAL - 31)) | (1 << (PqlParser.DOUBLE_QUOTED_STRING - 31)) | (1 << (PqlParser.SINGLE_QUOTED_STRING - 31)))) !== 0))) {
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
	case 1:
			return this.expr_sempred(localctx, predIndex);
    default:
        throw "No predicate with index:" + ruleIndex;
   }
};

PqlParser.prototype.expr_sempred = function(localctx, predIndex) {
	switch(predIndex) {
		case 0:
			return this.precpred(this._ctx, 13);
		case 1:
			return this.precpred(this._ctx, 12);
		case 2:
			return this.precpred(this._ctx, 11);
		case 3:
			return this.precpred(this._ctx, 10);
		case 4:
			return this.precpred(this._ctx, 9);
		case 5:
			return this.precpred(this._ctx, 7);
		case 6:
			return this.precpred(this._ctx, 6);
		case 7:
			return this.precpred(this._ctx, 5);
		case 8:
			return this.precpred(this._ctx, 8);
		default:
			throw "No predicate with index:" + predIndex;
	}
};


exports.PqlParser = PqlParser;

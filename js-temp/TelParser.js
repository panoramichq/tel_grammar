// Generated from grammar/TelParser.g4 by ANTLR 4.8
// jshint ignore: start
var antlr4 = require('antlr4/index');
var TelParserListener = require('./TelParserListener').TelParserListener;
var TelParserVisitor = require('./TelParserVisitor').TelParserVisitor;

var grammarFileName = "TelParser.g4";


var serializedATN = ["\u0003\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964",
    "\u0003 P\u0004\u0002\t\u0002\u0004\u0003\t\u0003\u0004\u0004\t\u0004",
    "\u0004\u0005\t\u0005\u0004\u0006\t\u0006\u0003\u0002\u0003\u0002\u0003",
    "\u0002\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0005\u0003\u0014",
    "\n\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0003",
    "\u0003\u0003\u0005\u0003\"\n\u0003\u0003\u0003\u0007\u0003%\n\u0003",
    "\f\u0003\u000e\u0003(\u000b\u0003\u0003\u0004\u0003\u0004\u0003\u0004",
    "\u0003\u0004\u0003\u0004\u0003\u0004\u0003\u0004\u0003\u0004\u0003\u0004",
    "\u0003\u0004\u0005\u00044\n\u0004\u0003\u0005\u0003\u0005\u0003\u0005",
    "\u0005\u00059\n\u0005\u0003\u0005\u0003\u0005\u0007\u0005=\n\u0005\f",
    "\u0005\u000e\u0005@\u000b\u0005\u0003\u0005\u0003\u0005\u0003\u0006",
    "\u0005\u0006E\n\u0006\u0003\u0006\u0003\u0006\u0003\u0006\u0005\u0006",
    "J\n\u0006\u0003\u0006\u0003\u0006\u0005\u0006N\n\u0006\u0003\u0006\u0002",
    "\u0003\u0004\u0007\u0002\u0004\u0006\b\n\u0002\u0007\u0003\u0002\u001c",
    "\u001d\u0003\u0002\u001a\u001b\u0003\u0002\u0012\u0019\u0003\u0002\u0003",
    "\u0004\u0003\u0002\u0005\u0006\u0002[\u0002\f\u0003\u0002\u0002\u0002",
    "\u0004\u0013\u0003\u0002\u0002\u0002\u00063\u0003\u0002\u0002\u0002",
    "\b5\u0003\u0002\u0002\u0002\nD\u0003\u0002\u0002\u0002\f\r\u0005\u0004",
    "\u0003\u0002\r\u000e\u0007\u0002\u0002\u0003\u000e\u0003\u0003\u0002",
    "\u0002\u0002\u000f\u0010\b\u0003\u0001\u0002\u0010\u0011\u0007\u0007",
    "\u0002\u0002\u0011\u0014\u0005\u0004\u0003\b\u0012\u0014\u0005\u0006",
    "\u0004\u0002\u0013\u000f\u0003\u0002\u0002\u0002\u0013\u0012\u0003\u0002",
    "\u0002\u0002\u0014&\u0003\u0002\u0002\u0002\u0015\u0016\f\u0007\u0002",
    "\u0002\u0016\u0017\t\u0002\u0002\u0002\u0017%\u0005\u0004\u0003\b\u0018",
    "\u0019\f\u0006\u0002\u0002\u0019\u001a\t\u0003\u0002\u0002\u001a%\u0005",
    "\u0004\u0003\u0007\u001b\u001c\f\u0005\u0002\u0002\u001c\u001d\t\u0004",
    "\u0002\u0002\u001d%\u0005\u0004\u0003\u0006\u001e\u001f\f\u0004\u0002",
    "\u0002\u001f!\u0007\b\u0002\u0002 \"\u0007\u0007\u0002\u0002! \u0003",
    "\u0002\u0002\u0002!\"\u0003\u0002\u0002\u0002\"#\u0003\u0002\u0002\u0002",
    "#%\u0007\t\u0002\u0002$\u0015\u0003\u0002\u0002\u0002$\u0018\u0003\u0002",
    "\u0002\u0002$\u001b\u0003\u0002\u0002\u0002$\u001e\u0003\u0002\u0002",
    "\u0002%(\u0003\u0002\u0002\u0002&$\u0003\u0002\u0002\u0002&\'\u0003",
    "\u0002\u0002\u0002\'\u0005\u0003\u0002\u0002\u0002(&\u0003\u0002\u0002",
    "\u0002)*\u0007\r\u0002\u0002*+\u0005\u0004\u0003\u0002+,\u0007\u000e",
    "\u0002\u0002,4\u0003\u0002\u0002\u0002-4\t\u0005\u0002\u0002.4\t\u0006",
    "\u0002\u0002/4\u0007\f\u0002\u000204\u0007\u000b\u0002\u000214\u0005",
    "\b\u0005\u000224\u0005\n\u0006\u00023)\u0003\u0002\u0002\u00023-\u0003",
    "\u0002\u0002\u00023.\u0003\u0002\u0002\u00023/\u0003\u0002\u0002\u0002",
    "30\u0003\u0002\u0002\u000231\u0003\u0002\u0002\u000232\u0003\u0002\u0002",
    "\u00024\u0007\u0003\u0002\u0002\u000256\u0007\n\u0002\u000268\u0007",
    "\r\u0002\u000279\u0005\u0004\u0003\u000287\u0003\u0002\u0002\u00028",
    "9\u0003\u0002\u0002\u00029>\u0003\u0002\u0002\u0002:;\u0007\u0011\u0002",
    "\u0002;=\u0005\u0004\u0003\u0002<:\u0003\u0002\u0002\u0002=@\u0003\u0002",
    "\u0002\u0002><\u0003\u0002\u0002\u0002>?\u0003\u0002\u0002\u0002?A\u0003",
    "\u0002\u0002\u0002@>\u0003\u0002\u0002\u0002AB\u0007\u000e\u0002\u0002",
    "B\t\u0003\u0002\u0002\u0002CE\u0007\u001e\u0002\u0002DC\u0003\u0002",
    "\u0002\u0002DE\u0003\u0002\u0002\u0002EF\u0003\u0002\u0002\u0002FI\u0007",
    "\n\u0002\u0002GH\u0007\u000f\u0002\u0002HJ\u0007\n\u0002\u0002IG\u0003",
    "\u0002\u0002\u0002IJ\u0003\u0002\u0002\u0002JM\u0003\u0002\u0002\u0002",
    "KL\u0007\u0010\u0002\u0002LN\u0007\n\u0002\u0002MK\u0003\u0002\u0002",
    "\u0002MN\u0003\u0002\u0002\u0002N\u000b\u0003\u0002\u0002\u0002\f\u0013",
    "!$&38>DIM"].join("");


var atn = new antlr4.atn.ATNDeserializer().deserialize(serializedATN);

var decisionsToDFA = atn.decisionToState.map( function(ds, index) { return new antlr4.dfa.DFA(ds, index); });

var sharedContextCache = new antlr4.PredictionContextCache();

var literalNames = [ null, null, null, null, null, null, null, null, null, 
                     null, null, "'('", "')'", "'|'", "':'", "','", "'||'", 
                     "'&&'", "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", 
                     "'+'", "'-'", "'*'", "'/'", "'?'" ];

var symbolicNames = [ null, "INT", "REAL", "TRUE", "FALSE", "NOT", "KW_IS", 
                      "KW_NULL", "WORD", "STRING_CONSTANT", "SINGLE_QUOTED_ELEMENT", 
                      "L_BRACKET", "R_BRACKET", "TAXON_NAMESPACE_DELIMITER", 
                      "TAXON_TAG_DELIMITER", "FN_PARAMETER_DELIMITER", "OR", 
                      "AND", "EQ", "NEQ", "GT", "LT", "GTEQ", "LTEQ", "PLUS", 
                      "MINUS", "MULT", "DIV", "OPTIONAL_TAXON_OPERATOR", 
                      "SINGLE_LINE_COMMENT", "WS" ];

var ruleNames =  [ "parse", "expr", "atom", "fn", "taxon" ];

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
TelParser.INT = 1;
TelParser.REAL = 2;
TelParser.TRUE = 3;
TelParser.FALSE = 4;
TelParser.NOT = 5;
TelParser.KW_IS = 6;
TelParser.KW_NULL = 7;
TelParser.WORD = 8;
TelParser.STRING_CONSTANT = 9;
TelParser.SINGLE_QUOTED_ELEMENT = 10;
TelParser.L_BRACKET = 11;
TelParser.R_BRACKET = 12;
TelParser.TAXON_NAMESPACE_DELIMITER = 13;
TelParser.TAXON_TAG_DELIMITER = 14;
TelParser.FN_PARAMETER_DELIMITER = 15;
TelParser.OR = 16;
TelParser.AND = 17;
TelParser.EQ = 18;
TelParser.NEQ = 19;
TelParser.GT = 20;
TelParser.LT = 21;
TelParser.GTEQ = 22;
TelParser.LTEQ = 23;
TelParser.PLUS = 24;
TelParser.MINUS = 25;
TelParser.MULT = 26;
TelParser.DIV = 27;
TelParser.OPTIONAL_TAXON_OPERATOR = 28;
TelParser.SINGLE_LINE_COMMENT = 29;
TelParser.WS = 30;

TelParser.RULE_parse = 0;
TelParser.RULE_expr = 1;
TelParser.RULE_atom = 2;
TelParser.RULE_fn = 3;
TelParser.RULE_taxon = 4;


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
        this.state = 10;
        this.expr(0);
        this.state = 11;
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
    return this;
}

ExprContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
ExprContext.prototype.constructor = ExprContext;


 
ExprContext.prototype.copyFrom = function(ctx) {
    antlr4.ParserRuleContext.prototype.copyFrom.call(this, ctx);
};

function NullTestExprContext(parser, ctx) {
	ExprContext.call(this, parser);
    ExprContext.prototype.copyFrom.call(this, ctx);
    return this;
}

NullTestExprContext.prototype = Object.create(ExprContext.prototype);
NullTestExprContext.prototype.constructor = NullTestExprContext;

TelParser.NullTestExprContext = NullTestExprContext;

NullTestExprContext.prototype.expr = function() {
    return this.getTypedRuleContext(ExprContext,0);
};

NullTestExprContext.prototype.KW_IS = function() {
    return this.getToken(TelParser.KW_IS, 0);
};

NullTestExprContext.prototype.KW_NULL = function() {
    return this.getToken(TelParser.KW_NULL, 0);
};

NullTestExprContext.prototype.NOT = function() {
    return this.getToken(TelParser.NOT, 0);
};
NullTestExprContext.prototype.enterRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.enterNullTestExpr(this);
	}
};

NullTestExprContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.exitNullTestExpr(this);
	}
};

NullTestExprContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelParserVisitor ) {
        return visitor.visitNullTestExpr(this);
    } else {
        return visitor.visitChildren(this);
    }
};


function NotExprContext(parser, ctx) {
	ExprContext.call(this, parser);
    ExprContext.prototype.copyFrom.call(this, ctx);
    return this;
}

NotExprContext.prototype = Object.create(ExprContext.prototype);
NotExprContext.prototype.constructor = NotExprContext;

TelParser.NotExprContext = NotExprContext;

NotExprContext.prototype.NOT = function() {
    return this.getToken(TelParser.NOT, 0);
};

NotExprContext.prototype.expr = function() {
    return this.getTypedRuleContext(ExprContext,0);
};
NotExprContext.prototype.enterRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.enterNotExpr(this);
	}
};

NotExprContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.exitNotExpr(this);
	}
};

NotExprContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelParserVisitor ) {
        return visitor.visitNotExpr(this);
    } else {
        return visitor.visitChildren(this);
    }
};


function LogicalExprContext(parser, ctx) {
	ExprContext.call(this, parser);
    this.op = null; // Token;
    ExprContext.prototype.copyFrom.call(this, ctx);
    return this;
}

LogicalExprContext.prototype = Object.create(ExprContext.prototype);
LogicalExprContext.prototype.constructor = LogicalExprContext;

TelParser.LogicalExprContext = LogicalExprContext;

LogicalExprContext.prototype.expr = function(i) {
    if(i===undefined) {
        i = null;
    }
    if(i===null) {
        return this.getTypedRuleContexts(ExprContext);
    } else {
        return this.getTypedRuleContext(ExprContext,i);
    }
};

LogicalExprContext.prototype.OR = function() {
    return this.getToken(TelParser.OR, 0);
};

LogicalExprContext.prototype.AND = function() {
    return this.getToken(TelParser.AND, 0);
};

LogicalExprContext.prototype.EQ = function() {
    return this.getToken(TelParser.EQ, 0);
};

LogicalExprContext.prototype.NEQ = function() {
    return this.getToken(TelParser.NEQ, 0);
};

LogicalExprContext.prototype.GT = function() {
    return this.getToken(TelParser.GT, 0);
};

LogicalExprContext.prototype.LT = function() {
    return this.getToken(TelParser.LT, 0);
};

LogicalExprContext.prototype.GTEQ = function() {
    return this.getToken(TelParser.GTEQ, 0);
};

LogicalExprContext.prototype.LTEQ = function() {
    return this.getToken(TelParser.LTEQ, 0);
};
LogicalExprContext.prototype.enterRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.enterLogicalExpr(this);
	}
};

LogicalExprContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.exitLogicalExpr(this);
	}
};

LogicalExprContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelParserVisitor ) {
        return visitor.visitLogicalExpr(this);
    } else {
        return visitor.visitChildren(this);
    }
};


function MultiplicationExprContext(parser, ctx) {
	ExprContext.call(this, parser);
    this.op = null; // Token;
    ExprContext.prototype.copyFrom.call(this, ctx);
    return this;
}

MultiplicationExprContext.prototype = Object.create(ExprContext.prototype);
MultiplicationExprContext.prototype.constructor = MultiplicationExprContext;

TelParser.MultiplicationExprContext = MultiplicationExprContext;

MultiplicationExprContext.prototype.expr = function(i) {
    if(i===undefined) {
        i = null;
    }
    if(i===null) {
        return this.getTypedRuleContexts(ExprContext);
    } else {
        return this.getTypedRuleContext(ExprContext,i);
    }
};

MultiplicationExprContext.prototype.MULT = function() {
    return this.getToken(TelParser.MULT, 0);
};

MultiplicationExprContext.prototype.DIV = function() {
    return this.getToken(TelParser.DIV, 0);
};
MultiplicationExprContext.prototype.enterRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.enterMultiplicationExpr(this);
	}
};

MultiplicationExprContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.exitMultiplicationExpr(this);
	}
};

MultiplicationExprContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelParserVisitor ) {
        return visitor.visitMultiplicationExpr(this);
    } else {
        return visitor.visitChildren(this);
    }
};


function AtomExprContext(parser, ctx) {
	ExprContext.call(this, parser);
    ExprContext.prototype.copyFrom.call(this, ctx);
    return this;
}

AtomExprContext.prototype = Object.create(ExprContext.prototype);
AtomExprContext.prototype.constructor = AtomExprContext;

TelParser.AtomExprContext = AtomExprContext;

AtomExprContext.prototype.atom = function() {
    return this.getTypedRuleContext(AtomContext,0);
};
AtomExprContext.prototype.enterRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.enterAtomExpr(this);
	}
};

AtomExprContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.exitAtomExpr(this);
	}
};

AtomExprContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelParserVisitor ) {
        return visitor.visitAtomExpr(this);
    } else {
        return visitor.visitChildren(this);
    }
};


function AdditiveExprContext(parser, ctx) {
	ExprContext.call(this, parser);
    this.op = null; // Token;
    ExprContext.prototype.copyFrom.call(this, ctx);
    return this;
}

AdditiveExprContext.prototype = Object.create(ExprContext.prototype);
AdditiveExprContext.prototype.constructor = AdditiveExprContext;

TelParser.AdditiveExprContext = AdditiveExprContext;

AdditiveExprContext.prototype.expr = function(i) {
    if(i===undefined) {
        i = null;
    }
    if(i===null) {
        return this.getTypedRuleContexts(ExprContext);
    } else {
        return this.getTypedRuleContext(ExprContext,i);
    }
};

AdditiveExprContext.prototype.PLUS = function() {
    return this.getToken(TelParser.PLUS, 0);
};

AdditiveExprContext.prototype.MINUS = function() {
    return this.getToken(TelParser.MINUS, 0);
};
AdditiveExprContext.prototype.enterRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.enterAdditiveExpr(this);
	}
};

AdditiveExprContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.exitAdditiveExpr(this);
	}
};

AdditiveExprContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelParserVisitor ) {
        return visitor.visitAdditiveExpr(this);
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
        this.state = 17;
        this._errHandler.sync(this);
        switch(this._input.LA(1)) {
        case TelParser.NOT:
            localctx = new NotExprContext(this, localctx);
            this._ctx = localctx;
            _prevctx = localctx;

            this.state = 14;
            this.match(TelParser.NOT);
            this.state = 15;
            this.expr(6);
            break;
        case TelParser.INT:
        case TelParser.REAL:
        case TelParser.TRUE:
        case TelParser.FALSE:
        case TelParser.WORD:
        case TelParser.STRING_CONSTANT:
        case TelParser.SINGLE_QUOTED_ELEMENT:
        case TelParser.L_BRACKET:
        case TelParser.OPTIONAL_TAXON_OPERATOR:
            localctx = new AtomExprContext(this, localctx);
            this._ctx = localctx;
            _prevctx = localctx;
            this.state = 16;
            this.atom();
            break;
        default:
            throw new antlr4.error.NoViableAltException(this);
        }
        this._ctx.stop = this._input.LT(-1);
        this.state = 36;
        this._errHandler.sync(this);
        var _alt = this._interp.adaptivePredict(this._input,3,this._ctx)
        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
            if(_alt===1) {
                if(this._parseListeners!==null) {
                    this.triggerExitRuleEvent();
                }
                _prevctx = localctx;
                this.state = 34;
                this._errHandler.sync(this);
                var la_ = this._interp.adaptivePredict(this._input,2,this._ctx);
                switch(la_) {
                case 1:
                    localctx = new MultiplicationExprContext(this, new ExprContext(this, _parentctx, _parentState));
                    this.pushNewRecursionContext(localctx, _startState, TelParser.RULE_expr);
                    this.state = 19;
                    if (!( this.precpred(this._ctx, 5))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 5)");
                    }
                    this.state = 20;
                    localctx.op = this._input.LT(1);
                    _la = this._input.LA(1);
                    if(!(_la===TelParser.MULT || _la===TelParser.DIV)) {
                        localctx.op = this._errHandler.recoverInline(this);
                    }
                    else {
                    	this._errHandler.reportMatch(this);
                        this.consume();
                    }
                    this.state = 21;
                    this.expr(6);
                    break;

                case 2:
                    localctx = new AdditiveExprContext(this, new ExprContext(this, _parentctx, _parentState));
                    this.pushNewRecursionContext(localctx, _startState, TelParser.RULE_expr);
                    this.state = 22;
                    if (!( this.precpred(this._ctx, 4))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 4)");
                    }
                    this.state = 23;
                    localctx.op = this._input.LT(1);
                    _la = this._input.LA(1);
                    if(!(_la===TelParser.PLUS || _la===TelParser.MINUS)) {
                        localctx.op = this._errHandler.recoverInline(this);
                    }
                    else {
                    	this._errHandler.reportMatch(this);
                        this.consume();
                    }
                    this.state = 24;
                    this.expr(5);
                    break;

                case 3:
                    localctx = new LogicalExprContext(this, new ExprContext(this, _parentctx, _parentState));
                    this.pushNewRecursionContext(localctx, _startState, TelParser.RULE_expr);
                    this.state = 25;
                    if (!( this.precpred(this._ctx, 3))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
                    }
                    this.state = 26;
                    localctx.op = this._input.LT(1);
                    _la = this._input.LA(1);
                    if(!((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << TelParser.OR) | (1 << TelParser.AND) | (1 << TelParser.EQ) | (1 << TelParser.NEQ) | (1 << TelParser.GT) | (1 << TelParser.LT) | (1 << TelParser.GTEQ) | (1 << TelParser.LTEQ))) !== 0))) {
                        localctx.op = this._errHandler.recoverInline(this);
                    }
                    else {
                    	this._errHandler.reportMatch(this);
                        this.consume();
                    }
                    this.state = 27;
                    this.expr(4);
                    break;

                case 4:
                    localctx = new NullTestExprContext(this, new ExprContext(this, _parentctx, _parentState));
                    this.pushNewRecursionContext(localctx, _startState, TelParser.RULE_expr);
                    this.state = 28;
                    if (!( this.precpred(this._ctx, 2))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 2)");
                    }
                    this.state = 29;
                    this.match(TelParser.KW_IS);
                    this.state = 31;
                    this._errHandler.sync(this);
                    _la = this._input.LA(1);
                    if(_la===TelParser.NOT) {
                        this.state = 30;
                        this.match(TelParser.NOT);
                    }

                    this.state = 33;
                    this.match(TelParser.KW_NULL);
                    break;

                } 
            }
            this.state = 38;
            this._errHandler.sync(this);
            _alt = this._interp.adaptivePredict(this._input,3,this._ctx);
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


function AtomContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = TelParser.RULE_atom;
    return this;
}

AtomContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
AtomContext.prototype.constructor = AtomContext;


 
AtomContext.prototype.copyFrom = function(ctx) {
    antlr4.ParserRuleContext.prototype.copyFrom.call(this, ctx);
};


function FnExprContext(parser, ctx) {
	AtomContext.call(this, parser);
    AtomContext.prototype.copyFrom.call(this, ctx);
    return this;
}

FnExprContext.prototype = Object.create(AtomContext.prototype);
FnExprContext.prototype.constructor = FnExprContext;

TelParser.FnExprContext = FnExprContext;

FnExprContext.prototype.fn = function() {
    return this.getTypedRuleContext(FnContext,0);
};
FnExprContext.prototype.enterRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.enterFnExpr(this);
	}
};

FnExprContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.exitFnExpr(this);
	}
};

FnExprContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelParserVisitor ) {
        return visitor.visitFnExpr(this);
    } else {
        return visitor.visitChildren(this);
    }
};


function TaxonSlugAtomContext(parser, ctx) {
	AtomContext.call(this, parser);
    AtomContext.prototype.copyFrom.call(this, ctx);
    return this;
}

TaxonSlugAtomContext.prototype = Object.create(AtomContext.prototype);
TaxonSlugAtomContext.prototype.constructor = TaxonSlugAtomContext;

TelParser.TaxonSlugAtomContext = TaxonSlugAtomContext;

TaxonSlugAtomContext.prototype.taxon = function() {
    return this.getTypedRuleContext(TaxonContext,0);
};
TaxonSlugAtomContext.prototype.enterRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.enterTaxonSlugAtom(this);
	}
};

TaxonSlugAtomContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.exitTaxonSlugAtom(this);
	}
};

TaxonSlugAtomContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelParserVisitor ) {
        return visitor.visitTaxonSlugAtom(this);
    } else {
        return visitor.visitChildren(this);
    }
};


function BooleanAtomContext(parser, ctx) {
	AtomContext.call(this, parser);
    AtomContext.prototype.copyFrom.call(this, ctx);
    return this;
}

BooleanAtomContext.prototype = Object.create(AtomContext.prototype);
BooleanAtomContext.prototype.constructor = BooleanAtomContext;

TelParser.BooleanAtomContext = BooleanAtomContext;

BooleanAtomContext.prototype.TRUE = function() {
    return this.getToken(TelParser.TRUE, 0);
};

BooleanAtomContext.prototype.FALSE = function() {
    return this.getToken(TelParser.FALSE, 0);
};
BooleanAtomContext.prototype.enterRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.enterBooleanAtom(this);
	}
};

BooleanAtomContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.exitBooleanAtom(this);
	}
};

BooleanAtomContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelParserVisitor ) {
        return visitor.visitBooleanAtom(this);
    } else {
        return visitor.visitChildren(this);
    }
};


function BracketExprContext(parser, ctx) {
	AtomContext.call(this, parser);
    AtomContext.prototype.copyFrom.call(this, ctx);
    return this;
}

BracketExprContext.prototype = Object.create(AtomContext.prototype);
BracketExprContext.prototype.constructor = BracketExprContext;

TelParser.BracketExprContext = BracketExprContext;

BracketExprContext.prototype.L_BRACKET = function() {
    return this.getToken(TelParser.L_BRACKET, 0);
};

BracketExprContext.prototype.expr = function() {
    return this.getTypedRuleContext(ExprContext,0);
};

BracketExprContext.prototype.R_BRACKET = function() {
    return this.getToken(TelParser.R_BRACKET, 0);
};
BracketExprContext.prototype.enterRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.enterBracketExpr(this);
	}
};

BracketExprContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.exitBracketExpr(this);
	}
};

BracketExprContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelParserVisitor ) {
        return visitor.visitBracketExpr(this);
    } else {
        return visitor.visitChildren(this);
    }
};


function SingleQuotedAtomContext(parser, ctx) {
	AtomContext.call(this, parser);
    AtomContext.prototype.copyFrom.call(this, ctx);
    return this;
}

SingleQuotedAtomContext.prototype = Object.create(AtomContext.prototype);
SingleQuotedAtomContext.prototype.constructor = SingleQuotedAtomContext;

TelParser.SingleQuotedAtomContext = SingleQuotedAtomContext;

SingleQuotedAtomContext.prototype.SINGLE_QUOTED_ELEMENT = function() {
    return this.getToken(TelParser.SINGLE_QUOTED_ELEMENT, 0);
};
SingleQuotedAtomContext.prototype.enterRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.enterSingleQuotedAtom(this);
	}
};

SingleQuotedAtomContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.exitSingleQuotedAtom(this);
	}
};

SingleQuotedAtomContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelParserVisitor ) {
        return visitor.visitSingleQuotedAtom(this);
    } else {
        return visitor.visitChildren(this);
    }
};


function NumberAtomContext(parser, ctx) {
	AtomContext.call(this, parser);
    AtomContext.prototype.copyFrom.call(this, ctx);
    return this;
}

NumberAtomContext.prototype = Object.create(AtomContext.prototype);
NumberAtomContext.prototype.constructor = NumberAtomContext;

TelParser.NumberAtomContext = NumberAtomContext;

NumberAtomContext.prototype.INT = function() {
    return this.getToken(TelParser.INT, 0);
};

NumberAtomContext.prototype.REAL = function() {
    return this.getToken(TelParser.REAL, 0);
};
NumberAtomContext.prototype.enterRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.enterNumberAtom(this);
	}
};

NumberAtomContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.exitNumberAtom(this);
	}
};

NumberAtomContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelParserVisitor ) {
        return visitor.visitNumberAtom(this);
    } else {
        return visitor.visitChildren(this);
    }
};


function StringConstantAtomContext(parser, ctx) {
	AtomContext.call(this, parser);
    AtomContext.prototype.copyFrom.call(this, ctx);
    return this;
}

StringConstantAtomContext.prototype = Object.create(AtomContext.prototype);
StringConstantAtomContext.prototype.constructor = StringConstantAtomContext;

TelParser.StringConstantAtomContext = StringConstantAtomContext;

StringConstantAtomContext.prototype.STRING_CONSTANT = function() {
    return this.getToken(TelParser.STRING_CONSTANT, 0);
};
StringConstantAtomContext.prototype.enterRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.enterStringConstantAtom(this);
	}
};

StringConstantAtomContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.exitStringConstantAtom(this);
	}
};

StringConstantAtomContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelParserVisitor ) {
        return visitor.visitStringConstantAtom(this);
    } else {
        return visitor.visitChildren(this);
    }
};



TelParser.AtomContext = AtomContext;

TelParser.prototype.atom = function() {

    var localctx = new AtomContext(this, this._ctx, this.state);
    this.enterRule(localctx, 4, TelParser.RULE_atom);
    var _la = 0; // Token type
    try {
        this.state = 49;
        this._errHandler.sync(this);
        var la_ = this._interp.adaptivePredict(this._input,4,this._ctx);
        switch(la_) {
        case 1:
            localctx = new BracketExprContext(this, localctx);
            this.enterOuterAlt(localctx, 1);
            this.state = 39;
            this.match(TelParser.L_BRACKET);
            this.state = 40;
            this.expr(0);
            this.state = 41;
            this.match(TelParser.R_BRACKET);
            break;

        case 2:
            localctx = new NumberAtomContext(this, localctx);
            this.enterOuterAlt(localctx, 2);
            this.state = 43;
            _la = this._input.LA(1);
            if(!(_la===TelParser.INT || _la===TelParser.REAL)) {
            this._errHandler.recoverInline(this);
            }
            else {
            	this._errHandler.reportMatch(this);
                this.consume();
            }
            break;

        case 3:
            localctx = new BooleanAtomContext(this, localctx);
            this.enterOuterAlt(localctx, 3);
            this.state = 44;
            _la = this._input.LA(1);
            if(!(_la===TelParser.TRUE || _la===TelParser.FALSE)) {
            this._errHandler.recoverInline(this);
            }
            else {
            	this._errHandler.reportMatch(this);
                this.consume();
            }
            break;

        case 4:
            localctx = new SingleQuotedAtomContext(this, localctx);
            this.enterOuterAlt(localctx, 4);
            this.state = 45;
            this.match(TelParser.SINGLE_QUOTED_ELEMENT);
            break;

        case 5:
            localctx = new StringConstantAtomContext(this, localctx);
            this.enterOuterAlt(localctx, 5);
            this.state = 46;
            this.match(TelParser.STRING_CONSTANT);
            break;

        case 6:
            localctx = new FnExprContext(this, localctx);
            this.enterOuterAlt(localctx, 6);
            this.state = 47;
            this.fn();
            break;

        case 7:
            localctx = new TaxonSlugAtomContext(this, localctx);
            this.enterOuterAlt(localctx, 7);
            this.state = 48;
            this.taxon();
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


function FnContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = TelParser.RULE_fn;
    return this;
}

FnContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
FnContext.prototype.constructor = FnContext;

FnContext.prototype.WORD = function() {
    return this.getToken(TelParser.WORD, 0);
};

FnContext.prototype.L_BRACKET = function() {
    return this.getToken(TelParser.L_BRACKET, 0);
};

FnContext.prototype.R_BRACKET = function() {
    return this.getToken(TelParser.R_BRACKET, 0);
};

FnContext.prototype.expr = function(i) {
    if(i===undefined) {
        i = null;
    }
    if(i===null) {
        return this.getTypedRuleContexts(ExprContext);
    } else {
        return this.getTypedRuleContext(ExprContext,i);
    }
};

FnContext.prototype.FN_PARAMETER_DELIMITER = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(TelParser.FN_PARAMETER_DELIMITER);
    } else {
        return this.getToken(TelParser.FN_PARAMETER_DELIMITER, i);
    }
};


FnContext.prototype.enterRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.enterFn(this);
	}
};

FnContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelParserListener ) {
        listener.exitFn(this);
	}
};

FnContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelParserVisitor ) {
        return visitor.visitFn(this);
    } else {
        return visitor.visitChildren(this);
    }
};




TelParser.FnContext = FnContext;

TelParser.prototype.fn = function() {

    var localctx = new FnContext(this, this._ctx, this.state);
    this.enterRule(localctx, 6, TelParser.RULE_fn);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 51;
        this.match(TelParser.WORD);
        this.state = 52;
        this.match(TelParser.L_BRACKET);
        this.state = 54;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        if((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << TelParser.INT) | (1 << TelParser.REAL) | (1 << TelParser.TRUE) | (1 << TelParser.FALSE) | (1 << TelParser.NOT) | (1 << TelParser.WORD) | (1 << TelParser.STRING_CONSTANT) | (1 << TelParser.SINGLE_QUOTED_ELEMENT) | (1 << TelParser.L_BRACKET) | (1 << TelParser.OPTIONAL_TAXON_OPERATOR))) !== 0)) {
            this.state = 53;
            this.expr(0);
        }

        this.state = 60;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        while(_la===TelParser.FN_PARAMETER_DELIMITER) {
            this.state = 56;
            this.match(TelParser.FN_PARAMETER_DELIMITER);
            this.state = 57;
            this.expr(0);
            this.state = 62;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
        }
        this.state = 63;
        this.match(TelParser.R_BRACKET);
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
    return this;
}

TaxonContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
TaxonContext.prototype.constructor = TaxonContext;

TaxonContext.prototype.WORD = function(i) {
	if(i===undefined) {
		i = null;
	}
    if(i===null) {
        return this.getTokens(TelParser.WORD);
    } else {
        return this.getToken(TelParser.WORD, i);
    }
};


TaxonContext.prototype.OPTIONAL_TAXON_OPERATOR = function() {
    return this.getToken(TelParser.OPTIONAL_TAXON_OPERATOR, 0);
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
        this.state = 66;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        if(_la===TelParser.OPTIONAL_TAXON_OPERATOR) {
            this.state = 65;
            this.match(TelParser.OPTIONAL_TAXON_OPERATOR);
        }

        this.state = 68;
        this.match(TelParser.WORD);
        this.state = 71;
        this._errHandler.sync(this);
        var la_ = this._interp.adaptivePredict(this._input,8,this._ctx);
        if(la_===1) {
            this.state = 69;
            this.match(TelParser.TAXON_NAMESPACE_DELIMITER);
            this.state = 70;
            this.match(TelParser.WORD);

        }
        this.state = 75;
        this._errHandler.sync(this);
        var la_ = this._interp.adaptivePredict(this._input,9,this._ctx);
        if(la_===1) {
            this.state = 73;
            this.match(TelParser.TAXON_TAG_DELIMITER);
            this.state = 74;
            this.match(TelParser.WORD);

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
			return this.precpred(this._ctx, 5);
		case 1:
			return this.precpred(this._ctx, 4);
		case 2:
			return this.precpred(this._ctx, 3);
		case 3:
			return this.precpred(this._ctx, 2);
		default:
			throw "No predicate with index:" + predIndex;
	}
};


exports.TelParser = TelParser;

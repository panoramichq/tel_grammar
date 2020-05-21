// Generated from grammar/Tel.g4 by ANTLR 4.8
// jshint ignore: start
var antlr4 = require('antlr4/index');
var TelListener = require('./TelListener').TelListener;
var TelVisitor = require('./TelVisitor').TelVisitor;

var grammarFileName = "Tel.g4";


var serializedATN = ["\u0003\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964",
    "\u0003\u001cM\u0004\u0002\t\u0002\u0004\u0003\t\u0003\u0004\u0004\t",
    "\u0004\u0004\u0005\t\u0005\u0004\u0006\t\u0006\u0004\u0007\t\u0007\u0003",
    "\u0002\u0003\u0002\u0003\u0002\u0005\u0002\u0012\n\u0002\u0003\u0002",
    "\u0003\u0002\u0007\u0002\u0016\n\u0002\f\u0002\u000e\u0002\u0019\u000b",
    "\u0002\u0003\u0002\u0003\u0002\u0003\u0003\u0003\u0003\u0003\u0003\u0005",
    "\u0003 \n\u0003\u0003\u0003\u0003\u0003\u0005\u0003$\n\u0003\u0003\u0004",
    "\u0005\u0004\'\n\u0004\u0003\u0004\u0003\u0004\u0003\u0005\u0003\u0005",
    "\u0003\u0005\u0003\u0006\u0003\u0006\u0003\u0006\u0003\u0006\u0005\u0006",
    "2\n\u0006\u0003\u0006\u0003\u0006\u0003\u0006\u0003\u0006\u0003\u0006",
    "\u0003\u0006\u0003\u0006\u0003\u0006\u0003\u0006\u0007\u0006=\n\u0006",
    "\f\u0006\u000e\u0006@\u000b\u0006\u0003\u0007\u0003\u0007\u0003\u0007",
    "\u0003\u0007\u0003\u0007\u0003\u0007\u0003\u0007\u0003\u0007\u0003\u0007",
    "\u0005\u0007K\n\u0007\u0003\u0007\u0002\u0003\n\b\u0002\u0004\u0006",
    "\b\n\f\u0002\u0007\u0003\u0002\u0019\u001a\u0003\u0002\u0017\u0018\u0003",
    "\u0002\u000f\u0016\u0003\u0002\u0003\u0004\u0003\u0002\u0005\u0006\u0002",
    "T\u0002\u000e\u0003\u0002\u0002\u0002\u0004\u001c\u0003\u0002\u0002",
    "\u0002\u0006&\u0003\u0002\u0002\u0002\b*\u0003\u0002\u0002\u0002\n1",
    "\u0003\u0002\u0002\u0002\fJ\u0003\u0002\u0002\u0002\u000e\u000f\u0007",
    "\b\u0002\u0002\u000f\u0011\u0007\n\u0002\u0002\u0010\u0012\u0005\n\u0006",
    "\u0002\u0011\u0010\u0003\u0002\u0002\u0002\u0011\u0012\u0003\u0002\u0002",
    "\u0002\u0012\u0017\u0003\u0002\u0002\u0002\u0013\u0014\u0007\u000e\u0002",
    "\u0002\u0014\u0016\u0005\n\u0006\u0002\u0015\u0013\u0003\u0002\u0002",
    "\u0002\u0016\u0019\u0003\u0002\u0002\u0002\u0017\u0015\u0003\u0002\u0002",
    "\u0002\u0017\u0018\u0003\u0002\u0002\u0002\u0018\u001a\u0003\u0002\u0002",
    "\u0002\u0019\u0017\u0003\u0002\u0002\u0002\u001a\u001b\u0007\u000b\u0002",
    "\u0002\u001b\u0003\u0003\u0002\u0002\u0002\u001c\u001f\u0007\b\u0002",
    "\u0002\u001d\u001e\u0007\f\u0002\u0002\u001e \u0007\b\u0002\u0002\u001f",
    "\u001d\u0003\u0002\u0002\u0002\u001f \u0003\u0002\u0002\u0002 #\u0003",
    "\u0002\u0002\u0002!\"\u0007\r\u0002\u0002\"$\u0007\b\u0002\u0002#!\u0003",
    "\u0002\u0002\u0002#$\u0003\u0002\u0002\u0002$\u0005\u0003\u0002\u0002",
    "\u0002%\'\u0007\u001b\u0002\u0002&%\u0003\u0002\u0002\u0002&\'\u0003",
    "\u0002\u0002\u0002\'(\u0003\u0002\u0002\u0002()\u0005\u0004\u0003\u0002",
    ")\u0007\u0003\u0002\u0002\u0002*+\u0005\n\u0006\u0002+,\u0007\u0002",
    "\u0002\u0003,\t\u0003\u0002\u0002\u0002-.\b\u0006\u0001\u0002./\u0007",
    "\u0007\u0002\u0002/2\u0005\n\u0006\u000702\u0005\f\u0007\u00021-\u0003",
    "\u0002\u0002\u000210\u0003\u0002\u0002\u00022>\u0003\u0002\u0002\u0002",
    "34\f\u0006\u0002\u000245\t\u0002\u0002\u00025=\u0005\n\u0006\u00076",
    "7\f\u0005\u0002\u000278\t\u0003\u0002\u00028=\u0005\n\u0006\u00069:",
    "\f\u0004\u0002\u0002:;\t\u0004\u0002\u0002;=\u0005\n\u0006\u0005<3\u0003",
    "\u0002\u0002\u0002<6\u0003\u0002\u0002\u0002<9\u0003\u0002\u0002\u0002",
    "=@\u0003\u0002\u0002\u0002><\u0003\u0002\u0002\u0002>?\u0003\u0002\u0002",
    "\u0002?\u000b\u0003\u0002\u0002\u0002@>\u0003\u0002\u0002\u0002AB\u0007",
    "\n\u0002\u0002BC\u0005\n\u0006\u0002CD\u0007\u000b\u0002\u0002DK\u0003",
    "\u0002\u0002\u0002EK\t\u0005\u0002\u0002FK\u0005\u0002\u0002\u0002G",
    "K\t\u0006\u0002\u0002HK\u0005\u0006\u0004\u0002IK\u0007\t\u0002\u0002",
    "JA\u0003\u0002\u0002\u0002JE\u0003\u0002\u0002\u0002JF\u0003\u0002\u0002",
    "\u0002JG\u0003\u0002\u0002\u0002JH\u0003\u0002\u0002\u0002JI\u0003\u0002",
    "\u0002\u0002K\r\u0003\u0002\u0002\u0002\u000b\u0011\u0017\u001f#&1<",
    ">J"].join("");


var atn = new antlr4.atn.ATNDeserializer().deserialize(serializedATN);

var decisionsToDFA = atn.decisionToState.map( function(ds, index) { return new antlr4.dfa.DFA(ds, index); });

var sharedContextCache = new antlr4.PredictionContextCache();

var literalNames = [ null, null, null, "'true'", "'false'", "'not'", null, 
                     null, "'('", "')'", "'|'", "':'", "','", "'||'", "'&&'", 
                     "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", "'+'", 
                     "'-'", "'*'", "'/'", "'?'" ];

var symbolicNames = [ null, "INT", "REAL", "TRUE", "FALSE", "NOT", "WORD", 
                      "STRING_CONSTANT", "L_BRACKET", "R_BRACKET", "TAXON_NAMESPACE_DELIMITER", 
                      "TAXON_TAG_DELIMITER", "FN_PARAMETER_DELIMITER", "OR", 
                      "AND", "EQ", "NEQ", "GT", "LT", "GTEQ", "LTEQ", "PLUS", 
                      "MINUS", "MULT", "DIV", "OPTIONAL_TAXON_OPERATOR", 
                      "WS" ];

var ruleNames =  [ "fn", "taxon", "taxon_expr", "parse", "expr", "atom" ];

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
TelParser.WORD = 6;
TelParser.STRING_CONSTANT = 7;
TelParser.L_BRACKET = 8;
TelParser.R_BRACKET = 9;
TelParser.TAXON_NAMESPACE_DELIMITER = 10;
TelParser.TAXON_TAG_DELIMITER = 11;
TelParser.FN_PARAMETER_DELIMITER = 12;
TelParser.OR = 13;
TelParser.AND = 14;
TelParser.EQ = 15;
TelParser.NEQ = 16;
TelParser.GT = 17;
TelParser.LT = 18;
TelParser.GTEQ = 19;
TelParser.LTEQ = 20;
TelParser.PLUS = 21;
TelParser.MINUS = 22;
TelParser.MULT = 23;
TelParser.DIV = 24;
TelParser.OPTIONAL_TAXON_OPERATOR = 25;
TelParser.WS = 26;

TelParser.RULE_fn = 0;
TelParser.RULE_taxon = 1;
TelParser.RULE_taxon_expr = 2;
TelParser.RULE_parse = 3;
TelParser.RULE_expr = 4;
TelParser.RULE_atom = 5;


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
    if(listener instanceof TelListener ) {
        listener.enterFn(this);
	}
};

FnContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelListener ) {
        listener.exitFn(this);
	}
};

FnContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelVisitor ) {
        return visitor.visitFn(this);
    } else {
        return visitor.visitChildren(this);
    }
};




TelParser.FnContext = FnContext;

TelParser.prototype.fn = function() {

    var localctx = new FnContext(this, this._ctx, this.state);
    this.enterRule(localctx, 0, TelParser.RULE_fn);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 12;
        this.match(TelParser.WORD);
        this.state = 13;
        this.match(TelParser.L_BRACKET);
        this.state = 15;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        if((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << TelParser.INT) | (1 << TelParser.REAL) | (1 << TelParser.TRUE) | (1 << TelParser.FALSE) | (1 << TelParser.NOT) | (1 << TelParser.WORD) | (1 << TelParser.STRING_CONSTANT) | (1 << TelParser.L_BRACKET) | (1 << TelParser.OPTIONAL_TAXON_OPERATOR))) !== 0)) {
            this.state = 14;
            this.expr(0);
        }

        this.state = 21;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        while(_la===TelParser.FN_PARAMETER_DELIMITER) {
            this.state = 17;
            this.match(TelParser.FN_PARAMETER_DELIMITER);
            this.state = 18;
            this.expr(0);
            this.state = 23;
            this._errHandler.sync(this);
            _la = this._input.LA(1);
        }
        this.state = 24;
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


TaxonContext.prototype.TAXON_NAMESPACE_DELIMITER = function() {
    return this.getToken(TelParser.TAXON_NAMESPACE_DELIMITER, 0);
};

TaxonContext.prototype.TAXON_TAG_DELIMITER = function() {
    return this.getToken(TelParser.TAXON_TAG_DELIMITER, 0);
};

TaxonContext.prototype.enterRule = function(listener) {
    if(listener instanceof TelListener ) {
        listener.enterTaxon(this);
	}
};

TaxonContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelListener ) {
        listener.exitTaxon(this);
	}
};

TaxonContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelVisitor ) {
        return visitor.visitTaxon(this);
    } else {
        return visitor.visitChildren(this);
    }
};




TelParser.TaxonContext = TaxonContext;

TelParser.prototype.taxon = function() {

    var localctx = new TaxonContext(this, this._ctx, this.state);
    this.enterRule(localctx, 2, TelParser.RULE_taxon);
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 26;
        this.match(TelParser.WORD);
        this.state = 29;
        this._errHandler.sync(this);
        var la_ = this._interp.adaptivePredict(this._input,2,this._ctx);
        if(la_===1) {
            this.state = 27;
            this.match(TelParser.TAXON_NAMESPACE_DELIMITER);
            this.state = 28;
            this.match(TelParser.WORD);

        }
        this.state = 33;
        this._errHandler.sync(this);
        var la_ = this._interp.adaptivePredict(this._input,3,this._ctx);
        if(la_===1) {
            this.state = 31;
            this.match(TelParser.TAXON_TAG_DELIMITER);
            this.state = 32;
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


function Taxon_exprContext(parser, parent, invokingState) {
	if(parent===undefined) {
	    parent = null;
	}
	if(invokingState===undefined || invokingState===null) {
		invokingState = -1;
	}
	antlr4.ParserRuleContext.call(this, parent, invokingState);
    this.parser = parser;
    this.ruleIndex = TelParser.RULE_taxon_expr;
    return this;
}

Taxon_exprContext.prototype = Object.create(antlr4.ParserRuleContext.prototype);
Taxon_exprContext.prototype.constructor = Taxon_exprContext;

Taxon_exprContext.prototype.taxon = function() {
    return this.getTypedRuleContext(TaxonContext,0);
};

Taxon_exprContext.prototype.OPTIONAL_TAXON_OPERATOR = function() {
    return this.getToken(TelParser.OPTIONAL_TAXON_OPERATOR, 0);
};

Taxon_exprContext.prototype.enterRule = function(listener) {
    if(listener instanceof TelListener ) {
        listener.enterTaxon_expr(this);
	}
};

Taxon_exprContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelListener ) {
        listener.exitTaxon_expr(this);
	}
};

Taxon_exprContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelVisitor ) {
        return visitor.visitTaxon_expr(this);
    } else {
        return visitor.visitChildren(this);
    }
};




TelParser.Taxon_exprContext = Taxon_exprContext;

TelParser.prototype.taxon_expr = function() {

    var localctx = new Taxon_exprContext(this, this._ctx, this.state);
    this.enterRule(localctx, 4, TelParser.RULE_taxon_expr);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 36;
        this._errHandler.sync(this);
        _la = this._input.LA(1);
        if(_la===TelParser.OPTIONAL_TAXON_OPERATOR) {
            this.state = 35;
            this.match(TelParser.OPTIONAL_TAXON_OPERATOR);
        }

        this.state = 38;
        this.taxon();
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
    if(listener instanceof TelListener ) {
        listener.enterParse(this);
	}
};

ParseContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelListener ) {
        listener.exitParse(this);
	}
};

ParseContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelVisitor ) {
        return visitor.visitParse(this);
    } else {
        return visitor.visitChildren(this);
    }
};




TelParser.ParseContext = ParseContext;

TelParser.prototype.parse = function() {

    var localctx = new ParseContext(this, this._ctx, this.state);
    this.enterRule(localctx, 6, TelParser.RULE_parse);
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 40;
        this.expr(0);
        this.state = 41;
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
    if(listener instanceof TelListener ) {
        listener.enterNotExpr(this);
	}
};

NotExprContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelListener ) {
        listener.exitNotExpr(this);
	}
};

NotExprContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelVisitor ) {
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
    if(listener instanceof TelListener ) {
        listener.enterLogicalExpr(this);
	}
};

LogicalExprContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelListener ) {
        listener.exitLogicalExpr(this);
	}
};

LogicalExprContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelVisitor ) {
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
    if(listener instanceof TelListener ) {
        listener.enterMultiplicationExpr(this);
	}
};

MultiplicationExprContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelListener ) {
        listener.exitMultiplicationExpr(this);
	}
};

MultiplicationExprContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelVisitor ) {
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
    if(listener instanceof TelListener ) {
        listener.enterAtomExpr(this);
	}
};

AtomExprContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelListener ) {
        listener.exitAtomExpr(this);
	}
};

AtomExprContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelVisitor ) {
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
    if(listener instanceof TelListener ) {
        listener.enterAdditiveExpr(this);
	}
};

AdditiveExprContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelListener ) {
        listener.exitAdditiveExpr(this);
	}
};

AdditiveExprContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelVisitor ) {
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
    var _startState = 8;
    this.enterRecursionRule(localctx, 8, TelParser.RULE_expr, _p);
    var _la = 0; // Token type
    try {
        this.enterOuterAlt(localctx, 1);
        this.state = 47;
        this._errHandler.sync(this);
        switch(this._input.LA(1)) {
        case TelParser.NOT:
            localctx = new NotExprContext(this, localctx);
            this._ctx = localctx;
            _prevctx = localctx;

            this.state = 44;
            this.match(TelParser.NOT);
            this.state = 45;
            this.expr(5);
            break;
        case TelParser.INT:
        case TelParser.REAL:
        case TelParser.TRUE:
        case TelParser.FALSE:
        case TelParser.WORD:
        case TelParser.STRING_CONSTANT:
        case TelParser.L_BRACKET:
        case TelParser.OPTIONAL_TAXON_OPERATOR:
            localctx = new AtomExprContext(this, localctx);
            this._ctx = localctx;
            _prevctx = localctx;
            this.state = 46;
            this.atom();
            break;
        default:
            throw new antlr4.error.NoViableAltException(this);
        }
        this._ctx.stop = this._input.LT(-1);
        this.state = 60;
        this._errHandler.sync(this);
        var _alt = this._interp.adaptivePredict(this._input,7,this._ctx)
        while(_alt!=2 && _alt!=antlr4.atn.ATN.INVALID_ALT_NUMBER) {
            if(_alt===1) {
                if(this._parseListeners!==null) {
                    this.triggerExitRuleEvent();
                }
                _prevctx = localctx;
                this.state = 58;
                this._errHandler.sync(this);
                var la_ = this._interp.adaptivePredict(this._input,6,this._ctx);
                switch(la_) {
                case 1:
                    localctx = new MultiplicationExprContext(this, new ExprContext(this, _parentctx, _parentState));
                    this.pushNewRecursionContext(localctx, _startState, TelParser.RULE_expr);
                    this.state = 49;
                    if (!( this.precpred(this._ctx, 4))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 4)");
                    }
                    this.state = 50;
                    localctx.op = this._input.LT(1);
                    _la = this._input.LA(1);
                    if(!(_la===TelParser.MULT || _la===TelParser.DIV)) {
                        localctx.op = this._errHandler.recoverInline(this);
                    }
                    else {
                    	this._errHandler.reportMatch(this);
                        this.consume();
                    }
                    this.state = 51;
                    this.expr(5);
                    break;

                case 2:
                    localctx = new AdditiveExprContext(this, new ExprContext(this, _parentctx, _parentState));
                    this.pushNewRecursionContext(localctx, _startState, TelParser.RULE_expr);
                    this.state = 52;
                    if (!( this.precpred(this._ctx, 3))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 3)");
                    }
                    this.state = 53;
                    localctx.op = this._input.LT(1);
                    _la = this._input.LA(1);
                    if(!(_la===TelParser.PLUS || _la===TelParser.MINUS)) {
                        localctx.op = this._errHandler.recoverInline(this);
                    }
                    else {
                    	this._errHandler.reportMatch(this);
                        this.consume();
                    }
                    this.state = 54;
                    this.expr(4);
                    break;

                case 3:
                    localctx = new LogicalExprContext(this, new ExprContext(this, _parentctx, _parentState));
                    this.pushNewRecursionContext(localctx, _startState, TelParser.RULE_expr);
                    this.state = 55;
                    if (!( this.precpred(this._ctx, 2))) {
                        throw new antlr4.error.FailedPredicateException(this, "this.precpred(this._ctx, 2)");
                    }
                    this.state = 56;
                    localctx.op = this._input.LT(1);
                    _la = this._input.LA(1);
                    if(!((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << TelParser.OR) | (1 << TelParser.AND) | (1 << TelParser.EQ) | (1 << TelParser.NEQ) | (1 << TelParser.GT) | (1 << TelParser.LT) | (1 << TelParser.GTEQ) | (1 << TelParser.LTEQ))) !== 0))) {
                        localctx.op = this._errHandler.recoverInline(this);
                    }
                    else {
                    	this._errHandler.reportMatch(this);
                        this.consume();
                    }
                    this.state = 57;
                    this.expr(3);
                    break;

                } 
            }
            this.state = 62;
            this._errHandler.sync(this);
            _alt = this._interp.adaptivePredict(this._input,7,this._ctx);
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
    if(listener instanceof TelListener ) {
        listener.enterFnExpr(this);
	}
};

FnExprContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelListener ) {
        listener.exitFnExpr(this);
	}
};

FnExprContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelVisitor ) {
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

TaxonSlugAtomContext.prototype.taxon_expr = function() {
    return this.getTypedRuleContext(Taxon_exprContext,0);
};
TaxonSlugAtomContext.prototype.enterRule = function(listener) {
    if(listener instanceof TelListener ) {
        listener.enterTaxonSlugAtom(this);
	}
};

TaxonSlugAtomContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelListener ) {
        listener.exitTaxonSlugAtom(this);
	}
};

TaxonSlugAtomContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelVisitor ) {
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
    if(listener instanceof TelListener ) {
        listener.enterBooleanAtom(this);
	}
};

BooleanAtomContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelListener ) {
        listener.exitBooleanAtom(this);
	}
};

BooleanAtomContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelVisitor ) {
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
    if(listener instanceof TelListener ) {
        listener.enterBracketExpr(this);
	}
};

BracketExprContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelListener ) {
        listener.exitBracketExpr(this);
	}
};

BracketExprContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelVisitor ) {
        return visitor.visitBracketExpr(this);
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
    if(listener instanceof TelListener ) {
        listener.enterNumberAtom(this);
	}
};

NumberAtomContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelListener ) {
        listener.exitNumberAtom(this);
	}
};

NumberAtomContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelVisitor ) {
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
    if(listener instanceof TelListener ) {
        listener.enterStringConstantAtom(this);
	}
};

StringConstantAtomContext.prototype.exitRule = function(listener) {
    if(listener instanceof TelListener ) {
        listener.exitStringConstantAtom(this);
	}
};

StringConstantAtomContext.prototype.accept = function(visitor) {
    if ( visitor instanceof TelVisitor ) {
        return visitor.visitStringConstantAtom(this);
    } else {
        return visitor.visitChildren(this);
    }
};



TelParser.AtomContext = AtomContext;

TelParser.prototype.atom = function() {

    var localctx = new AtomContext(this, this._ctx, this.state);
    this.enterRule(localctx, 10, TelParser.RULE_atom);
    var _la = 0; // Token type
    try {
        this.state = 72;
        this._errHandler.sync(this);
        var la_ = this._interp.adaptivePredict(this._input,8,this._ctx);
        switch(la_) {
        case 1:
            localctx = new BracketExprContext(this, localctx);
            this.enterOuterAlt(localctx, 1);
            this.state = 63;
            this.match(TelParser.L_BRACKET);
            this.state = 64;
            this.expr(0);
            this.state = 65;
            this.match(TelParser.R_BRACKET);
            break;

        case 2:
            localctx = new NumberAtomContext(this, localctx);
            this.enterOuterAlt(localctx, 2);
            this.state = 67;
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
            localctx = new FnExprContext(this, localctx);
            this.enterOuterAlt(localctx, 3);
            this.state = 68;
            this.fn();
            break;

        case 4:
            localctx = new BooleanAtomContext(this, localctx);
            this.enterOuterAlt(localctx, 4);
            this.state = 69;
            _la = this._input.LA(1);
            if(!(_la===TelParser.TRUE || _la===TelParser.FALSE)) {
            this._errHandler.recoverInline(this);
            }
            else {
            	this._errHandler.reportMatch(this);
                this.consume();
            }
            break;

        case 5:
            localctx = new TaxonSlugAtomContext(this, localctx);
            this.enterOuterAlt(localctx, 5);
            this.state = 70;
            this.taxon_expr();
            break;

        case 6:
            localctx = new StringConstantAtomContext(this, localctx);
            this.enterOuterAlt(localctx, 6);
            this.state = 71;
            this.match(TelParser.STRING_CONSTANT);
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


TelParser.prototype.sempred = function(localctx, ruleIndex, predIndex) {
	switch(ruleIndex) {
	case 4:
			return this.expr_sempred(localctx, predIndex);
    default:
        throw "No predicate with index:" + ruleIndex;
   }
};

TelParser.prototype.expr_sempred = function(localctx, predIndex) {
	switch(predIndex) {
		case 0:
			return this.precpred(this._ctx, 4);
		case 1:
			return this.precpred(this._ctx, 3);
		case 2:
			return this.precpred(this._ctx, 2);
		default:
			throw "No predicate with index:" + predIndex;
	}
};


exports.TelParser = TelParser;

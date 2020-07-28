# Generated from grammar/Tel.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\35")
        buf.write("N\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\5\2\22\n\2\3\2\3\2\7\2\26\n\2\f\2\16\2\31\13")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\5\3 \n\3\3\3\3\3\5\3$\n\3\3\4\5")
        buf.write("\4\'\n\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\5\6\62\n")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6=\n\6\f\6\16")
        buf.write("\6@\13\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7L")
        buf.write("\n\7\3\7\2\3\n\b\2\4\6\b\n\f\2\7\3\2\32\33\3\2\30\31\3")
        buf.write("\2\20\27\3\2\3\4\3\2\5\6\2V\2\16\3\2\2\2\4\34\3\2\2\2")
        buf.write("\6&\3\2\2\2\b*\3\2\2\2\n\61\3\2\2\2\fK\3\2\2\2\16\17\7")
        buf.write("\b\2\2\17\21\7\13\2\2\20\22\5\n\6\2\21\20\3\2\2\2\21\22")
        buf.write("\3\2\2\2\22\27\3\2\2\2\23\24\7\17\2\2\24\26\5\n\6\2\25")
        buf.write("\23\3\2\2\2\26\31\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2")
        buf.write("\30\32\3\2\2\2\31\27\3\2\2\2\32\33\7\f\2\2\33\3\3\2\2")
        buf.write("\2\34\37\7\b\2\2\35\36\7\r\2\2\36 \7\b\2\2\37\35\3\2\2")
        buf.write("\2\37 \3\2\2\2 #\3\2\2\2!\"\7\16\2\2\"$\7\b\2\2#!\3\2")
        buf.write("\2\2#$\3\2\2\2$\5\3\2\2\2%\'\7\34\2\2&%\3\2\2\2&\'\3\2")
        buf.write("\2\2\'(\3\2\2\2()\5\4\3\2)\7\3\2\2\2*+\5\n\6\2+,\7\2\2")
        buf.write("\3,\t\3\2\2\2-.\b\6\1\2./\7\7\2\2/\62\5\n\6\7\60\62\5")
        buf.write("\f\7\2\61-\3\2\2\2\61\60\3\2\2\2\62>\3\2\2\2\63\64\f\6")
        buf.write("\2\2\64\65\t\2\2\2\65=\5\n\6\7\66\67\f\5\2\2\678\t\3\2")
        buf.write("\28=\5\n\6\69:\f\4\2\2:;\t\4\2\2;=\5\n\6\5<\63\3\2\2\2")
        buf.write("<\66\3\2\2\2<9\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?")
        buf.write("\13\3\2\2\2@>\3\2\2\2AB\7\13\2\2BC\5\n\6\2CD\7\f\2\2D")
        buf.write("L\3\2\2\2EL\t\5\2\2FL\5\2\2\2GL\t\6\2\2HL\5\6\4\2IL\7")
        buf.write("\n\2\2JL\7\t\2\2KA\3\2\2\2KE\3\2\2\2KF\3\2\2\2KG\3\2\2")
        buf.write("\2KH\3\2\2\2KI\3\2\2\2KJ\3\2\2\2L\r\3\2\2\2\13\21\27\37")
        buf.write("#&\61<>K")
        return buf.getvalue()


class TelParser ( Parser ):

    grammarFileName = "Tel.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'true'", "'false'", 
                     "'not'", "<INVALID>", "<INVALID>", "<INVALID>", "'('", 
                     "')'", "'|'", "':'", "','", "'||'", "'&&'", "'=='", 
                     "'!='", "'>'", "'<'", "'>='", "'<='", "'+'", "'-'", 
                     "'*'", "'/'", "'?'" ]

    symbolicNames = [ "<INVALID>", "INT", "REAL", "TRUE", "FALSE", "NOT", 
                      "WORD", "STRING_CONSTANT", "SINGLE_QUOTED_ELEMENT", 
                      "L_BRACKET", "R_BRACKET", "TAXON_NAMESPACE_DELIMITER", 
                      "TAXON_TAG_DELIMITER", "FN_PARAMETER_DELIMITER", "OR", 
                      "AND", "EQ", "NEQ", "GT", "LT", "GTEQ", "LTEQ", "PLUS", 
                      "MINUS", "MULT", "DIV", "OPTIONAL_TAXON_OPERATOR", 
                      "WS" ]

    RULE_fn = 0
    RULE_taxon = 1
    RULE_taxon_expr = 2
    RULE_parse = 3
    RULE_expr = 4
    RULE_atom = 5

    ruleNames =  [ "fn", "taxon", "taxon_expr", "parse", "expr", "atom" ]

    EOF = Token.EOF
    INT=1
    REAL=2
    TRUE=3
    FALSE=4
    NOT=5
    WORD=6
    STRING_CONSTANT=7
    SINGLE_QUOTED_ELEMENT=8
    L_BRACKET=9
    R_BRACKET=10
    TAXON_NAMESPACE_DELIMITER=11
    TAXON_TAG_DELIMITER=12
    FN_PARAMETER_DELIMITER=13
    OR=14
    AND=15
    EQ=16
    NEQ=17
    GT=18
    LT=19
    GTEQ=20
    LTEQ=21
    PLUS=22
    MINUS=23
    MULT=24
    DIV=25
    OPTIONAL_TAXON_OPERATOR=26
    WS=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(TelParser.WORD, 0)

        def L_BRACKET(self):
            return self.getToken(TelParser.L_BRACKET, 0)

        def R_BRACKET(self):
            return self.getToken(TelParser.R_BRACKET, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TelParser.ExprContext)
            else:
                return self.getTypedRuleContext(TelParser.ExprContext,i)


        def FN_PARAMETER_DELIMITER(self, i:int=None):
            if i is None:
                return self.getTokens(TelParser.FN_PARAMETER_DELIMITER)
            else:
                return self.getToken(TelParser.FN_PARAMETER_DELIMITER, i)

        def getRuleIndex(self):
            return TelParser.RULE_fn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFn" ):
                listener.enterFn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFn" ):
                listener.exitFn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFn" ):
                return visitor.visitFn(self)
            else:
                return visitor.visitChildren(self)




    def fn(self):

        localctx = TelParser.FnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_fn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(TelParser.WORD)
            self.state = 13
            self.match(TelParser.L_BRACKET)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TelParser.INT) | (1 << TelParser.REAL) | (1 << TelParser.TRUE) | (1 << TelParser.FALSE) | (1 << TelParser.NOT) | (1 << TelParser.WORD) | (1 << TelParser.STRING_CONSTANT) | (1 << TelParser.SINGLE_QUOTED_ELEMENT) | (1 << TelParser.L_BRACKET) | (1 << TelParser.OPTIONAL_TAXON_OPERATOR))) != 0):
                self.state = 14
                self.expr(0)


            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TelParser.FN_PARAMETER_DELIMITER:
                self.state = 17
                self.match(TelParser.FN_PARAMETER_DELIMITER)
                self.state = 18
                self.expr(0)
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(TelParser.R_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TaxonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(TelParser.WORD)
            else:
                return self.getToken(TelParser.WORD, i)

        def TAXON_NAMESPACE_DELIMITER(self):
            return self.getToken(TelParser.TAXON_NAMESPACE_DELIMITER, 0)

        def TAXON_TAG_DELIMITER(self):
            return self.getToken(TelParser.TAXON_TAG_DELIMITER, 0)

        def getRuleIndex(self):
            return TelParser.RULE_taxon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTaxon" ):
                listener.enterTaxon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTaxon" ):
                listener.exitTaxon(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTaxon" ):
                return visitor.visitTaxon(self)
            else:
                return visitor.visitChildren(self)




    def taxon(self):

        localctx = TelParser.TaxonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_taxon)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(TelParser.WORD)
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 27
                self.match(TelParser.TAXON_NAMESPACE_DELIMITER)
                self.state = 28
                self.match(TelParser.WORD)


            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 31
                self.match(TelParser.TAXON_TAG_DELIMITER)
                self.state = 32
                self.match(TelParser.WORD)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Taxon_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def taxon(self):
            return self.getTypedRuleContext(TelParser.TaxonContext,0)


        def OPTIONAL_TAXON_OPERATOR(self):
            return self.getToken(TelParser.OPTIONAL_TAXON_OPERATOR, 0)

        def getRuleIndex(self):
            return TelParser.RULE_taxon_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTaxon_expr" ):
                listener.enterTaxon_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTaxon_expr" ):
                listener.exitTaxon_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTaxon_expr" ):
                return visitor.visitTaxon_expr(self)
            else:
                return visitor.visitChildren(self)




    def taxon_expr(self):

        localctx = TelParser.Taxon_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_taxon_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TelParser.OPTIONAL_TAXON_OPERATOR:
                self.state = 35
                self.match(TelParser.OPTIONAL_TAXON_OPERATOR)


            self.state = 38
            self.taxon()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(TelParser.ExprContext,0)


        def EOF(self):
            return self.getToken(TelParser.EOF, 0)

        def getRuleIndex(self):
            return TelParser.RULE_parse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParse" ):
                listener.enterParse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParse" ):
                listener.exitParse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParse" ):
                return visitor.visitParse(self)
            else:
                return visitor.visitChildren(self)




    def parse(self):

        localctx = TelParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.expr(0)
            self.state = 41
            self.match(TelParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TelParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NotExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TelParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(TelParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(TelParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class LogicalExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TelParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TelParser.ExprContext)
            else:
                return self.getTypedRuleContext(TelParser.ExprContext,i)

        def OR(self):
            return self.getToken(TelParser.OR, 0)
        def AND(self):
            return self.getToken(TelParser.AND, 0)
        def EQ(self):
            return self.getToken(TelParser.EQ, 0)
        def NEQ(self):
            return self.getToken(TelParser.NEQ, 0)
        def GT(self):
            return self.getToken(TelParser.GT, 0)
        def LT(self):
            return self.getToken(TelParser.LT, 0)
        def GTEQ(self):
            return self.getToken(TelParser.GTEQ, 0)
        def LTEQ(self):
            return self.getToken(TelParser.LTEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalExpr" ):
                listener.enterLogicalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalExpr" ):
                listener.exitLogicalExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalExpr" ):
                return visitor.visitLogicalExpr(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicationExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TelParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TelParser.ExprContext)
            else:
                return self.getTypedRuleContext(TelParser.ExprContext,i)

        def MULT(self):
            return self.getToken(TelParser.MULT, 0)
        def DIV(self):
            return self.getToken(TelParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicationExpr" ):
                listener.enterMultiplicationExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicationExpr" ):
                listener.exitMultiplicationExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicationExpr" ):
                return visitor.visitMultiplicationExpr(self)
            else:
                return visitor.visitChildren(self)


    class AtomExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TelParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(TelParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomExpr" ):
                listener.enterAtomExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomExpr" ):
                listener.exitAtomExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomExpr" ):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)


    class AdditiveExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TelParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TelParser.ExprContext)
            else:
                return self.getTypedRuleContext(TelParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(TelParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(TelParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpr" ):
                listener.enterAdditiveExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpr" ):
                listener.exitAdditiveExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpr" ):
                return visitor.visitAdditiveExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TelParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TelParser.NOT]:
                localctx = TelParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 44
                self.match(TelParser.NOT)
                self.state = 45
                self.expr(5)
                pass
            elif token in [TelParser.INT, TelParser.REAL, TelParser.TRUE, TelParser.FALSE, TelParser.WORD, TelParser.STRING_CONSTANT, TelParser.SINGLE_QUOTED_ELEMENT, TelParser.L_BRACKET, TelParser.OPTIONAL_TAXON_OPERATOR]:
                localctx = TelParser.AtomExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 46
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 58
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = TelParser.MultiplicationExprContext(self, TelParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 49
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 50
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==TelParser.MULT or _la==TelParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 51
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = TelParser.AdditiveExprContext(self, TelParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 52
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 53
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==TelParser.PLUS or _la==TelParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 54
                        self.expr(4)
                        pass

                    elif la_ == 3:
                        localctx = TelParser.LogicalExprContext(self, TelParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 55
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 56
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TelParser.OR) | (1 << TelParser.AND) | (1 << TelParser.EQ) | (1 << TelParser.NEQ) | (1 << TelParser.GT) | (1 << TelParser.LT) | (1 << TelParser.GTEQ) | (1 << TelParser.LTEQ))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 57
                        self.expr(3)
                        pass

             
                self.state = 62
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TelParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FnExprContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TelParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fn(self):
            return self.getTypedRuleContext(TelParser.FnContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFnExpr" ):
                listener.enterFnExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFnExpr" ):
                listener.exitFnExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFnExpr" ):
                return visitor.visitFnExpr(self)
            else:
                return visitor.visitChildren(self)


    class TaxonSlugAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TelParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def taxon_expr(self):
            return self.getTypedRuleContext(TelParser.Taxon_exprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTaxonSlugAtom" ):
                listener.enterTaxonSlugAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTaxonSlugAtom" ):
                listener.exitTaxonSlugAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTaxonSlugAtom" ):
                return visitor.visitTaxonSlugAtom(self)
            else:
                return visitor.visitChildren(self)


    class BooleanAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TelParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(TelParser.TRUE, 0)
        def FALSE(self):
            return self.getToken(TelParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanAtom" ):
                listener.enterBooleanAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanAtom" ):
                listener.exitBooleanAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanAtom" ):
                return visitor.visitBooleanAtom(self)
            else:
                return visitor.visitChildren(self)


    class BracketExprContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TelParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def L_BRACKET(self):
            return self.getToken(TelParser.L_BRACKET, 0)
        def expr(self):
            return self.getTypedRuleContext(TelParser.ExprContext,0)

        def R_BRACKET(self):
            return self.getToken(TelParser.R_BRACKET, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBracketExpr" ):
                listener.enterBracketExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBracketExpr" ):
                listener.exitBracketExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBracketExpr" ):
                return visitor.visitBracketExpr(self)
            else:
                return visitor.visitChildren(self)


    class SingleQuotedAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TelParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SINGLE_QUOTED_ELEMENT(self):
            return self.getToken(TelParser.SINGLE_QUOTED_ELEMENT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleQuotedAtom" ):
                listener.enterSingleQuotedAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleQuotedAtom" ):
                listener.exitSingleQuotedAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleQuotedAtom" ):
                return visitor.visitSingleQuotedAtom(self)
            else:
                return visitor.visitChildren(self)


    class NumberAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TelParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(TelParser.INT, 0)
        def REAL(self):
            return self.getToken(TelParser.REAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberAtom" ):
                listener.enterNumberAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberAtom" ):
                listener.exitNumberAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberAtom" ):
                return visitor.visitNumberAtom(self)
            else:
                return visitor.visitChildren(self)


    class StringConstantAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TelParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING_CONSTANT(self):
            return self.getToken(TelParser.STRING_CONSTANT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringConstantAtom" ):
                listener.enterStringConstantAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringConstantAtom" ):
                listener.exitStringConstantAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringConstantAtom" ):
                return visitor.visitStringConstantAtom(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = TelParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = TelParser.BracketExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(TelParser.L_BRACKET)
                self.state = 64
                self.expr(0)
                self.state = 65
                self.match(TelParser.R_BRACKET)
                pass

            elif la_ == 2:
                localctx = TelParser.NumberAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                _la = self._input.LA(1)
                if not(_la==TelParser.INT or _la==TelParser.REAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                localctx = TelParser.FnExprContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.fn()
                pass

            elif la_ == 4:
                localctx = TelParser.BooleanAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                _la = self._input.LA(1)
                if not(_la==TelParser.TRUE or _la==TelParser.FALSE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 5:
                localctx = TelParser.TaxonSlugAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 70
                self.taxon_expr()
                pass

            elif la_ == 6:
                localctx = TelParser.SingleQuotedAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 71
                self.match(TelParser.SINGLE_QUOTED_ELEMENT)
                pass

            elif la_ == 7:
                localctx = TelParser.StringConstantAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 72
                self.match(TelParser.STRING_CONSTANT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         





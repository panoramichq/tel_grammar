# Generated from grammar/TelParser.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3 ")
        buf.write("P\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\5\3\24\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\5\3\"\n\3\3\3\7\3%\n\3\f\3\16\3")
        buf.write("(\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\64")
        buf.write("\n\4\3\5\3\5\3\5\5\59\n\5\3\5\3\5\7\5=\n\5\f\5\16\5@\13")
        buf.write("\5\3\5\3\5\3\6\5\6E\n\6\3\6\3\6\3\6\5\6J\n\6\3\6\3\6\5")
        buf.write("\6N\n\6\3\6\2\3\4\7\2\4\6\b\n\2\7\3\2\34\35\3\2\32\33")
        buf.write("\3\2\22\31\3\2\3\4\3\2\5\6\2[\2\f\3\2\2\2\4\23\3\2\2\2")
        buf.write("\6\63\3\2\2\2\b\65\3\2\2\2\nD\3\2\2\2\f\r\5\4\3\2\r\16")
        buf.write("\7\2\2\3\16\3\3\2\2\2\17\20\b\3\1\2\20\21\7\7\2\2\21\24")
        buf.write("\5\4\3\b\22\24\5\6\4\2\23\17\3\2\2\2\23\22\3\2\2\2\24")
        buf.write("&\3\2\2\2\25\26\f\7\2\2\26\27\t\2\2\2\27%\5\4\3\b\30\31")
        buf.write("\f\6\2\2\31\32\t\3\2\2\32%\5\4\3\7\33\34\f\5\2\2\34\35")
        buf.write("\t\4\2\2\35%\5\4\3\6\36\37\f\4\2\2\37!\7\b\2\2 \"\7\7")
        buf.write("\2\2! \3\2\2\2!\"\3\2\2\2\"#\3\2\2\2#%\7\t\2\2$\25\3\2")
        buf.write("\2\2$\30\3\2\2\2$\33\3\2\2\2$\36\3\2\2\2%(\3\2\2\2&$\3")
        buf.write("\2\2\2&\'\3\2\2\2\'\5\3\2\2\2(&\3\2\2\2)*\7\r\2\2*+\5")
        buf.write("\4\3\2+,\7\16\2\2,\64\3\2\2\2-\64\t\5\2\2.\64\t\6\2\2")
        buf.write("/\64\7\f\2\2\60\64\7\13\2\2\61\64\5\b\5\2\62\64\5\n\6")
        buf.write("\2\63)\3\2\2\2\63-\3\2\2\2\63.\3\2\2\2\63/\3\2\2\2\63")
        buf.write("\60\3\2\2\2\63\61\3\2\2\2\63\62\3\2\2\2\64\7\3\2\2\2\65")
        buf.write("\66\7\n\2\2\668\7\r\2\2\679\5\4\3\28\67\3\2\2\289\3\2")
        buf.write("\2\29>\3\2\2\2:;\7\21\2\2;=\5\4\3\2<:\3\2\2\2=@\3\2\2")
        buf.write("\2><\3\2\2\2>?\3\2\2\2?A\3\2\2\2@>\3\2\2\2AB\7\16\2\2")
        buf.write("B\t\3\2\2\2CE\7\36\2\2DC\3\2\2\2DE\3\2\2\2EF\3\2\2\2F")
        buf.write("I\7\n\2\2GH\7\17\2\2HJ\7\n\2\2IG\3\2\2\2IJ\3\2\2\2JM\3")
        buf.write("\2\2\2KL\7\20\2\2LN\7\n\2\2MK\3\2\2\2MN\3\2\2\2N\13\3")
        buf.write("\2\2\2\f\23!$&\638>DIM")
        return buf.getvalue()


class TelParser ( Parser ):

    grammarFileName = "TelParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'|'", "':'", "','", "'||'", "'&&'", "'=='", "'!='", 
                     "'>'", "'<'", "'>='", "'<='", "'+'", "'-'", "'*'", 
                     "'/'", "'?'" ]

    symbolicNames = [ "<INVALID>", "INT", "REAL", "TRUE", "FALSE", "NOT", 
                      "KW_IS", "KW_NULL", "WORD", "STRING_CONSTANT", "SINGLE_QUOTED_ELEMENT", 
                      "L_BRACKET", "R_BRACKET", "TAXON_NAMESPACE_DELIMITER", 
                      "TAXON_TAG_DELIMITER", "FN_PARAMETER_DELIMITER", "OR", 
                      "AND", "EQ", "NEQ", "GT", "LT", "GTEQ", "LTEQ", "PLUS", 
                      "MINUS", "MULT", "DIV", "OPTIONAL_TAXON_OPERATOR", 
                      "SINGLE_LINE_COMMENT", "WS" ]

    RULE_parse = 0
    RULE_expr = 1
    RULE_atom = 2
    RULE_fn = 3
    RULE_taxon = 4

    ruleNames =  [ "parse", "expr", "atom", "fn", "taxon" ]

    EOF = Token.EOF
    INT=1
    REAL=2
    TRUE=3
    FALSE=4
    NOT=5
    KW_IS=6
    KW_NULL=7
    WORD=8
    STRING_CONSTANT=9
    SINGLE_QUOTED_ELEMENT=10
    L_BRACKET=11
    R_BRACKET=12
    TAXON_NAMESPACE_DELIMITER=13
    TAXON_TAG_DELIMITER=14
    FN_PARAMETER_DELIMITER=15
    OR=16
    AND=17
    EQ=18
    NEQ=19
    GT=20
    LT=21
    GTEQ=22
    LTEQ=23
    PLUS=24
    MINUS=25
    MULT=26
    DIV=27
    OPTIONAL_TAXON_OPERATOR=28
    SINGLE_LINE_COMMENT=29
    WS=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




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
        self.enterRule(localctx, 0, self.RULE_parse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.expr(0)
            self.state = 11
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


    class NullTestExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TelParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(TelParser.ExprContext,0)

        def KW_IS(self):
            return self.getToken(TelParser.KW_IS, 0)
        def KW_NULL(self):
            return self.getToken(TelParser.KW_NULL, 0)
        def NOT(self):
            return self.getToken(TelParser.NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNullTestExpr" ):
                listener.enterNullTestExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNullTestExpr" ):
                listener.exitNullTestExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNullTestExpr" ):
                return visitor.visitNullTestExpr(self)
            else:
                return visitor.visitChildren(self)


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
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TelParser.NOT]:
                localctx = TelParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 14
                self.match(TelParser.NOT)
                self.state = 15
                self.expr(6)
                pass
            elif token in [TelParser.INT, TelParser.REAL, TelParser.TRUE, TelParser.FALSE, TelParser.WORD, TelParser.STRING_CONSTANT, TelParser.SINGLE_QUOTED_ELEMENT, TelParser.L_BRACKET, TelParser.OPTIONAL_TAXON_OPERATOR]:
                localctx = TelParser.AtomExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 16
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 36
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 34
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = TelParser.MultiplicationExprContext(self, TelParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 19
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 20
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==TelParser.MULT or _la==TelParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 21
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = TelParser.AdditiveExprContext(self, TelParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 22
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 23
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==TelParser.PLUS or _la==TelParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 24
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = TelParser.LogicalExprContext(self, TelParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 25
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 26
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TelParser.OR) | (1 << TelParser.AND) | (1 << TelParser.EQ) | (1 << TelParser.NEQ) | (1 << TelParser.GT) | (1 << TelParser.LT) | (1 << TelParser.GTEQ) | (1 << TelParser.LTEQ))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 27
                        self.expr(4)
                        pass

                    elif la_ == 4:
                        localctx = TelParser.NullTestExprContext(self, TelParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 28
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 29
                        self.match(TelParser.KW_IS)
                        self.state = 31
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==TelParser.NOT:
                            self.state = 30
                            self.match(TelParser.NOT)


                        self.state = 33
                        self.match(TelParser.KW_NULL)
                        pass

             
                self.state = 38
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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

        def taxon(self):
            return self.getTypedRuleContext(TelParser.TaxonContext,0)


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
        self.enterRule(localctx, 4, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = TelParser.BracketExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(TelParser.L_BRACKET)
                self.state = 40
                self.expr(0)
                self.state = 41
                self.match(TelParser.R_BRACKET)
                pass

            elif la_ == 2:
                localctx = TelParser.NumberAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                _la = self._input.LA(1)
                if not(_la==TelParser.INT or _la==TelParser.REAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                localctx = TelParser.BooleanAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                _la = self._input.LA(1)
                if not(_la==TelParser.TRUE or _la==TelParser.FALSE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 4:
                localctx = TelParser.SingleQuotedAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.match(TelParser.SINGLE_QUOTED_ELEMENT)
                pass

            elif la_ == 5:
                localctx = TelParser.StringConstantAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 46
                self.match(TelParser.STRING_CONSTANT)
                pass

            elif la_ == 6:
                localctx = TelParser.FnExprContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 47
                self.fn()
                pass

            elif la_ == 7:
                localctx = TelParser.TaxonSlugAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 48
                self.taxon()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


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
        self.enterRule(localctx, 6, self.RULE_fn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(TelParser.WORD)
            self.state = 52
            self.match(TelParser.L_BRACKET)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TelParser.INT) | (1 << TelParser.REAL) | (1 << TelParser.TRUE) | (1 << TelParser.FALSE) | (1 << TelParser.NOT) | (1 << TelParser.WORD) | (1 << TelParser.STRING_CONSTANT) | (1 << TelParser.SINGLE_QUOTED_ELEMENT) | (1 << TelParser.L_BRACKET) | (1 << TelParser.OPTIONAL_TAXON_OPERATOR))) != 0):
                self.state = 53
                self.expr(0)


            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==TelParser.FN_PARAMETER_DELIMITER:
                self.state = 56
                self.match(TelParser.FN_PARAMETER_DELIMITER)
                self.state = 57
                self.expr(0)
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
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

        def OPTIONAL_TAXON_OPERATOR(self):
            return self.getToken(TelParser.OPTIONAL_TAXON_OPERATOR, 0)

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
        self.enterRule(localctx, 8, self.RULE_taxon)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TelParser.OPTIONAL_TAXON_OPERATOR:
                self.state = 65
                self.match(TelParser.OPTIONAL_TAXON_OPERATOR)


            self.state = 68
            self.match(TelParser.WORD)
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 69
                self.match(TelParser.TAXON_NAMESPACE_DELIMITER)
                self.state = 70
                self.match(TelParser.WORD)


            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 73
                self.match(TelParser.TAXON_TAG_DELIMITER)
                self.state = 74
                self.match(TelParser.WORD)


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
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         





# Generated from grammar/PqlParser.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\63")
        buf.write("]\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\5\3\36\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\62\n\3\f\3\16\3\65")
        buf.write("\13\3\3\4\3\4\3\4\5\4:\n\4\3\4\3\4\3\5\3\5\3\5\7\5A\n")
        buf.write("\5\f\5\16\5D\13\5\3\6\5\6G\n\6\3\6\3\6\3\6\5\6L\n\6\3")
        buf.write("\6\3\6\3\6\5\6Q\n\6\3\7\3\7\3\7\7\7V\n\7\f\7\16\7Y\13")
        buf.write("\7\3\b\3\b\3\b\2\3\4\t\2\4\6\b\n\f\16\2\n\5\2\25\25\31")
        buf.write("\31$$\5\2\22\22\26\26\34\34\4\2\25\25\31\31\4\2\5\6\23")
        buf.write("\24\6\2\4\4\7\b\r\r!!\4\2\3\3\37\37\4\2\t\t\'\'\6\2  ")
        buf.write("&&(*--\2e\2\20\3\2\2\2\4\35\3\2\2\2\6\66\3\2\2\2\b=\3")
        buf.write("\2\2\2\nF\3\2\2\2\fR\3\2\2\2\16Z\3\2\2\2\20\21\5\4\3\2")
        buf.write("\21\22\7\2\2\3\22\3\3\2\2\2\23\24\b\3\1\2\24\25\t\2\2")
        buf.write("\2\25\36\5\4\3\r\26\27\7\27\2\2\27\30\5\4\3\2\30\31\7")
        buf.write("\16\2\2\31\36\3\2\2\2\32\36\5\16\b\2\33\36\5\6\4\2\34")
        buf.write("\36\5\n\6\2\35\23\3\2\2\2\35\26\3\2\2\2\35\32\3\2\2\2")
        buf.write("\35\33\3\2\2\2\35\34\3\2\2\2\36\63\3\2\2\2\37 \f\f\2\2")
        buf.write(" !\t\3\2\2!\62\5\4\3\r\"#\f\13\2\2#$\t\4\2\2$\62\5\4\3")
        buf.write("\f%&\f\n\2\2&\'\t\5\2\2\'\62\5\4\3\13()\f\t\2\2)*\t\6")
        buf.write("\2\2*\62\5\4\3\n+,\f\b\2\2,-\t\7\2\2-\62\5\4\3\t./\f\7")
        buf.write("\2\2/\60\t\b\2\2\60\62\5\4\3\b\61\37\3\2\2\2\61\"\3\2")
        buf.write("\2\2\61%\3\2\2\2\61(\3\2\2\2\61+\3\2\2\2\61.\3\2\2\2\62")
        buf.write("\65\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64\5\3\2\2\2\65")
        buf.write("\63\3\2\2\2\66\67\5\f\7\2\679\7\27\2\28:\5\b\5\298\3\2")
        buf.write("\2\29:\3\2\2\2:;\3\2\2\2;<\7\16\2\2<\7\3\2\2\2=B\5\4\3")
        buf.write("\2>?\7\20\2\2?A\5\4\3\2@>\3\2\2\2AD\3\2\2\2B@\3\2\2\2")
        buf.write("BC\3\2\2\2C\t\3\2\2\2DB\3\2\2\2EG\7\32\2\2FE\3\2\2\2F")
        buf.write("G\3\2\2\2GK\3\2\2\2HI\5\f\7\2IJ\7\30\2\2JL\3\2\2\2KH\3")
        buf.write("\2\2\2KL\3\2\2\2LM\3\2\2\2MP\5\f\7\2NO\7\17\2\2OQ\5\f")
        buf.write("\7\2PN\3\2\2\2PQ\3\2\2\2Q\13\3\2\2\2RW\7\63\2\2ST\7\21")
        buf.write("\2\2TV\7\63\2\2US\3\2\2\2VY\3\2\2\2WU\3\2\2\2WX\3\2\2")
        buf.write("\2X\r\3\2\2\2YW\3\2\2\2Z[\t\t\2\2[\17\3\2\2\2\13\35\61")
        buf.write("\639BFKPW")
        return buf.getvalue()


class PqlParser ( Parser ):

    grammarFileName = "PqlParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'&&'", "'=='", "'>='", "'<='", "'!='", 
                     "'<>'", "'||'", "'<<'", "'>>'", "'&'", "'='", "')'", 
                     "':'", "','", "'.'", "'/'", "'>'", "'<'", "'-'", "'%'", 
                     "'('", "'|'", "'+'", "'?'", "';'", "'*'", "'~'", "'_'" ]

    symbolicNames = [ "<INVALID>", "AND", "EQ", "GT_EQ", "LT_EQ", "NOT_EQ1", 
                      "NOT_EQ2", "OR", "SHIFT_LEFT", "SHIFT_RIGHT", "AMP", 
                      "ASSIGN", "CLOSE_PAREN", "COLON", "COMMA", "DOT", 
                      "FORWARD_SLASH", "GT", "LT", "MINUS", "MOD", "OPEN_PAREN", 
                      "PIPE", "PLUS", "QUESTION_MARK", "SCOL", "STAR", "TILDE", 
                      "UNDER", "K_AND", "K_FALSE", "K_IS", "K_ISNULL", "K_LIKE", 
                      "K_NOT", "K_NOTNULL", "K_NULL", "K_OR", "K_TRUE", 
                      "NUMERIC_LITERAL", "DOUBLE_QUOTED_STRING", "DOUBLE_QUOTED_STRING_TEL", 
                      "DOUBLE_QUOTED_STRING_SQL", "SINGLE_QUOTED_STRING", 
                      "SINGLE_QUOTED_STRING_TEL", "SINGLE_QUOTED_STRING_SQL", 
                      "SINGLE_LINE_COMMENT", "MULTILINE_COMMENT", "SPACES", 
                      "WORD" ]

    RULE_parseTel = 0
    RULE_expr = 1
    RULE_fn = 2
    RULE_exprList = 3
    RULE_taxon = 4
    RULE_identifierMultipart = 5
    RULE_literalValue = 6

    ruleNames =  [ "parseTel", "expr", "fn", "exprList", "taxon", "identifierMultipart", 
                   "literalValue" ]

    EOF = Token.EOF
    AND=1
    EQ=2
    GT_EQ=3
    LT_EQ=4
    NOT_EQ1=5
    NOT_EQ2=6
    OR=7
    SHIFT_LEFT=8
    SHIFT_RIGHT=9
    AMP=10
    ASSIGN=11
    CLOSE_PAREN=12
    COLON=13
    COMMA=14
    DOT=15
    FORWARD_SLASH=16
    GT=17
    LT=18
    MINUS=19
    MOD=20
    OPEN_PAREN=21
    PIPE=22
    PLUS=23
    QUESTION_MARK=24
    SCOL=25
    STAR=26
    TILDE=27
    UNDER=28
    K_AND=29
    K_FALSE=30
    K_IS=31
    K_ISNULL=32
    K_LIKE=33
    K_NOT=34
    K_NOTNULL=35
    K_NULL=36
    K_OR=37
    K_TRUE=38
    NUMERIC_LITERAL=39
    DOUBLE_QUOTED_STRING=40
    DOUBLE_QUOTED_STRING_TEL=41
    DOUBLE_QUOTED_STRING_SQL=42
    SINGLE_QUOTED_STRING=43
    SINGLE_QUOTED_STRING_TEL=44
    SINGLE_QUOTED_STRING_SQL=45
    SINGLE_LINE_COMMENT=46
    MULTILINE_COMMENT=47
    SPACES=48
    WORD=49

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ParseTelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PqlParser.ExprContext,0)


        def EOF(self):
            return self.getToken(PqlParser.EOF, 0)

        def getRuleIndex(self):
            return PqlParser.RULE_parseTel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParseTel" ):
                listener.enterParseTel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParseTel" ):
                listener.exitParseTel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParseTel" ):
                return visitor.visitParseTel(self)
            else:
                return visitor.visitChildren(self)




    def parseTel(self):

        localctx = PqlParser.ParseTelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parseTel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.expr(0)
            self.state = 15
            self.match(PqlParser.EOF)
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
            self.left = None # ExprContext
            self.unary_operator = None # Token
            self.right = None # ExprContext
            self.inner = None # ExprContext
            self.operator = None # Token

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PqlParser.ExprContext)
            else:
                return self.getTypedRuleContext(PqlParser.ExprContext,i)


        def MINUS(self):
            return self.getToken(PqlParser.MINUS, 0)

        def PLUS(self):
            return self.getToken(PqlParser.PLUS, 0)

        def K_NOT(self):
            return self.getToken(PqlParser.K_NOT, 0)

        def OPEN_PAREN(self):
            return self.getToken(PqlParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(PqlParser.CLOSE_PAREN, 0)

        def literalValue(self):
            return self.getTypedRuleContext(PqlParser.LiteralValueContext,0)


        def fn(self):
            return self.getTypedRuleContext(PqlParser.FnContext,0)


        def taxon(self):
            return self.getTypedRuleContext(PqlParser.TaxonContext,0)


        def STAR(self):
            return self.getToken(PqlParser.STAR, 0)

        def FORWARD_SLASH(self):
            return self.getToken(PqlParser.FORWARD_SLASH, 0)

        def MOD(self):
            return self.getToken(PqlParser.MOD, 0)

        def LT(self):
            return self.getToken(PqlParser.LT, 0)

        def LT_EQ(self):
            return self.getToken(PqlParser.LT_EQ, 0)

        def GT(self):
            return self.getToken(PqlParser.GT, 0)

        def GT_EQ(self):
            return self.getToken(PqlParser.GT_EQ, 0)

        def ASSIGN(self):
            return self.getToken(PqlParser.ASSIGN, 0)

        def EQ(self):
            return self.getToken(PqlParser.EQ, 0)

        def NOT_EQ1(self):
            return self.getToken(PqlParser.NOT_EQ1, 0)

        def NOT_EQ2(self):
            return self.getToken(PqlParser.NOT_EQ2, 0)

        def K_IS(self):
            return self.getToken(PqlParser.K_IS, 0)

        def K_AND(self):
            return self.getToken(PqlParser.K_AND, 0)

        def AND(self):
            return self.getToken(PqlParser.AND, 0)

        def K_OR(self):
            return self.getToken(PqlParser.K_OR, 0)

        def OR(self):
            return self.getToken(PqlParser.OR, 0)

        def getRuleIndex(self):
            return PqlParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PqlParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 18
                localctx.unary_operator = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.MINUS) | (1 << PqlParser.PLUS) | (1 << PqlParser.K_NOT))) != 0)):
                    localctx.unary_operator = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 19
                localctx.right = self.expr(11)
                pass

            elif la_ == 2:
                self.state = 20
                self.match(PqlParser.OPEN_PAREN)
                self.state = 21
                localctx.inner = self.expr(0)
                self.state = 22
                self.match(PqlParser.CLOSE_PAREN)
                pass

            elif la_ == 3:
                self.state = 24
                self.literalValue()
                pass

            elif la_ == 4:
                self.state = 25
                self.fn()
                pass

            elif la_ == 5:
                self.state = 26
                self.taxon()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 49
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 47
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 29
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 30
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.FORWARD_SLASH) | (1 << PqlParser.MOD) | (1 << PqlParser.STAR))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 31
                        localctx.right = self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 32
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 33
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PqlParser.MINUS or _la==PqlParser.PLUS):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 34
                        localctx.right = self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 35
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 36
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.GT_EQ) | (1 << PqlParser.LT_EQ) | (1 << PqlParser.GT) | (1 << PqlParser.LT))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 37
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 38
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 39
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.EQ) | (1 << PqlParser.NOT_EQ1) | (1 << PqlParser.NOT_EQ2) | (1 << PqlParser.ASSIGN) | (1 << PqlParser.K_IS))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 40
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 5:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 41
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 42
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PqlParser.AND or _la==PqlParser.K_AND):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 43
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 6:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 44
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 45
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PqlParser.OR or _la==PqlParser.K_OR):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 46
                        localctx.right = self.expr(6)
                        pass

             
                self.state = 51
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.function_name = None # IdentifierMultipartContext
            self.arguments = None # ExprListContext

        def OPEN_PAREN(self):
            return self.getToken(PqlParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(PqlParser.CLOSE_PAREN, 0)

        def identifierMultipart(self):
            return self.getTypedRuleContext(PqlParser.IdentifierMultipartContext,0)


        def exprList(self):
            return self.getTypedRuleContext(PqlParser.ExprListContext,0)


        def getRuleIndex(self):
            return PqlParser.RULE_fn

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

        localctx = PqlParser.FnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_fn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            localctx.function_name = self.identifierMultipart()
            self.state = 53
            self.match(PqlParser.OPEN_PAREN)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.MINUS) | (1 << PqlParser.OPEN_PAREN) | (1 << PqlParser.PLUS) | (1 << PqlParser.QUESTION_MARK) | (1 << PqlParser.K_FALSE) | (1 << PqlParser.K_NOT) | (1 << PqlParser.K_NULL) | (1 << PqlParser.K_TRUE) | (1 << PqlParser.NUMERIC_LITERAL) | (1 << PqlParser.DOUBLE_QUOTED_STRING) | (1 << PqlParser.SINGLE_QUOTED_STRING) | (1 << PqlParser.WORD))) != 0):
                self.state = 54
                localctx.arguments = self.exprList()


            self.state = 57
            self.match(PqlParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PqlParser.ExprContext)
            else:
                return self.getTypedRuleContext(PqlParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PqlParser.COMMA)
            else:
                return self.getToken(PqlParser.COMMA, i)

        def getRuleIndex(self):
            return PqlParser.RULE_exprList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprList" ):
                listener.enterExprList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprList" ):
                listener.exitExprList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprList" ):
                return visitor.visitExprList(self)
            else:
                return visitor.visitChildren(self)




    def exprList(self):

        localctx = PqlParser.ExprListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.expr(0)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PqlParser.COMMA:
                self.state = 60
                self.match(PqlParser.COMMA)
                self.state = 61
                self.expr(0)
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.is_optional = None # Token
            self.namespace = None # IdentifierMultipartContext
            self.slug = None # IdentifierMultipartContext
            self.tag = None # IdentifierMultipartContext

        def identifierMultipart(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PqlParser.IdentifierMultipartContext)
            else:
                return self.getTypedRuleContext(PqlParser.IdentifierMultipartContext,i)


        def PIPE(self):
            return self.getToken(PqlParser.PIPE, 0)

        def COLON(self):
            return self.getToken(PqlParser.COLON, 0)

        def QUESTION_MARK(self):
            return self.getToken(PqlParser.QUESTION_MARK, 0)

        def getRuleIndex(self):
            return PqlParser.RULE_taxon

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

        localctx = PqlParser.TaxonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_taxon)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.QUESTION_MARK:
                self.state = 67
                localctx.is_optional = self.match(PqlParser.QUESTION_MARK)


            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 70
                localctx.namespace = self.identifierMultipart()
                self.state = 71
                self.match(PqlParser.PIPE)


            self.state = 75
            localctx.slug = self.identifierMultipart()
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 76
                self.match(PqlParser.COLON)
                self.state = 77
                localctx.tag = self.identifierMultipart()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierMultipartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self, i:int=None):
            if i is None:
                return self.getTokens(PqlParser.WORD)
            else:
                return self.getToken(PqlParser.WORD, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(PqlParser.DOT)
            else:
                return self.getToken(PqlParser.DOT, i)

        def getRuleIndex(self):
            return PqlParser.RULE_identifierMultipart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierMultipart" ):
                listener.enterIdentifierMultipart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierMultipart" ):
                listener.exitIdentifierMultipart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierMultipart" ):
                return visitor.visitIdentifierMultipart(self)
            else:
                return visitor.visitChildren(self)




    def identifierMultipart(self):

        localctx = PqlParser.IdentifierMultipartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_identifierMultipart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(PqlParser.WORD)
            self.state = 85
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 81
                    self.match(PqlParser.DOT)
                    self.state = 82
                    self.match(PqlParser.WORD) 
                self.state = 87
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERIC_LITERAL(self):
            return self.getToken(PqlParser.NUMERIC_LITERAL, 0)

        def DOUBLE_QUOTED_STRING(self):
            return self.getToken(PqlParser.DOUBLE_QUOTED_STRING, 0)

        def SINGLE_QUOTED_STRING(self):
            return self.getToken(PqlParser.SINGLE_QUOTED_STRING, 0)

        def K_NULL(self):
            return self.getToken(PqlParser.K_NULL, 0)

        def K_TRUE(self):
            return self.getToken(PqlParser.K_TRUE, 0)

        def K_FALSE(self):
            return self.getToken(PqlParser.K_FALSE, 0)

        def getRuleIndex(self):
            return PqlParser.RULE_literalValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralValue" ):
                listener.enterLiteralValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralValue" ):
                listener.exitLiteralValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralValue" ):
                return visitor.visitLiteralValue(self)
            else:
                return visitor.visitChildren(self)




    def literalValue(self):

        localctx = PqlParser.LiteralValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_literalValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.K_FALSE) | (1 << PqlParser.K_NULL) | (1 << PqlParser.K_TRUE) | (1 << PqlParser.NUMERIC_LITERAL) | (1 << PqlParser.DOUBLE_QUOTED_STRING) | (1 << PqlParser.SINGLE_QUOTED_STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         





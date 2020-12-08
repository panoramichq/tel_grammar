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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\66")
        buf.write("\u0084\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\5\3\"\n\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\62\n\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3>\n\3\3\3\3\3\3\3")
        buf.write("\3\3\5\3D\n\3\3\3\3\3\3\3\3\3\3\3\7\3K\n\3\f\3\16\3N\13")
        buf.write("\3\3\4\3\4\3\4\7\4S\n\4\f\4\16\4V\13\4\3\5\3\5\3\5\5\5")
        buf.write("[\n\5\3\5\3\5\3\6\3\6\3\6\7\6b\n\6\f\6\16\6e\13\6\3\7")
        buf.write("\3\7\5\7i\n\7\3\7\3\7\3\b\5\bn\n\b\3\b\3\b\3\b\5\bs\n")
        buf.write("\b\3\b\3\b\3\b\5\bx\n\b\3\t\3\t\3\t\7\t}\n\t\f\t\16\t")
        buf.write("\u0080\13\t\3\n\3\n\3\n\2\3\4\13\2\4\6\b\n\f\16\20\22")
        buf.write("\2\13\5\2\25\25\31\31\'\'\5\2\22\22\26\26\34\34\4\2\25")
        buf.write("\25\31\31\4\2\5\6\23\24\6\2\4\4\7\b\r\r$$\4\2\"\"&&\4")
        buf.write("\2\3\3\37\37\4\2\t\t**\6\2!!))+-\60\60\2\u0092\2\24\3")
        buf.write("\2\2\2\4!\3\2\2\2\6O\3\2\2\2\bW\3\2\2\2\n^\3\2\2\2\fh")
        buf.write("\3\2\2\2\16m\3\2\2\2\20y\3\2\2\2\22\u0081\3\2\2\2\24\25")
        buf.write("\5\4\3\2\25\26\7\2\2\3\26\3\3\2\2\2\27\30\b\3\1\2\30\31")
        buf.write("\t\2\2\2\31\"\5\4\3\20\32\33\7\27\2\2\33\34\5\4\3\2\34")
        buf.write("\35\7\16\2\2\35\"\3\2\2\2\36\"\5\22\n\2\37\"\5\b\5\2 ")
        buf.write("\"\5\16\b\2!\27\3\2\2\2!\32\3\2\2\2!\36\3\2\2\2!\37\3")
        buf.write("\2\2\2! \3\2\2\2\"L\3\2\2\2#$\f\17\2\2$%\t\3\2\2%K\5\4")
        buf.write("\3\20&\'\f\16\2\2\'(\t\4\2\2(K\5\4\3\17)*\f\r\2\2*+\t")
        buf.write("\5\2\2+K\5\4\3\16,-\f\f\2\2-.\t\6\2\2.K\5\4\3\r/\61\f")
        buf.write("\13\2\2\60\62\7\'\2\2\61\60\3\2\2\2\61\62\3\2\2\2\62\63")
        buf.write("\3\2\2\2\63\64\t\7\2\2\64K\5\4\3\f\65\66\f\t\2\2\66\67")
        buf.write("\t\b\2\2\67K\5\4\3\n89\f\b\2\29:\t\t\2\2:K\5\4\3\t;=\f")
        buf.write("\7\2\2<>\7\'\2\2=<\3\2\2\2=>\3\2\2\2>?\3\2\2\2?@\7 \2")
        buf.write("\2@K\5\4\3\bAC\f\n\2\2BD\7\'\2\2CB\3\2\2\2CD\3\2\2\2D")
        buf.write("E\3\2\2\2EF\7#\2\2FG\7\27\2\2GH\5\6\4\2HI\7\16\2\2IK\3")
        buf.write("\2\2\2J#\3\2\2\2J&\3\2\2\2J)\3\2\2\2J,\3\2\2\2J/\3\2\2")
        buf.write("\2J\65\3\2\2\2J8\3\2\2\2J;\3\2\2\2JA\3\2\2\2KN\3\2\2\2")
        buf.write("LJ\3\2\2\2LM\3\2\2\2M\5\3\2\2\2NL\3\2\2\2OT\5\4\3\2PQ")
        buf.write("\7\20\2\2QS\5\4\3\2RP\3\2\2\2SV\3\2\2\2TR\3\2\2\2TU\3")
        buf.write("\2\2\2U\7\3\2\2\2VT\3\2\2\2WX\5\20\t\2XZ\7\27\2\2Y[\5")
        buf.write("\n\6\2ZY\3\2\2\2Z[\3\2\2\2[\\\3\2\2\2\\]\7\16\2\2]\t\3")
        buf.write("\2\2\2^c\5\f\7\2_`\7\20\2\2`b\5\f\7\2a_\3\2\2\2be\3\2")
        buf.write("\2\2ca\3\2\2\2cd\3\2\2\2d\13\3\2\2\2ec\3\2\2\2fg\7\66")
        buf.write("\2\2gi\7\r\2\2hf\3\2\2\2hi\3\2\2\2ij\3\2\2\2jk\5\4\3\2")
        buf.write("k\r\3\2\2\2ln\7\32\2\2ml\3\2\2\2mn\3\2\2\2nr\3\2\2\2o")
        buf.write("p\5\20\t\2pq\7\30\2\2qs\3\2\2\2ro\3\2\2\2rs\3\2\2\2st")
        buf.write("\3\2\2\2tw\5\20\t\2uv\7\17\2\2vx\5\20\t\2wu\3\2\2\2wx")
        buf.write("\3\2\2\2x\17\3\2\2\2y~\7\66\2\2z{\7\21\2\2{}\7\66\2\2")
        buf.write("|z\3\2\2\2}\u0080\3\2\2\2~|\3\2\2\2~\177\3\2\2\2\177\21")
        buf.write("\3\2\2\2\u0080~\3\2\2\2\u0081\u0082\t\n\2\2\u0082\23\3")
        buf.write("\2\2\2\20!\61=CJLTZchmrw~")
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
                      "UNDER", "K_AND", "K_BETWEEN", "K_FALSE", "K_ILIKE", 
                      "K_IN", "K_IS", "K_ISNULL", "K_LIKE", "K_NOT", "K_NOTNULL", 
                      "K_NULL", "K_OR", "K_TRUE", "NUMERIC_LITERAL", "DOUBLE_QUOTED_STRING", 
                      "DOUBLE_QUOTED_STRING_TEL", "DOUBLE_QUOTED_STRING_SQL", 
                      "SINGLE_QUOTED_STRING", "SINGLE_QUOTED_STRING_TEL", 
                      "SINGLE_QUOTED_STRING_SQL", "SINGLE_LINE_COMMENT", 
                      "MULTILINE_COMMENT", "SPACES", "WORD" ]

    RULE_parseTel = 0
    RULE_expr = 1
    RULE_exprList = 2
    RULE_fn = 3
    RULE_fnArgs = 4
    RULE_fnArg = 5
    RULE_taxon = 6
    RULE_identifierMultipart = 7
    RULE_literalValue = 8

    ruleNames =  [ "parseTel", "expr", "exprList", "fn", "fnArgs", "fnArg", 
                   "taxon", "identifierMultipart", "literalValue" ]

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
    K_BETWEEN=30
    K_FALSE=31
    K_ILIKE=32
    K_IN=33
    K_IS=34
    K_ISNULL=35
    K_LIKE=36
    K_NOT=37
    K_NOTNULL=38
    K_NULL=39
    K_OR=40
    K_TRUE=41
    NUMERIC_LITERAL=42
    DOUBLE_QUOTED_STRING=43
    DOUBLE_QUOTED_STRING_TEL=44
    DOUBLE_QUOTED_STRING_SQL=45
    SINGLE_QUOTED_STRING=46
    SINGLE_QUOTED_STRING_TEL=47
    SINGLE_QUOTED_STRING_SQL=48
    SINGLE_LINE_COMMENT=49
    MULTILINE_COMMENT=50
    SPACES=51
    WORD=52

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
            self.state = 18
            self.expr(0)
            self.state = 19
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
            self.is_negated = None # Token
            self.right_list = None # ExprListContext

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

        def K_LIKE(self):
            return self.getToken(PqlParser.K_LIKE, 0)

        def K_ILIKE(self):
            return self.getToken(PqlParser.K_ILIKE, 0)

        def K_AND(self):
            return self.getToken(PqlParser.K_AND, 0)

        def AND(self):
            return self.getToken(PqlParser.AND, 0)

        def K_OR(self):
            return self.getToken(PqlParser.K_OR, 0)

        def OR(self):
            return self.getToken(PqlParser.OR, 0)

        def K_BETWEEN(self):
            return self.getToken(PqlParser.K_BETWEEN, 0)

        def K_IN(self):
            return self.getToken(PqlParser.K_IN, 0)

        def exprList(self):
            return self.getTypedRuleContext(PqlParser.ExprListContext,0)


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
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 22
                localctx.unary_operator = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.MINUS) | (1 << PqlParser.PLUS) | (1 << PqlParser.K_NOT))) != 0)):
                    localctx.unary_operator = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 23
                localctx.right = self.expr(14)
                pass

            elif la_ == 2:
                self.state = 24
                self.match(PqlParser.OPEN_PAREN)
                self.state = 25
                localctx.inner = self.expr(0)
                self.state = 26
                self.match(PqlParser.CLOSE_PAREN)
                pass

            elif la_ == 3:
                self.state = 28
                self.literalValue()
                pass

            elif la_ == 4:
                self.state = 29
                self.fn()
                pass

            elif la_ == 5:
                self.state = 30
                self.taxon()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 74
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 72
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 33
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 34
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.FORWARD_SLASH) | (1 << PqlParser.MOD) | (1 << PqlParser.STAR))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 35
                        localctx.right = self.expr(14)
                        pass

                    elif la_ == 2:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 36
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 37
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PqlParser.MINUS or _la==PqlParser.PLUS):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 38
                        localctx.right = self.expr(13)
                        pass

                    elif la_ == 3:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 39
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 40
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.GT_EQ) | (1 << PqlParser.LT_EQ) | (1 << PqlParser.GT) | (1 << PqlParser.LT))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 41
                        localctx.right = self.expr(12)
                        pass

                    elif la_ == 4:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 42
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 43
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.EQ) | (1 << PqlParser.NOT_EQ1) | (1 << PqlParser.NOT_EQ2) | (1 << PqlParser.ASSIGN) | (1 << PqlParser.K_IS))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 44
                        localctx.right = self.expr(11)
                        pass

                    elif la_ == 5:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 45
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 47
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==PqlParser.K_NOT:
                            self.state = 46
                            localctx.is_negated = self.match(PqlParser.K_NOT)


                        self.state = 49
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PqlParser.K_ILIKE or _la==PqlParser.K_LIKE):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 50
                        localctx.right = self.expr(10)
                        pass

                    elif la_ == 6:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 51
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 52
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PqlParser.AND or _la==PqlParser.K_AND):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 53
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 7:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 54
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 55
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PqlParser.OR or _la==PqlParser.K_OR):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 56
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 8:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 57
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 59
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==PqlParser.K_NOT:
                            self.state = 58
                            localctx.is_negated = self.match(PqlParser.K_NOT)


                        self.state = 61
                        localctx.operator = self.match(PqlParser.K_BETWEEN)
                        self.state = 62
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 9:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 63
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 65
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==PqlParser.K_NOT:
                            self.state = 64
                            localctx.is_negated = self.match(PqlParser.K_NOT)


                        self.state = 67
                        localctx.operator = self.match(PqlParser.K_IN)
                        self.state = 68
                        self.match(PqlParser.OPEN_PAREN)
                        self.state = 69
                        localctx.right_list = self.exprList()
                        self.state = 70
                        self.match(PqlParser.CLOSE_PAREN)
                        pass

             
                self.state = 76
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 4, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.expr(0)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PqlParser.COMMA:
                self.state = 78
                self.match(PqlParser.COMMA)
                self.state = 79
                self.expr(0)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            self.function_name = None # IdentifierMultipartContext
            self.arguments = None # FnArgsContext

        def OPEN_PAREN(self):
            return self.getToken(PqlParser.OPEN_PAREN, 0)

        def CLOSE_PAREN(self):
            return self.getToken(PqlParser.CLOSE_PAREN, 0)

        def identifierMultipart(self):
            return self.getTypedRuleContext(PqlParser.IdentifierMultipartContext,0)


        def fnArgs(self):
            return self.getTypedRuleContext(PqlParser.FnArgsContext,0)


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
        self.enterRule(localctx, 6, self.RULE_fn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            localctx.function_name = self.identifierMultipart()
            self.state = 86
            self.match(PqlParser.OPEN_PAREN)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.MINUS) | (1 << PqlParser.OPEN_PAREN) | (1 << PqlParser.PLUS) | (1 << PqlParser.QUESTION_MARK) | (1 << PqlParser.K_FALSE) | (1 << PqlParser.K_NOT) | (1 << PqlParser.K_NULL) | (1 << PqlParser.K_TRUE) | (1 << PqlParser.NUMERIC_LITERAL) | (1 << PqlParser.DOUBLE_QUOTED_STRING) | (1 << PqlParser.SINGLE_QUOTED_STRING) | (1 << PqlParser.WORD))) != 0):
                self.state = 87
                localctx.arguments = self.fnArgs()


            self.state = 90
            self.match(PqlParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FnArgsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fnArg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PqlParser.FnArgContext)
            else:
                return self.getTypedRuleContext(PqlParser.FnArgContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PqlParser.COMMA)
            else:
                return self.getToken(PqlParser.COMMA, i)

        def getRuleIndex(self):
            return PqlParser.RULE_fnArgs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFnArgs" ):
                listener.enterFnArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFnArgs" ):
                listener.exitFnArgs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFnArgs" ):
                return visitor.visitFnArgs(self)
            else:
                return visitor.visitChildren(self)




    def fnArgs(self):

        localctx = PqlParser.FnArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_fnArgs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.fnArg()
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PqlParser.COMMA:
                self.state = 93
                self.match(PqlParser.COMMA)
                self.state = 94
                self.fnArg()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FnArgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.argument_name = None # Token
            self.argument_value = None # ExprContext

        def expr(self):
            return self.getTypedRuleContext(PqlParser.ExprContext,0)


        def ASSIGN(self):
            return self.getToken(PqlParser.ASSIGN, 0)

        def WORD(self):
            return self.getToken(PqlParser.WORD, 0)

        def getRuleIndex(self):
            return PqlParser.RULE_fnArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFnArg" ):
                listener.enterFnArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFnArg" ):
                listener.exitFnArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFnArg" ):
                return visitor.visitFnArg(self)
            else:
                return visitor.visitChildren(self)




    def fnArg(self):

        localctx = PqlParser.FnArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_fnArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 100
                localctx.argument_name = self.match(PqlParser.WORD)
                self.state = 101
                self.match(PqlParser.ASSIGN)


            self.state = 104
            localctx.argument_value = self.expr(0)
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
        self.enterRule(localctx, 12, self.RULE_taxon)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.QUESTION_MARK:
                self.state = 106
                localctx.is_optional = self.match(PqlParser.QUESTION_MARK)


            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 109
                localctx.namespace = self.identifierMultipart()
                self.state = 110
                self.match(PqlParser.PIPE)


            self.state = 114
            localctx.slug = self.identifierMultipart()
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 115
                self.match(PqlParser.COLON)
                self.state = 116
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
        self.enterRule(localctx, 14, self.RULE_identifierMultipart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(PqlParser.WORD)
            self.state = 124
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 120
                    self.match(PqlParser.DOT)
                    self.state = 121
                    self.match(PqlParser.WORD) 
                self.state = 126
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        self.enterRule(localctx, 16, self.RULE_literalValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
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
                return self.precpred(self._ctx, 13)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 8)
         





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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3<")
        buf.write("\u00cd\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\3\2\3\3\7\3+\n\3\f\3\16\3.\13\3\3\3\3\3\3\4\7")
        buf.write("\4\63\n\4\f\4\16\4\66\13\4\3\4\3\4\6\4:\n\4\r\4\16\4;")
        buf.write("\3\4\7\4?\n\4\f\4\16\4B\13\4\3\4\7\4E\n\4\f\4\16\4H\13")
        buf.write("\4\3\5\3\5\5\5L\n\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\5\7U\n")
        buf.write("\7\3\7\5\7X\n\7\3\7\5\7[\n\7\3\b\3\b\3\b\3\b\7\ba\n\b")
        buf.write("\f\b\16\bd\13\b\3\t\3\t\3\t\3\t\5\tj\n\t\3\t\3\t\5\tn")
        buf.write("\n\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\7\13x\n\13\f")
        buf.write("\13\16\13{\13\13\3\f\3\f\5\f\177\n\f\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u008e")
        buf.write("\n\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\7\16\u00a2\n")
        buf.write("\16\f\16\16\16\u00a5\13\16\3\17\3\17\3\17\5\17\u00aa\n")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\7\20\u00b1\n\20\f\20\16\20")
        buf.write("\u00b4\13\20\3\21\5\21\u00b7\n\21\3\21\3\21\3\21\5\21")
        buf.write("\u00bc\n\21\3\21\3\21\3\21\5\21\u00c1\n\21\3\22\3\22\3")
        buf.write("\22\7\22\u00c6\n\22\f\22\16\22\u00c9\13\22\3\23\3\23\3")
        buf.write("\23\2\3\32\24\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 ")
        buf.write("\"$\2\13\4\2!!##\5\2\25\25\31\31))\5\2\22\22\26\26\34")
        buf.write("\34\4\2\25\25\31\31\4\2\5\6\23\24\6\2\4\4\7\b\r\r%%\4")
        buf.write("\2\3\3\37\37\4\2\t\t,,\7\2$$++\60\60\62\63\66\66\2\u00d8")
        buf.write("\2&\3\2\2\2\4,\3\2\2\2\6\64\3\2\2\2\bK\3\2\2\2\nM\3\2")
        buf.write("\2\2\fR\3\2\2\2\16\\\3\2\2\2\20e\3\2\2\2\22o\3\2\2\2\24")
        buf.write("r\3\2\2\2\26|\3\2\2\2\30\u0080\3\2\2\2\32\u008d\3\2\2")
        buf.write("\2\34\u00a6\3\2\2\2\36\u00ad\3\2\2\2 \u00b6\3\2\2\2\"")
        buf.write("\u00c2\3\2\2\2$\u00ca\3\2\2\2&\'\5\32\16\2\'(\7\2\2\3")
        buf.write("(\3\3\2\2\2)+\5\6\4\2*)\3\2\2\2+.\3\2\2\2,*\3\2\2\2,-")
        buf.write("\3\2\2\2-/\3\2\2\2.,\3\2\2\2/\60\7\2\2\3\60\5\3\2\2\2")
        buf.write("\61\63\7\33\2\2\62\61\3\2\2\2\63\66\3\2\2\2\64\62\3\2")
        buf.write("\2\2\64\65\3\2\2\2\65\67\3\2\2\2\66\64\3\2\2\2\67@\5\b")
        buf.write("\5\28:\7\33\2\298\3\2\2\2:;\3\2\2\2;9\3\2\2\2;<\3\2\2")
        buf.write("\2<=\3\2\2\2=?\5\b\5\2>9\3\2\2\2?B\3\2\2\2@>\3\2\2\2@")
        buf.write("A\3\2\2\2AF\3\2\2\2B@\3\2\2\2CE\7\33\2\2DC\3\2\2\2EH\3")
        buf.write("\2\2\2FD\3\2\2\2FG\3\2\2\2G\7\3\2\2\2HF\3\2\2\2IL\5\n")
        buf.write("\6\2JL\5\f\7\2KI\3\2\2\2KJ\3\2\2\2L\t\3\2\2\2MN\7/\2\2")
        buf.write("NO\5\"\22\2OP\7\r\2\2PQ\5\32\16\2Q\13\3\2\2\2RT\5\16\b")
        buf.write("\2SU\5\22\n\2TS\3\2\2\2TU\3\2\2\2UW\3\2\2\2VX\5\24\13")
        buf.write("\2WV\3\2\2\2WX\3\2\2\2XZ\3\2\2\2Y[\5\30\r\2ZY\3\2\2\2")
        buf.write("Z[\3\2\2\2[\r\3\2\2\2\\]\7.\2\2]b\5\20\t\2^_\7\20\2\2")
        buf.write("_a\5\20\t\2`^\3\2\2\2ad\3\2\2\2b`\3\2\2\2bc\3\2\2\2c\17")
        buf.write("\3\2\2\2db\3\2\2\2ei\5\32\16\2fg\7\17\2\2gh\7\17\2\2h")
        buf.write("j\5\34\17\2if\3\2\2\2ij\3\2\2\2jm\3\2\2\2kl\7 \2\2ln\5")
        buf.write(" \21\2mk\3\2\2\2mn\3\2\2\2n\21\3\2\2\2op\7\61\2\2pq\5")
        buf.write("\32\16\2q\23\3\2\2\2rs\7-\2\2st\7\"\2\2ty\5\26\f\2uv\7")
        buf.write("\20\2\2vx\5\26\f\2wu\3\2\2\2x{\3\2\2\2yw\3\2\2\2yz\3\2")
        buf.write("\2\2z\25\3\2\2\2{y\3\2\2\2|~\5\32\16\2}\177\t\2\2\2~}")
        buf.write("\3\2\2\2~\177\3\2\2\2\177\27\3\2\2\2\u0080\u0081\7(\2")
        buf.write("\2\u0081\u0082\5\32\16\2\u0082\31\3\2\2\2\u0083\u0084")
        buf.write("\b\16\1\2\u0084\u0085\t\3\2\2\u0085\u008e\5\32\16\r\u0086")
        buf.write("\u0087\7\27\2\2\u0087\u0088\5\32\16\2\u0088\u0089\7\16")
        buf.write("\2\2\u0089\u008e\3\2\2\2\u008a\u008e\5$\23\2\u008b\u008e")
        buf.write("\5\34\17\2\u008c\u008e\5 \21\2\u008d\u0083\3\2\2\2\u008d")
        buf.write("\u0086\3\2\2\2\u008d\u008a\3\2\2\2\u008d\u008b\3\2\2\2")
        buf.write("\u008d\u008c\3\2\2\2\u008e\u00a3\3\2\2\2\u008f\u0090\f")
        buf.write("\f\2\2\u0090\u0091\t\4\2\2\u0091\u00a2\5\32\16\r\u0092")
        buf.write("\u0093\f\13\2\2\u0093\u0094\t\5\2\2\u0094\u00a2\5\32\16")
        buf.write("\f\u0095\u0096\f\n\2\2\u0096\u0097\t\6\2\2\u0097\u00a2")
        buf.write("\5\32\16\13\u0098\u0099\f\t\2\2\u0099\u009a\t\7\2\2\u009a")
        buf.write("\u00a2\5\32\16\n\u009b\u009c\f\b\2\2\u009c\u009d\t\b\2")
        buf.write("\2\u009d\u00a2\5\32\16\t\u009e\u009f\f\7\2\2\u009f\u00a0")
        buf.write("\t\t\2\2\u00a0\u00a2\5\32\16\b\u00a1\u008f\3\2\2\2\u00a1")
        buf.write("\u0092\3\2\2\2\u00a1\u0095\3\2\2\2\u00a1\u0098\3\2\2\2")
        buf.write("\u00a1\u009b\3\2\2\2\u00a1\u009e\3\2\2\2\u00a2\u00a5\3")
        buf.write("\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\33")
        buf.write("\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a7\5\"\22\2\u00a7")
        buf.write("\u00a9\7\27\2\2\u00a8\u00aa\5\36\20\2\u00a9\u00a8\3\2")
        buf.write("\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\u00ac")
        buf.write("\7\16\2\2\u00ac\35\3\2\2\2\u00ad\u00b2\5\32\16\2\u00ae")
        buf.write("\u00af\7\20\2\2\u00af\u00b1\5\32\16\2\u00b0\u00ae\3\2")
        buf.write("\2\2\u00b1\u00b4\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3")
        buf.write("\3\2\2\2\u00b3\37\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b5\u00b7")
        buf.write("\7\32\2\2\u00b6\u00b5\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7")
        buf.write("\u00bb\3\2\2\2\u00b8\u00b9\5\"\22\2\u00b9\u00ba\7\30\2")
        buf.write("\2\u00ba\u00bc\3\2\2\2\u00bb\u00b8\3\2\2\2\u00bb\u00bc")
        buf.write("\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00c0\5\"\22\2\u00be")
        buf.write("\u00bf\7\17\2\2\u00bf\u00c1\5\"\22\2\u00c0\u00be\3\2\2")
        buf.write("\2\u00c0\u00c1\3\2\2\2\u00c1!\3\2\2\2\u00c2\u00c7\7<\2")
        buf.write("\2\u00c3\u00c4\7\21\2\2\u00c4\u00c6\7<\2\2\u00c5\u00c3")
        buf.write("\3\2\2\2\u00c6\u00c9\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7")
        buf.write("\u00c8\3\2\2\2\u00c8#\3\2\2\2\u00c9\u00c7\3\2\2\2\u00ca")
        buf.write("\u00cb\t\n\2\2\u00cb%\3\2\2\2\31,\64;@FKTWZbimy~\u008d")
        buf.write("\u00a1\u00a3\u00a9\u00b2\u00b6\u00bb\u00c0\u00c7")
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
                      "UNDER", "K_AND", "K_AS", "K_ASC", "K_BY", "K_DESC", 
                      "K_FALSE", "K_IS", "K_ISNULL", "K_LIKE", "K_LIMIT", 
                      "K_NOT", "K_NOTNULL", "K_NULL", "K_OR", "K_ORDER", 
                      "K_SELECT", "K_SET", "K_TRUE", "K_WHERE", "NUMERIC_LITERAL", 
                      "DOUBLE_QUOTED_STRING", "DOUBLE_QUOTED_STRING_TEL", 
                      "DOUBLE_QUOTED_STRING_SQL", "SINGLE_QUOTED_STRING", 
                      "SINGLE_QUOTED_STRING_TEL", "SINGLE_QUOTED_STRING_SQL", 
                      "SINGLE_LINE_COMMENT", "MULTILINE_COMMENT", "SPACES", 
                      "WORD" ]

    RULE_parseTel = 0
    RULE_parsePql = 1
    RULE_sqlStmtList = 2
    RULE_sqlStmt = 3
    RULE_setStmt = 4
    RULE_selectStmt = 5
    RULE_selectClause = 6
    RULE_columns = 7
    RULE_whereClause = 8
    RULE_orderByClause = 9
    RULE_orderExpr = 10
    RULE_limitClause = 11
    RULE_expr = 12
    RULE_function = 13
    RULE_exprList = 14
    RULE_taxon = 15
    RULE_identifierMultipart = 16
    RULE_literalValue = 17

    ruleNames =  [ "parseTel", "parsePql", "sqlStmtList", "sqlStmt", "setStmt", 
                   "selectStmt", "selectClause", "columns", "whereClause", 
                   "orderByClause", "orderExpr", "limitClause", "expr", 
                   "function", "exprList", "taxon", "identifierMultipart", 
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
    K_AS=30
    K_ASC=31
    K_BY=32
    K_DESC=33
    K_FALSE=34
    K_IS=35
    K_ISNULL=36
    K_LIKE=37
    K_LIMIT=38
    K_NOT=39
    K_NOTNULL=40
    K_NULL=41
    K_OR=42
    K_ORDER=43
    K_SELECT=44
    K_SET=45
    K_TRUE=46
    K_WHERE=47
    NUMERIC_LITERAL=48
    DOUBLE_QUOTED_STRING=49
    DOUBLE_QUOTED_STRING_TEL=50
    DOUBLE_QUOTED_STRING_SQL=51
    SINGLE_QUOTED_STRING=52
    SINGLE_QUOTED_STRING_TEL=53
    SINGLE_QUOTED_STRING_SQL=54
    SINGLE_LINE_COMMENT=55
    MULTILINE_COMMENT=56
    SPACES=57
    WORD=58

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
            self.state = 36
            self.expr(0)
            self.state = 37
            self.match(PqlParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParsePqlContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PqlParser.EOF, 0)

        def sqlStmtList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PqlParser.SqlStmtListContext)
            else:
                return self.getTypedRuleContext(PqlParser.SqlStmtListContext,i)


        def getRuleIndex(self):
            return PqlParser.RULE_parsePql

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParsePql" ):
                listener.enterParsePql(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParsePql" ):
                listener.exitParsePql(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParsePql" ):
                return visitor.visitParsePql(self)
            else:
                return visitor.visitChildren(self)




    def parsePql(self):

        localctx = PqlParser.ParsePqlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_parsePql)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.SCOL) | (1 << PqlParser.K_SELECT) | (1 << PqlParser.K_SET))) != 0):
                self.state = 39
                self.sqlStmtList()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self.match(PqlParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SqlStmtListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sqlStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PqlParser.SqlStmtContext)
            else:
                return self.getTypedRuleContext(PqlParser.SqlStmtContext,i)


        def SCOL(self, i:int=None):
            if i is None:
                return self.getTokens(PqlParser.SCOL)
            else:
                return self.getToken(PqlParser.SCOL, i)

        def getRuleIndex(self):
            return PqlParser.RULE_sqlStmtList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSqlStmtList" ):
                listener.enterSqlStmtList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSqlStmtList" ):
                listener.exitSqlStmtList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSqlStmtList" ):
                return visitor.visitSqlStmtList(self)
            else:
                return visitor.visitChildren(self)




    def sqlStmtList(self):

        localctx = PqlParser.SqlStmtListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sqlStmtList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PqlParser.SCOL:
                self.state = 47
                self.match(PqlParser.SCOL)
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
            self.sqlStmt()
            self.state = 62
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 55 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 54
                        self.match(PqlParser.SCOL)
                        self.state = 57 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==PqlParser.SCOL):
                            break

                    self.state = 59
                    self.sqlStmt() 
                self.state = 64
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 68
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 65
                    self.match(PqlParser.SCOL) 
                self.state = 70
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SqlStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def setStmt(self):
            return self.getTypedRuleContext(PqlParser.SetStmtContext,0)


        def selectStmt(self):
            return self.getTypedRuleContext(PqlParser.SelectStmtContext,0)


        def getRuleIndex(self):
            return PqlParser.RULE_sqlStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSqlStmt" ):
                listener.enterSqlStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSqlStmt" ):
                listener.exitSqlStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSqlStmt" ):
                return visitor.visitSqlStmt(self)
            else:
                return visitor.visitChildren(self)




    def sqlStmt(self):

        localctx = PqlParser.SqlStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_sqlStmt)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PqlParser.K_SET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.setStmt()
                pass
            elif token in [PqlParser.K_SELECT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.selectStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.key = None # IdentifierMultipartContext
            self.values = None # ExprContext

        def K_SET(self):
            return self.getToken(PqlParser.K_SET, 0)

        def ASSIGN(self):
            return self.getToken(PqlParser.ASSIGN, 0)

        def identifierMultipart(self):
            return self.getTypedRuleContext(PqlParser.IdentifierMultipartContext,0)


        def expr(self):
            return self.getTypedRuleContext(PqlParser.ExprContext,0)


        def getRuleIndex(self):
            return PqlParser.RULE_setStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetStmt" ):
                listener.enterSetStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetStmt" ):
                listener.exitSetStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetStmt" ):
                return visitor.visitSetStmt(self)
            else:
                return visitor.visitChildren(self)




    def setStmt(self):

        localctx = PqlParser.SetStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_setStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(PqlParser.K_SET)
            self.state = 76
            localctx.key = self.identifierMultipart()
            self.state = 77
            self.match(PqlParser.ASSIGN)
            self.state = 78
            localctx.values = self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def selectClause(self):
            return self.getTypedRuleContext(PqlParser.SelectClauseContext,0)


        def whereClause(self):
            return self.getTypedRuleContext(PqlParser.WhereClauseContext,0)


        def orderByClause(self):
            return self.getTypedRuleContext(PqlParser.OrderByClauseContext,0)


        def limitClause(self):
            return self.getTypedRuleContext(PqlParser.LimitClauseContext,0)


        def getRuleIndex(self):
            return PqlParser.RULE_selectStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectStmt" ):
                listener.enterSelectStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectStmt" ):
                listener.exitSelectStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectStmt" ):
                return visitor.visitSelectStmt(self)
            else:
                return visitor.visitChildren(self)




    def selectStmt(self):

        localctx = PqlParser.SelectStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_selectStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.selectClause()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.K_WHERE:
                self.state = 81
                self.whereClause()


            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.K_ORDER:
                self.state = 84
                self.orderByClause()


            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.K_LIMIT:
                self.state = 87
                self.limitClause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectClauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_SELECT(self):
            return self.getToken(PqlParser.K_SELECT, 0)

        def columns(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PqlParser.ColumnsContext)
            else:
                return self.getTypedRuleContext(PqlParser.ColumnsContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PqlParser.COMMA)
            else:
                return self.getToken(PqlParser.COMMA, i)

        def getRuleIndex(self):
            return PqlParser.RULE_selectClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectClause" ):
                listener.enterSelectClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectClause" ):
                listener.exitSelectClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectClause" ):
                return visitor.visitSelectClause(self)
            else:
                return visitor.visitChildren(self)




    def selectClause(self):

        localctx = PqlParser.SelectClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_selectClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(PqlParser.K_SELECT)
            self.state = 91
            self.columns()
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PqlParser.COMMA:
                self.state = 92
                self.match(PqlParser.COMMA)
                self.state = 93
                self.columns()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None # ExprContext
            self.type_cast = None # FunctionContext
            self.alias = None # TaxonContext

        def expr(self):
            return self.getTypedRuleContext(PqlParser.ExprContext,0)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(PqlParser.COLON)
            else:
                return self.getToken(PqlParser.COLON, i)

        def K_AS(self):
            return self.getToken(PqlParser.K_AS, 0)

        def function(self):
            return self.getTypedRuleContext(PqlParser.FunctionContext,0)


        def taxon(self):
            return self.getTypedRuleContext(PqlParser.TaxonContext,0)


        def getRuleIndex(self):
            return PqlParser.RULE_columns

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumns" ):
                listener.enterColumns(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumns" ):
                listener.exitColumns(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumns" ):
                return visitor.visitColumns(self)
            else:
                return visitor.visitChildren(self)




    def columns(self):

        localctx = PqlParser.ColumnsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_columns)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            localctx.value = self.expr(0)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.COLON:
                self.state = 100
                self.match(PqlParser.COLON)
                self.state = 101
                self.match(PqlParser.COLON)
                self.state = 102
                localctx.type_cast = self.function()


            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.K_AS:
                self.state = 105
                self.match(PqlParser.K_AS)
                self.state = 106
                localctx.alias = self.taxon()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhereClauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_WHERE(self):
            return self.getToken(PqlParser.K_WHERE, 0)

        def expr(self):
            return self.getTypedRuleContext(PqlParser.ExprContext,0)


        def getRuleIndex(self):
            return PqlParser.RULE_whereClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhereClause" ):
                listener.enterWhereClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhereClause" ):
                listener.exitWhereClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhereClause" ):
                return visitor.visitWhereClause(self)
            else:
                return visitor.visitChildren(self)




    def whereClause(self):

        localctx = PqlParser.WhereClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whereClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(PqlParser.K_WHERE)
            self.state = 110
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderByClauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_ORDER(self):
            return self.getToken(PqlParser.K_ORDER, 0)

        def K_BY(self):
            return self.getToken(PqlParser.K_BY, 0)

        def orderExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PqlParser.OrderExprContext)
            else:
                return self.getTypedRuleContext(PqlParser.OrderExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PqlParser.COMMA)
            else:
                return self.getToken(PqlParser.COMMA, i)

        def getRuleIndex(self):
            return PqlParser.RULE_orderByClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderByClause" ):
                listener.enterOrderByClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderByClause" ):
                listener.exitOrderByClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderByClause" ):
                return visitor.visitOrderByClause(self)
            else:
                return visitor.visitChildren(self)




    def orderByClause(self):

        localctx = PqlParser.OrderByClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_orderByClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(PqlParser.K_ORDER)
            self.state = 113
            self.match(PqlParser.K_BY)
            self.state = 114
            self.orderExpr()
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PqlParser.COMMA:
                self.state = 115
                self.match(PqlParser.COMMA)
                self.state = 116
                self.orderExpr()
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PqlParser.ExprContext,0)


        def K_ASC(self):
            return self.getToken(PqlParser.K_ASC, 0)

        def K_DESC(self):
            return self.getToken(PqlParser.K_DESC, 0)

        def getRuleIndex(self):
            return PqlParser.RULE_orderExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderExpr" ):
                listener.enterOrderExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderExpr" ):
                listener.exitOrderExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderExpr" ):
                return visitor.visitOrderExpr(self)
            else:
                return visitor.visitChildren(self)




    def orderExpr(self):

        localctx = PqlParser.OrderExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_orderExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.expr(0)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.K_ASC or _la==PqlParser.K_DESC:
                self.state = 123
                _la = self._input.LA(1)
                if not(_la==PqlParser.K_ASC or _la==PqlParser.K_DESC):
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


    class LimitClauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.limit = None # ExprContext

        def K_LIMIT(self):
            return self.getToken(PqlParser.K_LIMIT, 0)

        def expr(self):
            return self.getTypedRuleContext(PqlParser.ExprContext,0)


        def getRuleIndex(self):
            return PqlParser.RULE_limitClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimitClause" ):
                listener.enterLimitClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimitClause" ):
                listener.exitLimitClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLimitClause" ):
                return visitor.visitLimitClause(self)
            else:
                return visitor.visitChildren(self)




    def limitClause(self):

        localctx = PqlParser.LimitClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_limitClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(PqlParser.K_LIMIT)
            self.state = 127
            localctx.limit = self.expr(0)
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


        def function(self):
            return self.getTypedRuleContext(PqlParser.FunctionContext,0)


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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 130
                localctx.unary_operator = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.MINUS) | (1 << PqlParser.PLUS) | (1 << PqlParser.K_NOT))) != 0)):
                    localctx.unary_operator = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 131
                localctx.right = self.expr(11)
                pass

            elif la_ == 2:
                self.state = 132
                self.match(PqlParser.OPEN_PAREN)
                self.state = 133
                localctx.inner = self.expr(0)
                self.state = 134
                self.match(PqlParser.CLOSE_PAREN)
                pass

            elif la_ == 3:
                self.state = 136
                self.literalValue()
                pass

            elif la_ == 4:
                self.state = 137
                self.function()
                pass

            elif la_ == 5:
                self.state = 138
                self.taxon()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 161
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 159
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 141
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 142
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.FORWARD_SLASH) | (1 << PqlParser.MOD) | (1 << PqlParser.STAR))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 143
                        localctx.right = self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 144
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 145
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PqlParser.MINUS or _la==PqlParser.PLUS):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 146
                        localctx.right = self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 147
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 148
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.GT_EQ) | (1 << PqlParser.LT_EQ) | (1 << PqlParser.GT) | (1 << PqlParser.LT))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 149
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 150
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 151
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.EQ) | (1 << PqlParser.NOT_EQ1) | (1 << PqlParser.NOT_EQ2) | (1 << PqlParser.ASSIGN) | (1 << PqlParser.K_IS))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 152
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 5:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 153
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 154
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PqlParser.AND or _la==PqlParser.K_AND):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 155
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 6:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 156
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 157
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PqlParser.OR or _la==PqlParser.K_OR):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 158
                        localctx.right = self.expr(6)
                        pass

             
                self.state = 163
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FunctionContext(ParserRuleContext):

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
            return PqlParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = PqlParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            localctx.function_name = self.identifierMultipart()
            self.state = 165
            self.match(PqlParser.OPEN_PAREN)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.MINUS) | (1 << PqlParser.OPEN_PAREN) | (1 << PqlParser.PLUS) | (1 << PqlParser.QUESTION_MARK) | (1 << PqlParser.K_FALSE) | (1 << PqlParser.K_NOT) | (1 << PqlParser.K_NULL) | (1 << PqlParser.K_TRUE) | (1 << PqlParser.NUMERIC_LITERAL) | (1 << PqlParser.DOUBLE_QUOTED_STRING) | (1 << PqlParser.SINGLE_QUOTED_STRING) | (1 << PqlParser.WORD))) != 0):
                self.state = 166
                localctx.arguments = self.exprList()


            self.state = 169
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
        self.enterRule(localctx, 28, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.expr(0)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PqlParser.COMMA:
                self.state = 172
                self.match(PqlParser.COMMA)
                self.state = 173
                self.expr(0)
                self.state = 178
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
        self.enterRule(localctx, 30, self.RULE_taxon)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.QUESTION_MARK:
                self.state = 179
                localctx.is_optional = self.match(PqlParser.QUESTION_MARK)


            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 182
                localctx.namespace = self.identifierMultipart()
                self.state = 183
                self.match(PqlParser.PIPE)


            self.state = 187
            localctx.slug = self.identifierMultipart()
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 188
                self.match(PqlParser.COLON)
                self.state = 189
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
        self.enterRule(localctx, 32, self.RULE_identifierMultipart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(PqlParser.WORD)
            self.state = 197
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 193
                    self.match(PqlParser.DOT)
                    self.state = 194
                    self.match(PqlParser.WORD) 
                self.state = 199
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
        self.enterRule(localctx, 34, self.RULE_literalValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
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
        self._predicates[12] = self.expr_sempred
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
         





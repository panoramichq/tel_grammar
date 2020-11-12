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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3;")
        buf.write("\u00c4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\2\3\3\7\3)\n\3\f\3\16\3,\13\3\3\3\3\3\3\4\7\4\61\n")
        buf.write("\4\f\4\16\4\64\13\4\3\4\3\4\6\48\n\4\r\4\16\49\3\4\7\4")
        buf.write("=\n\4\f\4\16\4@\13\4\3\4\7\4C\n\4\f\4\16\4F\13\4\3\5\3")
        buf.write("\5\3\6\3\6\5\6L\n\6\3\6\5\6O\n\6\3\6\5\6R\n\6\3\7\3\7")
        buf.write("\3\7\3\7\7\7X\n\7\f\7\16\7[\13\7\3\b\3\b\3\b\3\b\5\ba")
        buf.write("\n\b\3\b\3\b\5\be\n\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n")
        buf.write("\7\no\n\n\f\n\16\nr\13\n\3\13\3\13\5\13v\n\13\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u0085")
        buf.write("\n\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\7\r\u0099\n\r\f\r\16\r\u009c\13")
        buf.write("\r\3\16\3\16\3\16\5\16\u00a1\n\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\7\17\u00a8\n\17\f\17\16\17\u00ab\13\17\3\20\5\20")
        buf.write("\u00ae\n\20\3\20\3\20\3\20\5\20\u00b3\n\20\3\20\3\20\3")
        buf.write("\20\5\20\u00b8\n\20\3\21\3\21\3\21\7\21\u00bd\n\21\f\21")
        buf.write("\16\21\u00c0\13\21\3\22\3\22\3\22\2\3\30\23\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"\2\13\4\2!!##\5\2\25\25")
        buf.write("\31\31))\5\2\22\22\26\26\34\34\4\2\25\25\31\31\4\2\5\6")
        buf.write("\23\24\6\2\4\4\7\b\r\r%%\4\2\3\3\37\37\4\2\t\t,,\7\2$")
        buf.write("$++//\61\62\65\65\2\u00cf\2$\3\2\2\2\4*\3\2\2\2\6\62\3")
        buf.write("\2\2\2\bG\3\2\2\2\nI\3\2\2\2\fS\3\2\2\2\16\\\3\2\2\2\20")
        buf.write("f\3\2\2\2\22i\3\2\2\2\24s\3\2\2\2\26w\3\2\2\2\30\u0084")
        buf.write("\3\2\2\2\32\u009d\3\2\2\2\34\u00a4\3\2\2\2\36\u00ad\3")
        buf.write("\2\2\2 \u00b9\3\2\2\2\"\u00c1\3\2\2\2$%\5\30\r\2%&\7\2")
        buf.write("\2\3&\3\3\2\2\2\')\5\6\4\2(\'\3\2\2\2),\3\2\2\2*(\3\2")
        buf.write("\2\2*+\3\2\2\2+-\3\2\2\2,*\3\2\2\2-.\7\2\2\3.\5\3\2\2")
        buf.write("\2/\61\7\33\2\2\60/\3\2\2\2\61\64\3\2\2\2\62\60\3\2\2")
        buf.write("\2\62\63\3\2\2\2\63\65\3\2\2\2\64\62\3\2\2\2\65>\5\b\5")
        buf.write("\2\668\7\33\2\2\67\66\3\2\2\289\3\2\2\29\67\3\2\2\29:")
        buf.write("\3\2\2\2:;\3\2\2\2;=\5\b\5\2<\67\3\2\2\2=@\3\2\2\2><\3")
        buf.write("\2\2\2>?\3\2\2\2?D\3\2\2\2@>\3\2\2\2AC\7\33\2\2BA\3\2")
        buf.write("\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2\2\2E\7\3\2\2\2FD\3\2\2")
        buf.write("\2GH\5\n\6\2H\t\3\2\2\2IK\5\f\7\2JL\5\20\t\2KJ\3\2\2\2")
        buf.write("KL\3\2\2\2LN\3\2\2\2MO\5\22\n\2NM\3\2\2\2NO\3\2\2\2OQ")
        buf.write("\3\2\2\2PR\5\26\f\2QP\3\2\2\2QR\3\2\2\2R\13\3\2\2\2ST")
        buf.write("\7.\2\2TY\5\16\b\2UV\7\20\2\2VX\5\16\b\2WU\3\2\2\2X[\3")
        buf.write("\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\r\3\2\2\2[Y\3\2\2\2\\`\5\30")
        buf.write("\r\2]^\7\17\2\2^_\7\17\2\2_a\5\32\16\2`]\3\2\2\2`a\3\2")
        buf.write("\2\2ad\3\2\2\2bc\7 \2\2ce\5\36\20\2db\3\2\2\2de\3\2\2")
        buf.write("\2e\17\3\2\2\2fg\7\60\2\2gh\5\30\r\2h\21\3\2\2\2ij\7-")
        buf.write("\2\2jk\7\"\2\2kp\5\24\13\2lm\7\20\2\2mo\5\24\13\2nl\3")
        buf.write("\2\2\2or\3\2\2\2pn\3\2\2\2pq\3\2\2\2q\23\3\2\2\2rp\3\2")
        buf.write("\2\2su\5\30\r\2tv\t\2\2\2ut\3\2\2\2uv\3\2\2\2v\25\3\2")
        buf.write("\2\2wx\7(\2\2xy\5\30\r\2y\27\3\2\2\2z{\b\r\1\2{|\t\3\2")
        buf.write("\2|\u0085\5\30\r\r}~\7\27\2\2~\177\5\30\r\2\177\u0080")
        buf.write("\7\16\2\2\u0080\u0085\3\2\2\2\u0081\u0085\5\"\22\2\u0082")
        buf.write("\u0085\5\32\16\2\u0083\u0085\5\36\20\2\u0084z\3\2\2\2")
        buf.write("\u0084}\3\2\2\2\u0084\u0081\3\2\2\2\u0084\u0082\3\2\2")
        buf.write("\2\u0084\u0083\3\2\2\2\u0085\u009a\3\2\2\2\u0086\u0087")
        buf.write("\f\f\2\2\u0087\u0088\t\4\2\2\u0088\u0099\5\30\r\r\u0089")
        buf.write("\u008a\f\13\2\2\u008a\u008b\t\5\2\2\u008b\u0099\5\30\r")
        buf.write("\f\u008c\u008d\f\n\2\2\u008d\u008e\t\6\2\2\u008e\u0099")
        buf.write("\5\30\r\13\u008f\u0090\f\t\2\2\u0090\u0091\t\7\2\2\u0091")
        buf.write("\u0099\5\30\r\n\u0092\u0093\f\b\2\2\u0093\u0094\t\b\2")
        buf.write("\2\u0094\u0099\5\30\r\t\u0095\u0096\f\7\2\2\u0096\u0097")
        buf.write("\t\t\2\2\u0097\u0099\5\30\r\b\u0098\u0086\3\2\2\2\u0098")
        buf.write("\u0089\3\2\2\2\u0098\u008c\3\2\2\2\u0098\u008f\3\2\2\2")
        buf.write("\u0098\u0092\3\2\2\2\u0098\u0095\3\2\2\2\u0099\u009c\3")
        buf.write("\2\2\2\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\31")
        buf.write("\3\2\2\2\u009c\u009a\3\2\2\2\u009d\u009e\5 \21\2\u009e")
        buf.write("\u00a0\7\27\2\2\u009f\u00a1\5\34\17\2\u00a0\u009f\3\2")
        buf.write("\2\2\u00a0\u00a1\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3")
        buf.write("\7\16\2\2\u00a3\33\3\2\2\2\u00a4\u00a9\5\30\r\2\u00a5")
        buf.write("\u00a6\7\20\2\2\u00a6\u00a8\5\30\r\2\u00a7\u00a5\3\2\2")
        buf.write("\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa")
        buf.write("\3\2\2\2\u00aa\35\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00ae")
        buf.write("\7\32\2\2\u00ad\u00ac\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae")
        buf.write("\u00b2\3\2\2\2\u00af\u00b0\5 \21\2\u00b0\u00b1\7\30\2")
        buf.write("\2\u00b1\u00b3\3\2\2\2\u00b2\u00af\3\2\2\2\u00b2\u00b3")
        buf.write("\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b7\5 \21\2\u00b5")
        buf.write("\u00b6\7\17\2\2\u00b6\u00b8\5 \21\2\u00b7\u00b5\3\2\2")
        buf.write("\2\u00b7\u00b8\3\2\2\2\u00b8\37\3\2\2\2\u00b9\u00be\7")
        buf.write(";\2\2\u00ba\u00bb\7\21\2\2\u00bb\u00bd\7;\2\2\u00bc\u00ba")
        buf.write("\3\2\2\2\u00bd\u00c0\3\2\2\2\u00be\u00bc\3\2\2\2\u00be")
        buf.write("\u00bf\3\2\2\2\u00bf!\3\2\2\2\u00c0\u00be\3\2\2\2\u00c1")
        buf.write("\u00c2\t\n\2\2\u00c2#\3\2\2\2\30*\629>DKNQY`dpu\u0084")
        buf.write("\u0098\u009a\u00a0\u00a9\u00ad\u00b2\u00b7\u00be")
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
                      "K_SELECT", "K_TRUE", "K_WHERE", "NUMERIC_LITERAL", 
                      "DOUBLE_QUOTED_STRING", "DOUBLE_QUOTED_STRING_TEL", 
                      "DOUBLE_QUOTED_STRING_SQL", "SINGLE_QUOTED_STRING", 
                      "SINGLE_QUOTED_STRING_TEL", "SINGLE_QUOTED_STRING_SQL", 
                      "SINGLE_LINE_COMMENT", "MULTILINE_COMMENT", "SPACES", 
                      "WORD" ]

    RULE_parseTel = 0
    RULE_parsePql = 1
    RULE_sqlStmtList = 2
    RULE_sqlStmt = 3
    RULE_selectStmt = 4
    RULE_selectClause = 5
    RULE_columns = 6
    RULE_whereClause = 7
    RULE_orderByClause = 8
    RULE_orderExpr = 9
    RULE_limitClause = 10
    RULE_expr = 11
    RULE_function = 12
    RULE_exprList = 13
    RULE_taxon = 14
    RULE_identifierMultipart = 15
    RULE_literalValue = 16

    ruleNames =  [ "parseTel", "parsePql", "sqlStmtList", "sqlStmt", "selectStmt", 
                   "selectClause", "columns", "whereClause", "orderByClause", 
                   "orderExpr", "limitClause", "expr", "function", "exprList", 
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
    K_TRUE=45
    K_WHERE=46
    NUMERIC_LITERAL=47
    DOUBLE_QUOTED_STRING=48
    DOUBLE_QUOTED_STRING_TEL=49
    DOUBLE_QUOTED_STRING_SQL=50
    SINGLE_QUOTED_STRING=51
    SINGLE_QUOTED_STRING_TEL=52
    SINGLE_QUOTED_STRING_SQL=53
    SINGLE_LINE_COMMENT=54
    MULTILINE_COMMENT=55
    SPACES=56
    WORD=57

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
            self.state = 34
            self.expr(0)
            self.state = 35
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
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PqlParser.SCOL or _la==PqlParser.K_SELECT:
                self.state = 37
                self.sqlStmtList()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 43
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
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PqlParser.SCOL:
                self.state = 45
                self.match(PqlParser.SCOL)
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
            self.sqlStmt()
            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 53 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 52
                        self.match(PqlParser.SCOL)
                        self.state = 55 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==PqlParser.SCOL):
                            break

                    self.state = 57
                    self.sqlStmt() 
                self.state = 62
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 63
                    self.match(PqlParser.SCOL) 
                self.state = 68
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
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.selectStmt()
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
        self.enterRule(localctx, 8, self.RULE_selectStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.selectClause()
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.K_WHERE:
                self.state = 72
                self.whereClause()


            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.K_ORDER:
                self.state = 75
                self.orderByClause()


            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.K_LIMIT:
                self.state = 78
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
        self.enterRule(localctx, 10, self.RULE_selectClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(PqlParser.K_SELECT)
            self.state = 82
            self.columns()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PqlParser.COMMA:
                self.state = 83
                self.match(PqlParser.COMMA)
                self.state = 84
                self.columns()
                self.state = 89
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
        self.enterRule(localctx, 12, self.RULE_columns)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            localctx.value = self.expr(0)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.COLON:
                self.state = 91
                self.match(PqlParser.COLON)
                self.state = 92
                self.match(PqlParser.COLON)
                self.state = 93
                localctx.type_cast = self.function()


            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.K_AS:
                self.state = 96
                self.match(PqlParser.K_AS)
                self.state = 97
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
        self.enterRule(localctx, 14, self.RULE_whereClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(PqlParser.K_WHERE)
            self.state = 101
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
        self.enterRule(localctx, 16, self.RULE_orderByClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(PqlParser.K_ORDER)
            self.state = 104
            self.match(PqlParser.K_BY)
            self.state = 105
            self.orderExpr()
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PqlParser.COMMA:
                self.state = 106
                self.match(PqlParser.COMMA)
                self.state = 107
                self.orderExpr()
                self.state = 112
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
        self.enterRule(localctx, 18, self.RULE_orderExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.expr(0)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.K_ASC or _la==PqlParser.K_DESC:
                self.state = 114
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
        self.enterRule(localctx, 20, self.RULE_limitClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(PqlParser.K_LIMIT)
            self.state = 118
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
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 121
                localctx.unary_operator = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.MINUS) | (1 << PqlParser.PLUS) | (1 << PqlParser.K_NOT))) != 0)):
                    localctx.unary_operator = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 122
                localctx.right = self.expr(11)
                pass

            elif la_ == 2:
                self.state = 123
                self.match(PqlParser.OPEN_PAREN)
                self.state = 124
                localctx.inner = self.expr(0)
                self.state = 125
                self.match(PqlParser.CLOSE_PAREN)
                pass

            elif la_ == 3:
                self.state = 127
                self.literalValue()
                pass

            elif la_ == 4:
                self.state = 128
                self.function()
                pass

            elif la_ == 5:
                self.state = 129
                self.taxon()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 152
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 150
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 132
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 133
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.FORWARD_SLASH) | (1 << PqlParser.MOD) | (1 << PqlParser.STAR))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 134
                        localctx.right = self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 135
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 136
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PqlParser.MINUS or _la==PqlParser.PLUS):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 137
                        localctx.right = self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 138
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 139
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.GT_EQ) | (1 << PqlParser.LT_EQ) | (1 << PqlParser.GT) | (1 << PqlParser.LT))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 140
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 141
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 142
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.EQ) | (1 << PqlParser.NOT_EQ1) | (1 << PqlParser.NOT_EQ2) | (1 << PqlParser.ASSIGN) | (1 << PqlParser.K_IS))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 143
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 5:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 144
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 145
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PqlParser.AND or _la==PqlParser.K_AND):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 146
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 6:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 147
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 148
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PqlParser.OR or _la==PqlParser.K_OR):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 149
                        localctx.right = self.expr(6)
                        pass

             
                self.state = 154
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        self.enterRule(localctx, 24, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            localctx.function_name = self.identifierMultipart()
            self.state = 156
            self.match(PqlParser.OPEN_PAREN)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.MINUS) | (1 << PqlParser.OPEN_PAREN) | (1 << PqlParser.PLUS) | (1 << PqlParser.QUESTION_MARK) | (1 << PqlParser.K_FALSE) | (1 << PqlParser.K_NOT) | (1 << PqlParser.K_NULL) | (1 << PqlParser.K_TRUE) | (1 << PqlParser.NUMERIC_LITERAL) | (1 << PqlParser.DOUBLE_QUOTED_STRING) | (1 << PqlParser.SINGLE_QUOTED_STRING) | (1 << PqlParser.WORD))) != 0):
                self.state = 157
                localctx.arguments = self.exprList()


            self.state = 160
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
        self.enterRule(localctx, 26, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.expr(0)
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PqlParser.COMMA:
                self.state = 163
                self.match(PqlParser.COMMA)
                self.state = 164
                self.expr(0)
                self.state = 169
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
        self.enterRule(localctx, 28, self.RULE_taxon)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.QUESTION_MARK:
                self.state = 170
                localctx.is_optional = self.match(PqlParser.QUESTION_MARK)


            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 173
                localctx.namespace = self.identifierMultipart()
                self.state = 174
                self.match(PqlParser.PIPE)


            self.state = 178
            localctx.slug = self.identifierMultipart()
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 179
                self.match(PqlParser.COLON)
                self.state = 180
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
        self.enterRule(localctx, 30, self.RULE_identifierMultipart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(PqlParser.WORD)
            self.state = 188
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 184
                    self.match(PqlParser.DOT)
                    self.state = 185
                    self.match(PqlParser.WORD) 
                self.state = 190
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        self.enterRule(localctx, 32, self.RULE_literalValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
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
        self._predicates[11] = self.expr_sempred
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
         





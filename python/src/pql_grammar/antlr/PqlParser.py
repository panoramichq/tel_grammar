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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3=")
        buf.write("\u00e4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\3\2\3\2\3\3\7\3/\n\3\f\3\16\3")
        buf.write("\62\13\3\3\3\3\3\3\4\7\4\67\n\4\f\4\16\4:\13\4\3\4\3\4")
        buf.write("\6\4>\n\4\r\4\16\4?\3\4\7\4C\n\4\f\4\16\4F\13\4\3\4\7")
        buf.write("\4I\n\4\f\4\16\4L\13\4\3\5\3\5\5\5P\n\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\5\7Y\n\7\3\7\5\7\\\n\7\3\7\5\7_\n\7\3\7")
        buf.write("\5\7b\n\7\3\b\3\b\3\b\3\b\7\bh\n\b\f\b\16\bk\13\b\3\t")
        buf.write("\3\t\3\t\3\t\5\tq\n\t\3\t\3\t\5\tu\n\t\3\n\3\n\3\n\3\n")
        buf.write("\7\n{\n\n\f\n\16\n~\13\n\3\13\3\13\5\13\u0082\n\13\3\13")
        buf.write("\5\13\u0085\n\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\7\r\u008f")
        buf.write("\n\r\f\r\16\r\u0092\13\r\3\16\3\16\5\16\u0096\n\16\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\5\20\u00a5\n\20\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\7\20\u00b9\n\20\f\20\16\20\u00bc\13\20\3\21\3\21")
        buf.write("\3\21\5\21\u00c1\n\21\3\21\3\21\3\22\3\22\3\22\7\22\u00c8")
        buf.write("\n\22\f\22\16\22\u00cb\13\22\3\23\5\23\u00ce\n\23\3\23")
        buf.write("\3\23\3\23\5\23\u00d3\n\23\3\23\3\23\3\23\5\23\u00d8\n")
        buf.write("\23\3\24\3\24\3\24\7\24\u00dd\n\24\f\24\16\24\u00e0\13")
        buf.write("\24\3\25\3\25\3\25\2\3\36\26\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(\2\13\4\2!!##\5\2\25\25\31\31**\5\2")
        buf.write("\22\22\26\26\34\34\4\2\25\25\31\31\4\2\5\6\23\24\6\2\4")
        buf.write("\4\7\b\r\r&&\4\2\3\3\37\37\4\2\t\t--\7\2$$,,\61\61\63")
        buf.write("\64\67\67\2\u00f1\2*\3\2\2\2\4\60\3\2\2\2\68\3\2\2\2\b")
        buf.write("O\3\2\2\2\nQ\3\2\2\2\fV\3\2\2\2\16c\3\2\2\2\20l\3\2\2")
        buf.write("\2\22v\3\2\2\2\24\177\3\2\2\2\26\u0086\3\2\2\2\30\u0089")
        buf.write("\3\2\2\2\32\u0093\3\2\2\2\34\u0097\3\2\2\2\36\u00a4\3")
        buf.write("\2\2\2 \u00bd\3\2\2\2\"\u00c4\3\2\2\2$\u00cd\3\2\2\2&")
        buf.write("\u00d9\3\2\2\2(\u00e1\3\2\2\2*+\5\36\20\2+,\7\2\2\3,\3")
        buf.write("\3\2\2\2-/\5\6\4\2.-\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60")
        buf.write("\61\3\2\2\2\61\63\3\2\2\2\62\60\3\2\2\2\63\64\7\2\2\3")
        buf.write("\64\5\3\2\2\2\65\67\7\33\2\2\66\65\3\2\2\2\67:\3\2\2\2")
        buf.write("8\66\3\2\2\289\3\2\2\29;\3\2\2\2:8\3\2\2\2;D\5\b\5\2<")
        buf.write(">\7\33\2\2=<\3\2\2\2>?\3\2\2\2?=\3\2\2\2?@\3\2\2\2@A\3")
        buf.write("\2\2\2AC\5\b\5\2B=\3\2\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2\2")
        buf.write("\2EJ\3\2\2\2FD\3\2\2\2GI\7\33\2\2HG\3\2\2\2IL\3\2\2\2")
        buf.write("JH\3\2\2\2JK\3\2\2\2K\7\3\2\2\2LJ\3\2\2\2MP\5\n\6\2NP")
        buf.write("\5\f\7\2OM\3\2\2\2ON\3\2\2\2P\t\3\2\2\2QR\7\60\2\2RS\5")
        buf.write("&\24\2ST\7\r\2\2TU\5\36\20\2U\13\3\2\2\2VX\5\16\b\2WY")
        buf.write("\5\22\n\2XW\3\2\2\2XY\3\2\2\2Y[\3\2\2\2Z\\\5\26\f\2[Z")
        buf.write("\3\2\2\2[\\\3\2\2\2\\^\3\2\2\2]_\5\30\r\2^]\3\2\2\2^_")
        buf.write("\3\2\2\2_a\3\2\2\2`b\5\34\17\2a`\3\2\2\2ab\3\2\2\2b\r")
        buf.write("\3\2\2\2cd\7/\2\2di\5\20\t\2ef\7\20\2\2fh\5\20\t\2ge\3")
        buf.write("\2\2\2hk\3\2\2\2ig\3\2\2\2ij\3\2\2\2j\17\3\2\2\2ki\3\2")
        buf.write("\2\2lp\5\36\20\2mn\7\17\2\2no\7\17\2\2oq\5 \21\2pm\3\2")
        buf.write("\2\2pq\3\2\2\2qt\3\2\2\2rs\7 \2\2su\5$\23\2tr\3\2\2\2")
        buf.write("tu\3\2\2\2u\21\3\2\2\2vw\7%\2\2w|\5\24\13\2xy\7\20\2\2")
        buf.write("y{\5\24\13\2zx\3\2\2\2{~\3\2\2\2|z\3\2\2\2|}\3\2\2\2}")
        buf.write("\23\3\2\2\2~|\3\2\2\2\177\u0084\5&\24\2\u0080\u0082\7")
        buf.write(" \2\2\u0081\u0080\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0083")
        buf.write("\3\2\2\2\u0083\u0085\5&\24\2\u0084\u0081\3\2\2\2\u0084")
        buf.write("\u0085\3\2\2\2\u0085\25\3\2\2\2\u0086\u0087\7\62\2\2\u0087")
        buf.write("\u0088\5\36\20\2\u0088\27\3\2\2\2\u0089\u008a\7.\2\2\u008a")
        buf.write("\u008b\7\"\2\2\u008b\u0090\5\32\16\2\u008c\u008d\7\20")
        buf.write("\2\2\u008d\u008f\5\32\16\2\u008e\u008c\3\2\2\2\u008f\u0092")
        buf.write("\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091")
        buf.write("\31\3\2\2\2\u0092\u0090\3\2\2\2\u0093\u0095\5\36\20\2")
        buf.write("\u0094\u0096\t\2\2\2\u0095\u0094\3\2\2\2\u0095\u0096\3")
        buf.write("\2\2\2\u0096\33\3\2\2\2\u0097\u0098\7)\2\2\u0098\u0099")
        buf.write("\5\36\20\2\u0099\35\3\2\2\2\u009a\u009b\b\20\1\2\u009b")
        buf.write("\u009c\t\3\2\2\u009c\u00a5\5\36\20\r\u009d\u009e\7\27")
        buf.write("\2\2\u009e\u009f\5\36\20\2\u009f\u00a0\7\16\2\2\u00a0")
        buf.write("\u00a5\3\2\2\2\u00a1\u00a5\5(\25\2\u00a2\u00a5\5 \21\2")
        buf.write("\u00a3\u00a5\5$\23\2\u00a4\u009a\3\2\2\2\u00a4\u009d\3")
        buf.write("\2\2\2\u00a4\u00a1\3\2\2\2\u00a4\u00a2\3\2\2\2\u00a4\u00a3")
        buf.write("\3\2\2\2\u00a5\u00ba\3\2\2\2\u00a6\u00a7\f\f\2\2\u00a7")
        buf.write("\u00a8\t\4\2\2\u00a8\u00b9\5\36\20\r\u00a9\u00aa\f\13")
        buf.write("\2\2\u00aa\u00ab\t\5\2\2\u00ab\u00b9\5\36\20\f\u00ac\u00ad")
        buf.write("\f\n\2\2\u00ad\u00ae\t\6\2\2\u00ae\u00b9\5\36\20\13\u00af")
        buf.write("\u00b0\f\t\2\2\u00b0\u00b1\t\7\2\2\u00b1\u00b9\5\36\20")
        buf.write("\n\u00b2\u00b3\f\b\2\2\u00b3\u00b4\t\b\2\2\u00b4\u00b9")
        buf.write("\5\36\20\t\u00b5\u00b6\f\7\2\2\u00b6\u00b7\t\t\2\2\u00b7")
        buf.write("\u00b9\5\36\20\b\u00b8\u00a6\3\2\2\2\u00b8\u00a9\3\2\2")
        buf.write("\2\u00b8\u00ac\3\2\2\2\u00b8\u00af\3\2\2\2\u00b8\u00b2")
        buf.write("\3\2\2\2\u00b8\u00b5\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba")
        buf.write("\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\37\3\2\2\2\u00bc")
        buf.write("\u00ba\3\2\2\2\u00bd\u00be\5&\24\2\u00be\u00c0\7\27\2")
        buf.write("\2\u00bf\u00c1\5\"\22\2\u00c0\u00bf\3\2\2\2\u00c0\u00c1")
        buf.write("\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c3\7\16\2\2\u00c3")
        buf.write("!\3\2\2\2\u00c4\u00c9\5\36\20\2\u00c5\u00c6\7\20\2\2\u00c6")
        buf.write("\u00c8\5\36\20\2\u00c7\u00c5\3\2\2\2\u00c8\u00cb\3\2\2")
        buf.write("\2\u00c9\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca#\3\2")
        buf.write("\2\2\u00cb\u00c9\3\2\2\2\u00cc\u00ce\7\32\2\2\u00cd\u00cc")
        buf.write("\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00d2\3\2\2\2\u00cf")
        buf.write("\u00d0\5&\24\2\u00d0\u00d1\7\30\2\2\u00d1\u00d3\3\2\2")
        buf.write("\2\u00d2\u00cf\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4")
        buf.write("\3\2\2\2\u00d4\u00d7\5&\24\2\u00d5\u00d6\7\17\2\2\u00d6")
        buf.write("\u00d8\5&\24\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2")
        buf.write("\u00d8%\3\2\2\2\u00d9\u00de\7=\2\2\u00da\u00db\7\21\2")
        buf.write("\2\u00db\u00dd\7=\2\2\u00dc\u00da\3\2\2\2\u00dd\u00e0")
        buf.write("\3\2\2\2\u00de\u00dc\3\2\2\2\u00de\u00df\3\2\2\2\u00df")
        buf.write("\'\3\2\2\2\u00e0\u00de\3\2\2\2\u00e1\u00e2\t\n\2\2\u00e2")
        buf.write(")\3\2\2\2\35\608?DJOX[^aipt|\u0081\u0084\u0090\u0095\u00a4")
        buf.write("\u00b8\u00ba\u00c0\u00c9\u00cd\u00d2\u00d7\u00de")
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
                      "K_FALSE", "K_FROM", "K_IS", "K_ISNULL", "K_LIKE", 
                      "K_LIMIT", "K_NOT", "K_NOTNULL", "K_NULL", "K_OR", 
                      "K_ORDER", "K_SELECT", "K_SET", "K_TRUE", "K_WHERE", 
                      "NUMERIC_LITERAL", "DOUBLE_QUOTED_STRING", "DOUBLE_QUOTED_STRING_TEL", 
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
    RULE_fromClause = 8
    RULE_tables = 9
    RULE_whereClause = 10
    RULE_orderByClause = 11
    RULE_orderExpr = 12
    RULE_limitClause = 13
    RULE_expr = 14
    RULE_function = 15
    RULE_exprList = 16
    RULE_taxon = 17
    RULE_identifierMultipart = 18
    RULE_literalValue = 19

    ruleNames =  [ "parseTel", "parsePql", "sqlStmtList", "sqlStmt", "setStmt", 
                   "selectStmt", "selectClause", "columns", "fromClause", 
                   "tables", "whereClause", "orderByClause", "orderExpr", 
                   "limitClause", "expr", "function", "exprList", "taxon", 
                   "identifierMultipart", "literalValue" ]

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
    K_FROM=35
    K_IS=36
    K_ISNULL=37
    K_LIKE=38
    K_LIMIT=39
    K_NOT=40
    K_NOTNULL=41
    K_NULL=42
    K_OR=43
    K_ORDER=44
    K_SELECT=45
    K_SET=46
    K_TRUE=47
    K_WHERE=48
    NUMERIC_LITERAL=49
    DOUBLE_QUOTED_STRING=50
    DOUBLE_QUOTED_STRING_TEL=51
    DOUBLE_QUOTED_STRING_SQL=52
    SINGLE_QUOTED_STRING=53
    SINGLE_QUOTED_STRING_TEL=54
    SINGLE_QUOTED_STRING_SQL=55
    SINGLE_LINE_COMMENT=56
    MULTILINE_COMMENT=57
    SPACES=58
    WORD=59

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
            self.state = 40
            self.expr(0)
            self.state = 41
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
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.SCOL) | (1 << PqlParser.K_SELECT) | (1 << PqlParser.K_SET))) != 0):
                self.state = 43
                self.sqlStmtList()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 49
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
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PqlParser.SCOL:
                self.state = 51
                self.match(PqlParser.SCOL)
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 57
            self.sqlStmt()
            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 59 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 58
                        self.match(PqlParser.SCOL)
                        self.state = 61 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==PqlParser.SCOL):
                            break

                    self.state = 63
                    self.sqlStmt() 
                self.state = 68
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 72
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 69
                    self.match(PqlParser.SCOL) 
                self.state = 74
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
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PqlParser.K_SET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.setStmt()
                pass
            elif token in [PqlParser.K_SELECT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
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
            self.value = None # ExprContext

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
            self.state = 79
            self.match(PqlParser.K_SET)
            self.state = 80
            localctx.key = self.identifierMultipart()
            self.state = 81
            self.match(PqlParser.ASSIGN)
            self.state = 82
            localctx.value = self.expr(0)
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


        def fromClause(self):
            return self.getTypedRuleContext(PqlParser.FromClauseContext,0)


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
            self.state = 84
            self.selectClause()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.K_FROM:
                self.state = 85
                self.fromClause()


            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.K_WHERE:
                self.state = 88
                self.whereClause()


            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.K_ORDER:
                self.state = 91
                self.orderByClause()


            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.K_LIMIT:
                self.state = 94
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
            self.state = 97
            self.match(PqlParser.K_SELECT)
            self.state = 98
            self.columns()
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PqlParser.COMMA:
                self.state = 99
                self.match(PqlParser.COMMA)
                self.state = 100
                self.columns()
                self.state = 105
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
            self.state = 106
            localctx.value = self.expr(0)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.COLON:
                self.state = 107
                self.match(PqlParser.COLON)
                self.state = 108
                self.match(PqlParser.COLON)
                self.state = 109
                localctx.type_cast = self.function()


            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.K_AS:
                self.state = 112
                self.match(PqlParser.K_AS)
                self.state = 113
                localctx.alias = self.taxon()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FromClauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_FROM(self):
            return self.getToken(PqlParser.K_FROM, 0)

        def tables(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PqlParser.TablesContext)
            else:
                return self.getTypedRuleContext(PqlParser.TablesContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PqlParser.COMMA)
            else:
                return self.getToken(PqlParser.COMMA, i)

        def getRuleIndex(self):
            return PqlParser.RULE_fromClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFromClause" ):
                listener.enterFromClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFromClause" ):
                listener.exitFromClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFromClause" ):
                return visitor.visitFromClause(self)
            else:
                return visitor.visitChildren(self)




    def fromClause(self):

        localctx = PqlParser.FromClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_fromClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(PqlParser.K_FROM)
            self.state = 117
            self.tables()
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PqlParser.COMMA:
                self.state = 118
                self.match(PqlParser.COMMA)
                self.state = 119
                self.tables()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TablesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.table_name = None # IdentifierMultipartContext
            self.table_alias = None # IdentifierMultipartContext

        def identifierMultipart(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PqlParser.IdentifierMultipartContext)
            else:
                return self.getTypedRuleContext(PqlParser.IdentifierMultipartContext,i)


        def K_AS(self):
            return self.getToken(PqlParser.K_AS, 0)

        def getRuleIndex(self):
            return PqlParser.RULE_tables

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTables" ):
                listener.enterTables(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTables" ):
                listener.exitTables(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTables" ):
                return visitor.visitTables(self)
            else:
                return visitor.visitChildren(self)




    def tables(self):

        localctx = PqlParser.TablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_tables)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            localctx.table_name = self.identifierMultipart()
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.K_AS or _la==PqlParser.WORD:
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PqlParser.K_AS:
                    self.state = 126
                    self.match(PqlParser.K_AS)


                self.state = 129
                localctx.table_alias = self.identifierMultipart()


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
        self.enterRule(localctx, 20, self.RULE_whereClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(PqlParser.K_WHERE)
            self.state = 133
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
        self.enterRule(localctx, 22, self.RULE_orderByClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(PqlParser.K_ORDER)
            self.state = 136
            self.match(PqlParser.K_BY)
            self.state = 137
            self.orderExpr()
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PqlParser.COMMA:
                self.state = 138
                self.match(PqlParser.COMMA)
                self.state = 139
                self.orderExpr()
                self.state = 144
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
        self.enterRule(localctx, 24, self.RULE_orderExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.expr(0)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.K_ASC or _la==PqlParser.K_DESC:
                self.state = 146
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
        self.enterRule(localctx, 26, self.RULE_limitClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(PqlParser.K_LIMIT)
            self.state = 150
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
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 153
                localctx.unary_operator = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.MINUS) | (1 << PqlParser.PLUS) | (1 << PqlParser.K_NOT))) != 0)):
                    localctx.unary_operator = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 154
                localctx.right = self.expr(11)
                pass

            elif la_ == 2:
                self.state = 155
                self.match(PqlParser.OPEN_PAREN)
                self.state = 156
                localctx.inner = self.expr(0)
                self.state = 157
                self.match(PqlParser.CLOSE_PAREN)
                pass

            elif la_ == 3:
                self.state = 159
                self.literalValue()
                pass

            elif la_ == 4:
                self.state = 160
                self.function()
                pass

            elif la_ == 5:
                self.state = 161
                self.taxon()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 184
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 182
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 164
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 165
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.FORWARD_SLASH) | (1 << PqlParser.MOD) | (1 << PqlParser.STAR))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 166
                        localctx.right = self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 167
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 168
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PqlParser.MINUS or _la==PqlParser.PLUS):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 169
                        localctx.right = self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 170
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 171
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.GT_EQ) | (1 << PqlParser.LT_EQ) | (1 << PqlParser.GT) | (1 << PqlParser.LT))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 172
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 173
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 174
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.EQ) | (1 << PqlParser.NOT_EQ1) | (1 << PqlParser.NOT_EQ2) | (1 << PqlParser.ASSIGN) | (1 << PqlParser.K_IS))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 175
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 5:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 176
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 177
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PqlParser.AND or _la==PqlParser.K_AND):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 178
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 6:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 179
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 180
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PqlParser.OR or _la==PqlParser.K_OR):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 181
                        localctx.right = self.expr(6)
                        pass

             
                self.state = 186
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
        self.enterRule(localctx, 30, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            localctx.function_name = self.identifierMultipart()
            self.state = 188
            self.match(PqlParser.OPEN_PAREN)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.MINUS) | (1 << PqlParser.OPEN_PAREN) | (1 << PqlParser.PLUS) | (1 << PqlParser.QUESTION_MARK) | (1 << PqlParser.K_FALSE) | (1 << PqlParser.K_NOT) | (1 << PqlParser.K_NULL) | (1 << PqlParser.K_TRUE) | (1 << PqlParser.NUMERIC_LITERAL) | (1 << PqlParser.DOUBLE_QUOTED_STRING) | (1 << PqlParser.SINGLE_QUOTED_STRING) | (1 << PqlParser.WORD))) != 0):
                self.state = 189
                localctx.arguments = self.exprList()


            self.state = 192
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
        self.enterRule(localctx, 32, self.RULE_exprList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.expr(0)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PqlParser.COMMA:
                self.state = 195
                self.match(PqlParser.COMMA)
                self.state = 196
                self.expr(0)
                self.state = 201
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
        self.enterRule(localctx, 34, self.RULE_taxon)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.QUESTION_MARK:
                self.state = 202
                localctx.is_optional = self.match(PqlParser.QUESTION_MARK)


            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 205
                localctx.namespace = self.identifierMultipart()
                self.state = 206
                self.match(PqlParser.PIPE)


            self.state = 210
            localctx.slug = self.identifierMultipart()
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 211
                self.match(PqlParser.COLON)
                self.state = 212
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
        self.enterRule(localctx, 36, self.RULE_identifierMultipart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(PqlParser.WORD)
            self.state = 220
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 216
                    self.match(PqlParser.DOT)
                    self.state = 217
                    self.match(PqlParser.WORD) 
                self.state = 222
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        self.enterRule(localctx, 38, self.RULE_literalValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
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
        self._predicates[14] = self.expr_sempred
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
         





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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3:")
        buf.write("\u00b2\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\2\3\3\7\3#\n\3\f\3\16\3&\13")
        buf.write("\3\3\3\3\3\3\4\7\4+\n\4\f\4\16\4.\13\4\3\4\3\4\6\4\62")
        buf.write("\n\4\r\4\16\4\63\3\4\7\4\67\n\4\f\4\16\4:\13\4\3\4\7\4")
        buf.write("=\n\4\f\4\16\4@\13\4\3\5\3\5\3\6\3\6\3\6\5\6G\n\6\3\6")
        buf.write("\5\6J\n\6\3\6\5\6M\n\6\3\7\3\7\3\7\7\7R\n\7\f\7\16\7U")
        buf.write("\13\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\7\t_\n\t\f\t\16")
        buf.write("\tb\13\t\3\n\3\n\5\nf\n\n\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\7\fx\n\f\f\f\16")
        buf.write("\f{\13\f\5\f}\n\f\3\f\3\f\3\f\5\f\u0082\n\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\7\f\u0096\n\f\f\f\16\f\u0099\13\f\3\r\5\r\u009c")
        buf.write("\n\r\3\r\3\r\3\r\5\r\u00a1\n\r\3\r\3\r\3\r\5\r\u00a6\n")
        buf.write("\r\3\16\3\16\3\16\7\16\u00ab\n\16\f\16\16\16\u00ae\13")
        buf.write("\16\3\17\3\17\3\17\2\3\26\20\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\2\13\4\2  \"\"\5\2\26\26\32\32((\5\2\23\23\27")
        buf.write("\27\34\34\4\2\26\26\32\32\4\2\7\b\24\25\6\2\6\6\t\n\17")
        buf.write("\17$$\4\2\5\5\37\37\4\2\13\13++\7\2##**..\60\61\64\64")
        buf.write("\2\u00be\2\36\3\2\2\2\4$\3\2\2\2\6,\3\2\2\2\bA\3\2\2\2")
        buf.write("\nC\3\2\2\2\fN\3\2\2\2\16V\3\2\2\2\20Y\3\2\2\2\22c\3\2")
        buf.write("\2\2\24g\3\2\2\2\26\u0081\3\2\2\2\30\u009b\3\2\2\2\32")
        buf.write("\u00a7\3\2\2\2\34\u00af\3\2\2\2\36\37\5\26\f\2\37 \7\2")
        buf.write("\2\3 \3\3\2\2\2!#\5\6\4\2\"!\3\2\2\2#&\3\2\2\2$\"\3\2")
        buf.write("\2\2$%\3\2\2\2%\'\3\2\2\2&$\3\2\2\2\'(\7\2\2\3(\5\3\2")
        buf.write("\2\2)+\7\33\2\2*)\3\2\2\2+.\3\2\2\2,*\3\2\2\2,-\3\2\2")
        buf.write("\2-/\3\2\2\2.,\3\2\2\2/8\5\b\5\2\60\62\7\33\2\2\61\60")
        buf.write("\3\2\2\2\62\63\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2\2\64")
        buf.write("\65\3\2\2\2\65\67\5\b\5\2\66\61\3\2\2\2\67:\3\2\2\28\66")
        buf.write("\3\2\2\289\3\2\2\29>\3\2\2\2:8\3\2\2\2;=\7\33\2\2<;\3")
        buf.write("\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?\7\3\2\2\2@>\3\2")
        buf.write("\2\2AB\5\n\6\2B\t\3\2\2\2CD\7-\2\2DF\5\f\7\2EG\5\16\b")
        buf.write("\2FE\3\2\2\2FG\3\2\2\2GI\3\2\2\2HJ\5\20\t\2IH\3\2\2\2")
        buf.write("IJ\3\2\2\2JL\3\2\2\2KM\5\24\13\2LK\3\2\2\2LM\3\2\2\2M")
        buf.write("\13\3\2\2\2NS\5\26\f\2OP\7\21\2\2PR\5\26\f\2QO\3\2\2\2")
        buf.write("RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2T\r\3\2\2\2US\3\2\2\2VW")
        buf.write("\7/\2\2WX\5\26\f\2X\17\3\2\2\2YZ\7,\2\2Z[\7!\2\2[`\5\22")
        buf.write("\n\2\\]\7\21\2\2]_\5\22\n\2^\\\3\2\2\2_b\3\2\2\2`^\3\2")
        buf.write("\2\2`a\3\2\2\2a\21\3\2\2\2b`\3\2\2\2ce\5\26\f\2df\t\2")
        buf.write("\2\2ed\3\2\2\2ef\3\2\2\2f\23\3\2\2\2gh\7\'\2\2hi\5\26")
        buf.write("\f\2i\25\3\2\2\2jk\b\f\1\2kl\t\3\2\2l\u0082\5\26\f\rm")
        buf.write("n\7\30\2\2no\5\26\f\2op\7\20\2\2p\u0082\3\2\2\2q\u0082")
        buf.write("\5\34\17\2rs\5\32\16\2s|\7\30\2\2ty\5\26\f\2uv\7\21\2")
        buf.write("\2vx\5\26\f\2wu\3\2\2\2x{\3\2\2\2yw\3\2\2\2yz\3\2\2\2")
        buf.write("z}\3\2\2\2{y\3\2\2\2|t\3\2\2\2|}\3\2\2\2}~\3\2\2\2~\177")
        buf.write("\7\20\2\2\177\u0082\3\2\2\2\u0080\u0082\5\30\r\2\u0081")
        buf.write("j\3\2\2\2\u0081m\3\2\2\2\u0081q\3\2\2\2\u0081r\3\2\2\2")
        buf.write("\u0081\u0080\3\2\2\2\u0082\u0097\3\2\2\2\u0083\u0084\f")
        buf.write("\f\2\2\u0084\u0085\t\4\2\2\u0085\u0096\5\26\f\r\u0086")
        buf.write("\u0087\f\13\2\2\u0087\u0088\t\5\2\2\u0088\u0096\5\26\f")
        buf.write("\f\u0089\u008a\f\n\2\2\u008a\u008b\t\6\2\2\u008b\u0096")
        buf.write("\5\26\f\13\u008c\u008d\f\t\2\2\u008d\u008e\t\7\2\2\u008e")
        buf.write("\u0096\5\26\f\n\u008f\u0090\f\b\2\2\u0090\u0091\t\b\2")
        buf.write("\2\u0091\u0096\5\26\f\t\u0092\u0093\f\7\2\2\u0093\u0094")
        buf.write("\t\t\2\2\u0094\u0096\5\26\f\b\u0095\u0083\3\2\2\2\u0095")
        buf.write("\u0086\3\2\2\2\u0095\u0089\3\2\2\2\u0095\u008c\3\2\2\2")
        buf.write("\u0095\u008f\3\2\2\2\u0095\u0092\3\2\2\2\u0096\u0099\3")
        buf.write("\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\27")
        buf.write("\3\2\2\2\u0099\u0097\3\2\2\2\u009a\u009c\7\4\2\2\u009b")
        buf.write("\u009a\3\2\2\2\u009b\u009c\3\2\2\2\u009c\u00a0\3\2\2\2")
        buf.write("\u009d\u009e\5\32\16\2\u009e\u009f\7\31\2\2\u009f\u00a1")
        buf.write("\3\2\2\2\u00a0\u009d\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1")
        buf.write("\u00a2\3\2\2\2\u00a2\u00a5\5\32\16\2\u00a3\u00a4\7\3\2")
        buf.write("\2\u00a4\u00a6\5\32\16\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6")
        buf.write("\3\2\2\2\u00a6\31\3\2\2\2\u00a7\u00ac\7:\2\2\u00a8\u00a9")
        buf.write("\7\22\2\2\u00a9\u00ab\7:\2\2\u00aa\u00a8\3\2\2\2\u00ab")
        buf.write("\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2")
        buf.write("\u00ad\33\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b0\t\n")
        buf.write("\2\2\u00b0\35\3\2\2\2\26$,\638>FILS`ey|\u0081\u0095\u0097")
        buf.write("\u009b\u00a0\u00a5\u00ac")
        return buf.getvalue()


class PqlParser ( Parser ):

    grammarFileName = "PqlParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'?'", "'&&'", "'=='", "'>='", 
                     "'<='", "'!='", "'<>'", "'||'", "'<<'", "'>>'", "'&'", 
                     "'='", "')'", "','", "'.'", "'/'", "'>'", "'<'", "'-'", 
                     "'%'", "'('", "'|'", "'+'", "';'", "'*'", "'~'", "'_'" ]

    symbolicNames = [ "<INVALID>", "TAXON_TAG_DELIMITER", "TAXON_OPTIONAL_OPERATOR", 
                      "AND", "EQ", "GT_EQ", "LT_EQ", "NOT_EQ1", "NOT_EQ2", 
                      "OR", "SHIFT_LEFT", "SHIFT_RIGHT", "AMP", "ASSIGN", 
                      "CLOSE_PAREN", "COMMA", "DOT", "FORWARD_SLASH", "GT", 
                      "LT", "MINUS", "MOD", "OPEN_PAREN", "PIPE", "PLUS", 
                      "SCOL", "STAR", "TILDE", "UNDER", "K_AND", "K_ASC", 
                      "K_BY", "K_DESC", "K_FALSE", "K_IS", "K_ISNULL", "K_LIKE", 
                      "K_LIMIT", "K_NOT", "K_NOTNULL", "K_NULL", "K_OR", 
                      "K_ORDER", "K_SELECT", "K_TRUE", "K_WHERE", "NUMERIC_LITERAL", 
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
    RULE_columns = 5
    RULE_whereClause = 6
    RULE_orderByClause = 7
    RULE_orderExpr = 8
    RULE_limitClause = 9
    RULE_expr = 10
    RULE_taxon = 11
    RULE_identifierMultipart = 12
    RULE_literalValue = 13

    ruleNames =  [ "parseTel", "parsePql", "sqlStmtList", "sqlStmt", "selectStmt", 
                   "columns", "whereClause", "orderByClause", "orderExpr", 
                   "limitClause", "expr", "taxon", "identifierMultipart", 
                   "literalValue" ]

    EOF = Token.EOF
    TAXON_TAG_DELIMITER=1
    TAXON_OPTIONAL_OPERATOR=2
    AND=3
    EQ=4
    GT_EQ=5
    LT_EQ=6
    NOT_EQ1=7
    NOT_EQ2=8
    OR=9
    SHIFT_LEFT=10
    SHIFT_RIGHT=11
    AMP=12
    ASSIGN=13
    CLOSE_PAREN=14
    COMMA=15
    DOT=16
    FORWARD_SLASH=17
    GT=18
    LT=19
    MINUS=20
    MOD=21
    OPEN_PAREN=22
    PIPE=23
    PLUS=24
    SCOL=25
    STAR=26
    TILDE=27
    UNDER=28
    K_AND=29
    K_ASC=30
    K_BY=31
    K_DESC=32
    K_FALSE=33
    K_IS=34
    K_ISNULL=35
    K_LIKE=36
    K_LIMIT=37
    K_NOT=38
    K_NOTNULL=39
    K_NULL=40
    K_OR=41
    K_ORDER=42
    K_SELECT=43
    K_TRUE=44
    K_WHERE=45
    NUMERIC_LITERAL=46
    DOUBLE_QUOTED_STRING=47
    DOUBLE_QUOTED_STRING_TEL=48
    DOUBLE_QUOTED_STRING_SQL=49
    SINGLE_QUOTED_STRING=50
    SINGLE_QUOTED_STRING_TEL=51
    SINGLE_QUOTED_STRING_SQL=52
    SINGLE_LINE_COMMENT=53
    MULTILINE_COMMENT=54
    SPACES=55
    WORD=56

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
            self.state = 28
            self.expr(0)
            self.state = 29
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
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PqlParser.SCOL or _la==PqlParser.K_SELECT:
                self.state = 31
                self.sqlStmtList()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
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
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PqlParser.SCOL:
                self.state = 39
                self.match(PqlParser.SCOL)
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self.sqlStmt()
            self.state = 54
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 47 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 46
                        self.match(PqlParser.SCOL)
                        self.state = 49 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==PqlParser.SCOL):
                            break

                    self.state = 51
                    self.sqlStmt() 
                self.state = 56
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 57
                    self.match(PqlParser.SCOL) 
                self.state = 62
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
            self.state = 63
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

        def K_SELECT(self):
            return self.getToken(PqlParser.K_SELECT, 0)

        def columns(self):
            return self.getTypedRuleContext(PqlParser.ColumnsContext,0)


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
            self.state = 65
            self.match(PqlParser.K_SELECT)
            self.state = 66
            self.columns()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.K_WHERE:
                self.state = 67
                self.whereClause()


            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.K_ORDER:
                self.state = 70
                self.orderByClause()


            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.K_LIMIT:
                self.state = 73
                self.limitClause()


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
        self.enterRule(localctx, 10, self.RULE_columns)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.expr(0)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PqlParser.COMMA:
                self.state = 77
                self.match(PqlParser.COMMA)
                self.state = 78
                self.expr(0)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 12, self.RULE_whereClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(PqlParser.K_WHERE)
            self.state = 85
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
        self.enterRule(localctx, 14, self.RULE_orderByClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(PqlParser.K_ORDER)
            self.state = 88
            self.match(PqlParser.K_BY)
            self.state = 89
            self.orderExpr()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PqlParser.COMMA:
                self.state = 90
                self.match(PqlParser.COMMA)
                self.state = 91
                self.orderExpr()
                self.state = 96
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
        self.enterRule(localctx, 16, self.RULE_orderExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.expr(0)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.K_ASC or _la==PqlParser.K_DESC:
                self.state = 98
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
        self.enterRule(localctx, 18, self.RULE_limitClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(PqlParser.K_LIMIT)
            self.state = 102
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
            self.function_name = None # IdentifierMultipartContext
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


        def identifierMultipart(self):
            return self.getTypedRuleContext(PqlParser.IdentifierMultipartContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PqlParser.COMMA)
            else:
                return self.getToken(PqlParser.COMMA, i)

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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 105
                localctx.unary_operator = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.MINUS) | (1 << PqlParser.PLUS) | (1 << PqlParser.K_NOT))) != 0)):
                    localctx.unary_operator = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 106
                localctx.right = self.expr(11)
                pass

            elif la_ == 2:
                self.state = 107
                self.match(PqlParser.OPEN_PAREN)
                self.state = 108
                localctx.inner = self.expr(0)
                self.state = 109
                self.match(PqlParser.CLOSE_PAREN)
                pass

            elif la_ == 3:
                self.state = 111
                self.literalValue()
                pass

            elif la_ == 4:
                self.state = 112
                localctx.function_name = self.identifierMultipart()
                self.state = 113
                self.match(PqlParser.OPEN_PAREN)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.TAXON_OPTIONAL_OPERATOR) | (1 << PqlParser.MINUS) | (1 << PqlParser.OPEN_PAREN) | (1 << PqlParser.PLUS) | (1 << PqlParser.K_FALSE) | (1 << PqlParser.K_NOT) | (1 << PqlParser.K_NULL) | (1 << PqlParser.K_TRUE) | (1 << PqlParser.NUMERIC_LITERAL) | (1 << PqlParser.DOUBLE_QUOTED_STRING) | (1 << PqlParser.SINGLE_QUOTED_STRING) | (1 << PqlParser.WORD))) != 0):
                    self.state = 114
                    self.expr(0)
                    self.state = 119
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==PqlParser.COMMA:
                        self.state = 115
                        self.match(PqlParser.COMMA)
                        self.state = 116
                        self.expr(0)
                        self.state = 121
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 124
                self.match(PqlParser.CLOSE_PAREN)
                pass

            elif la_ == 5:
                self.state = 126
                self.taxon()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 149
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 147
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 129
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 130
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.FORWARD_SLASH) | (1 << PqlParser.MOD) | (1 << PqlParser.STAR))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 131
                        localctx.right = self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 132
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 133
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PqlParser.MINUS or _la==PqlParser.PLUS):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 134
                        localctx.right = self.expr(10)
                        pass

                    elif la_ == 3:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 135
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 136
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.GT_EQ) | (1 << PqlParser.LT_EQ) | (1 << PqlParser.GT) | (1 << PqlParser.LT))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 137
                        localctx.right = self.expr(9)
                        pass

                    elif la_ == 4:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 138
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 139
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PqlParser.EQ) | (1 << PqlParser.NOT_EQ1) | (1 << PqlParser.NOT_EQ2) | (1 << PqlParser.ASSIGN) | (1 << PqlParser.K_IS))) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 140
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 5:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 141
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 142
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PqlParser.AND or _la==PqlParser.K_AND):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 143
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 6:
                        localctx = PqlParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 144
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 145
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==PqlParser.OR or _la==PqlParser.K_OR):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 146
                        localctx.right = self.expr(6)
                        pass

             
                self.state = 151
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TaxonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.namespace = None # IdentifierMultipartContext
            self.slug = None # IdentifierMultipartContext
            self.tag = None # IdentifierMultipartContext

        def identifierMultipart(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PqlParser.IdentifierMultipartContext)
            else:
                return self.getTypedRuleContext(PqlParser.IdentifierMultipartContext,i)


        def TAXON_OPTIONAL_OPERATOR(self):
            return self.getToken(PqlParser.TAXON_OPTIONAL_OPERATOR, 0)

        def PIPE(self):
            return self.getToken(PqlParser.PIPE, 0)

        def TAXON_TAG_DELIMITER(self):
            return self.getToken(PqlParser.TAXON_TAG_DELIMITER, 0)

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
        self.enterRule(localctx, 22, self.RULE_taxon)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PqlParser.TAXON_OPTIONAL_OPERATOR:
                self.state = 152
                self.match(PqlParser.TAXON_OPTIONAL_OPERATOR)


            self.state = 158
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 155
                localctx.namespace = self.identifierMultipart()
                self.state = 156
                self.match(PqlParser.PIPE)


            self.state = 160
            localctx.slug = self.identifierMultipart()
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 161
                self.match(PqlParser.TAXON_TAG_DELIMITER)
                self.state = 162
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
        self.enterRule(localctx, 24, self.RULE_identifierMultipart)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(PqlParser.WORD)
            self.state = 170
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 166
                    self.match(PqlParser.DOT)
                    self.state = 167
                    self.match(PqlParser.WORD) 
                self.state = 172
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        self.enterRule(localctx, 26, self.RULE_literalValue)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
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
        self._predicates[10] = self.expr_sempred
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
         





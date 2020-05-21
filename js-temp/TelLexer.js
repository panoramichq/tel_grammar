// Generated from grammar/Tel.g4 by ANTLR 4.8
// jshint ignore: start
var antlr4 = require('antlr4/index');



var serializedATN = ["\u0003\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964",
    "\u0002\u001c\u009d\b\u0001\u0004\u0002\t\u0002\u0004\u0003\t\u0003\u0004",
    "\u0004\t\u0004\u0004\u0005\t\u0005\u0004\u0006\t\u0006\u0004\u0007\t",
    "\u0007\u0004\b\t\b\u0004\t\t\t\u0004\n\t\n\u0004\u000b\t\u000b\u0004",
    "\f\t\f\u0004\r\t\r\u0004\u000e\t\u000e\u0004\u000f\t\u000f\u0004\u0010",
    "\t\u0010\u0004\u0011\t\u0011\u0004\u0012\t\u0012\u0004\u0013\t\u0013",
    "\u0004\u0014\t\u0014\u0004\u0015\t\u0015\u0004\u0016\t\u0016\u0004\u0017",
    "\t\u0017\u0004\u0018\t\u0018\u0004\u0019\t\u0019\u0004\u001a\t\u001a",
    "\u0004\u001b\t\u001b\u0003\u0002\u0005\u00029\n\u0002\u0003\u0002\u0006",
    "\u0002<\n\u0002\r\u0002\u000e\u0002=\u0003\u0003\u0005\u0003A\n\u0003",
    "\u0003\u0003\u0006\u0003D\n\u0003\r\u0003\u000e\u0003E\u0003\u0003\u0003",
    "\u0003\u0006\u0003J\n\u0003\r\u0003\u000e\u0003K\u0003\u0004\u0003\u0004",
    "\u0003\u0004\u0003\u0004\u0003\u0004\u0003\u0005\u0003\u0005\u0003\u0005",
    "\u0003\u0005\u0003\u0005\u0003\u0005\u0003\u0006\u0003\u0006\u0003\u0006",
    "\u0003\u0006\u0003\u0007\u0006\u0007^\n\u0007\r\u0007\u000e\u0007_\u0003",
    "\b\u0003\b\u0003\b\u0003\b\u0007\bf\n\b\f\b\u000e\bi\u000b\b\u0003\b",
    "\u0003\b\u0003\t\u0003\t\u0003\n\u0003\n\u0003\u000b\u0003\u000b\u0003",
    "\f\u0003\f\u0003\r\u0003\r\u0003\u000e\u0003\u000e\u0003\u000e\u0003",
    "\u000f\u0003\u000f\u0003\u000f\u0003\u0010\u0003\u0010\u0003\u0010\u0003",
    "\u0011\u0003\u0011\u0003\u0011\u0003\u0012\u0003\u0012\u0003\u0013\u0003",
    "\u0013\u0003\u0014\u0003\u0014\u0003\u0014\u0003\u0015\u0003\u0015\u0003",
    "\u0015\u0003\u0016\u0003\u0016\u0003\u0017\u0003\u0017\u0003\u0018\u0003",
    "\u0018\u0003\u0019\u0003\u0019\u0003\u001a\u0003\u001a\u0003\u001b\u0006",
    "\u001b\u0098\n\u001b\r\u001b\u000e\u001b\u0099\u0003\u001b\u0003\u001b",
    "\u0002\u0002\u001c\u0003\u0003\u0005\u0004\u0007\u0005\t\u0006\u000b",
    "\u0007\r\b\u000f\t\u0011\n\u0013\u000b\u0015\f\u0017\r\u0019\u000e\u001b",
    "\u000f\u001d\u0010\u001f\u0011!\u0012#\u0013%\u0014\'\u0015)\u0016+",
    "\u0017-\u0018/\u00191\u001a3\u001b5\u001c\u0003\u0002\u0006\u0003\u0002",
    "2;\u0006\u00022;C\\aac|\u0003\u0002$$\u0005\u0002\u000b\f\u000f\u000f",
    "\"\"\u0002\u00a5\u0002\u0003\u0003\u0002\u0002\u0002\u0002\u0005\u0003",
    "\u0002\u0002\u0002\u0002\u0007\u0003\u0002\u0002\u0002\u0002\t\u0003",
    "\u0002\u0002\u0002\u0002\u000b\u0003\u0002\u0002\u0002\u0002\r\u0003",
    "\u0002\u0002\u0002\u0002\u000f\u0003\u0002\u0002\u0002\u0002\u0011\u0003",
    "\u0002\u0002\u0002\u0002\u0013\u0003\u0002\u0002\u0002\u0002\u0015\u0003",
    "\u0002\u0002\u0002\u0002\u0017\u0003\u0002\u0002\u0002\u0002\u0019\u0003",
    "\u0002\u0002\u0002\u0002\u001b\u0003\u0002\u0002\u0002\u0002\u001d\u0003",
    "\u0002\u0002\u0002\u0002\u001f\u0003\u0002\u0002\u0002\u0002!\u0003",
    "\u0002\u0002\u0002\u0002#\u0003\u0002\u0002\u0002\u0002%\u0003\u0002",
    "\u0002\u0002\u0002\'\u0003\u0002\u0002\u0002\u0002)\u0003\u0002\u0002",
    "\u0002\u0002+\u0003\u0002\u0002\u0002\u0002-\u0003\u0002\u0002\u0002",
    "\u0002/\u0003\u0002\u0002\u0002\u00021\u0003\u0002\u0002\u0002\u0002",
    "3\u0003\u0002\u0002\u0002\u00025\u0003\u0002\u0002\u0002\u00038\u0003",
    "\u0002\u0002\u0002\u0005@\u0003\u0002\u0002\u0002\u0007M\u0003\u0002",
    "\u0002\u0002\tR\u0003\u0002\u0002\u0002\u000bX\u0003\u0002\u0002\u0002",
    "\r]\u0003\u0002\u0002\u0002\u000fa\u0003\u0002\u0002\u0002\u0011l\u0003",
    "\u0002\u0002\u0002\u0013n\u0003\u0002\u0002\u0002\u0015p\u0003\u0002",
    "\u0002\u0002\u0017r\u0003\u0002\u0002\u0002\u0019t\u0003\u0002\u0002",
    "\u0002\u001bv\u0003\u0002\u0002\u0002\u001dy\u0003\u0002\u0002\u0002",
    "\u001f|\u0003\u0002\u0002\u0002!\u007f\u0003\u0002\u0002\u0002#\u0082",
    "\u0003\u0002\u0002\u0002%\u0084\u0003\u0002\u0002\u0002\'\u0086\u0003",
    "\u0002\u0002\u0002)\u0089\u0003\u0002\u0002\u0002+\u008c\u0003\u0002",
    "\u0002\u0002-\u008e\u0003\u0002\u0002\u0002/\u0090\u0003\u0002\u0002",
    "\u00021\u0092\u0003\u0002\u0002\u00023\u0094\u0003\u0002\u0002\u0002",
    "5\u0097\u0003\u0002\u0002\u000279\u0007/\u0002\u000287\u0003\u0002\u0002",
    "\u000289\u0003\u0002\u0002\u00029;\u0003\u0002\u0002\u0002:<\t\u0002",
    "\u0002\u0002;:\u0003\u0002\u0002\u0002<=\u0003\u0002\u0002\u0002=;\u0003",
    "\u0002\u0002\u0002=>\u0003\u0002\u0002\u0002>\u0004\u0003\u0002\u0002",
    "\u0002?A\u0007/\u0002\u0002@?\u0003\u0002\u0002\u0002@A\u0003\u0002",
    "\u0002\u0002AC\u0003\u0002\u0002\u0002BD\t\u0002\u0002\u0002CB\u0003",
    "\u0002\u0002\u0002DE\u0003\u0002\u0002\u0002EC\u0003\u0002\u0002\u0002",
    "EF\u0003\u0002\u0002\u0002FG\u0003\u0002\u0002\u0002GI\u00070\u0002",
    "\u0002HJ\t\u0002\u0002\u0002IH\u0003\u0002\u0002\u0002JK\u0003\u0002",
    "\u0002\u0002KI\u0003\u0002\u0002\u0002KL\u0003\u0002\u0002\u0002L\u0006",
    "\u0003\u0002\u0002\u0002MN\u0007v\u0002\u0002NO\u0007t\u0002\u0002O",
    "P\u0007w\u0002\u0002PQ\u0007g\u0002\u0002Q\b\u0003\u0002\u0002\u0002",
    "RS\u0007h\u0002\u0002ST\u0007c\u0002\u0002TU\u0007n\u0002\u0002UV\u0007",
    "u\u0002\u0002VW\u0007g\u0002\u0002W\n\u0003\u0002\u0002\u0002XY\u0007",
    "p\u0002\u0002YZ\u0007q\u0002\u0002Z[\u0007v\u0002\u0002[\f\u0003\u0002",
    "\u0002\u0002\\^\t\u0003\u0002\u0002]\\\u0003\u0002\u0002\u0002^_\u0003",
    "\u0002\u0002\u0002_]\u0003\u0002\u0002\u0002_`\u0003\u0002\u0002\u0002",
    "`\u000e\u0003\u0002\u0002\u0002ag\u0007$\u0002\u0002bc\u0007^\u0002",
    "\u0002cf\u0007$\u0002\u0002df\n\u0004\u0002\u0002eb\u0003\u0002\u0002",
    "\u0002ed\u0003\u0002\u0002\u0002fi\u0003\u0002\u0002\u0002ge\u0003\u0002",
    "\u0002\u0002gh\u0003\u0002\u0002\u0002hj\u0003\u0002\u0002\u0002ig\u0003",
    "\u0002\u0002\u0002jk\u0007$\u0002\u0002k\u0010\u0003\u0002\u0002\u0002",
    "lm\u0007*\u0002\u0002m\u0012\u0003\u0002\u0002\u0002no\u0007+\u0002",
    "\u0002o\u0014\u0003\u0002\u0002\u0002pq\u0007~\u0002\u0002q\u0016\u0003",
    "\u0002\u0002\u0002rs\u0007<\u0002\u0002s\u0018\u0003\u0002\u0002\u0002",
    "tu\u0007.\u0002\u0002u\u001a\u0003\u0002\u0002\u0002vw\u0007~\u0002",
    "\u0002wx\u0007~\u0002\u0002x\u001c\u0003\u0002\u0002\u0002yz\u0007(",
    "\u0002\u0002z{\u0007(\u0002\u0002{\u001e\u0003\u0002\u0002\u0002|}\u0007",
    "?\u0002\u0002}~\u0007?\u0002\u0002~ \u0003\u0002\u0002\u0002\u007f\u0080",
    "\u0007#\u0002\u0002\u0080\u0081\u0007?\u0002\u0002\u0081\"\u0003\u0002",
    "\u0002\u0002\u0082\u0083\u0007@\u0002\u0002\u0083$\u0003\u0002\u0002",
    "\u0002\u0084\u0085\u0007>\u0002\u0002\u0085&\u0003\u0002\u0002\u0002",
    "\u0086\u0087\u0007@\u0002\u0002\u0087\u0088\u0007?\u0002\u0002\u0088",
    "(\u0003\u0002\u0002\u0002\u0089\u008a\u0007>\u0002\u0002\u008a\u008b",
    "\u0007?\u0002\u0002\u008b*\u0003\u0002\u0002\u0002\u008c\u008d\u0007",
    "-\u0002\u0002\u008d,\u0003\u0002\u0002\u0002\u008e\u008f\u0007/\u0002",
    "\u0002\u008f.\u0003\u0002\u0002\u0002\u0090\u0091\u0007,\u0002\u0002",
    "\u00910\u0003\u0002\u0002\u0002\u0092\u0093\u00071\u0002\u0002\u0093",
    "2\u0003\u0002\u0002\u0002\u0094\u0095\u0007A\u0002\u0002\u00954\u0003",
    "\u0002\u0002\u0002\u0096\u0098\t\u0005\u0002\u0002\u0097\u0096\u0003",
    "\u0002\u0002\u0002\u0098\u0099\u0003\u0002\u0002\u0002\u0099\u0097\u0003",
    "\u0002\u0002\u0002\u0099\u009a\u0003\u0002\u0002\u0002\u009a\u009b\u0003",
    "\u0002\u0002\u0002\u009b\u009c\b\u001b\u0002\u0002\u009c6\u0003\u0002",
    "\u0002\u0002\f\u00028=@EK_eg\u0099\u0003\b\u0002\u0002"].join("");


var atn = new antlr4.atn.ATNDeserializer().deserialize(serializedATN);

var decisionsToDFA = atn.decisionToState.map( function(ds, index) { return new antlr4.dfa.DFA(ds, index); });

function TelLexer(input) {
	antlr4.Lexer.call(this, input);
    this._interp = new antlr4.atn.LexerATNSimulator(this, atn, decisionsToDFA, new antlr4.PredictionContextCache());
    return this;
}

TelLexer.prototype = Object.create(antlr4.Lexer.prototype);
TelLexer.prototype.constructor = TelLexer;

Object.defineProperty(TelLexer.prototype, "atn", {
        get : function() {
                return atn;
        }
});

TelLexer.EOF = antlr4.Token.EOF;
TelLexer.INT = 1;
TelLexer.REAL = 2;
TelLexer.TRUE = 3;
TelLexer.FALSE = 4;
TelLexer.NOT = 5;
TelLexer.WORD = 6;
TelLexer.STRING_CONSTANT = 7;
TelLexer.L_BRACKET = 8;
TelLexer.R_BRACKET = 9;
TelLexer.TAXON_NAMESPACE_DELIMITER = 10;
TelLexer.TAXON_TAG_DELIMITER = 11;
TelLexer.FN_PARAMETER_DELIMITER = 12;
TelLexer.OR = 13;
TelLexer.AND = 14;
TelLexer.EQ = 15;
TelLexer.NEQ = 16;
TelLexer.GT = 17;
TelLexer.LT = 18;
TelLexer.GTEQ = 19;
TelLexer.LTEQ = 20;
TelLexer.PLUS = 21;
TelLexer.MINUS = 22;
TelLexer.MULT = 23;
TelLexer.DIV = 24;
TelLexer.OPTIONAL_TAXON_OPERATOR = 25;
TelLexer.WS = 26;

TelLexer.prototype.channelNames = [ "DEFAULT_TOKEN_CHANNEL", "HIDDEN" ];

TelLexer.prototype.modeNames = [ "DEFAULT_MODE" ];

TelLexer.prototype.literalNames = [ null, null, null, "'true'", "'false'", 
                                    "'not'", null, null, "'('", "')'", "'|'", 
                                    "':'", "','", "'||'", "'&&'", "'=='", 
                                    "'!='", "'>'", "'<'", "'>='", "'<='", 
                                    "'+'", "'-'", "'*'", "'/'", "'?'" ];

TelLexer.prototype.symbolicNames = [ null, "INT", "REAL", "TRUE", "FALSE", 
                                     "NOT", "WORD", "STRING_CONSTANT", "L_BRACKET", 
                                     "R_BRACKET", "TAXON_NAMESPACE_DELIMITER", 
                                     "TAXON_TAG_DELIMITER", "FN_PARAMETER_DELIMITER", 
                                     "OR", "AND", "EQ", "NEQ", "GT", "LT", 
                                     "GTEQ", "LTEQ", "PLUS", "MINUS", "MULT", 
                                     "DIV", "OPTIONAL_TAXON_OPERATOR", "WS" ];

TelLexer.prototype.ruleNames = [ "INT", "REAL", "TRUE", "FALSE", "NOT", 
                                 "WORD", "STRING_CONSTANT", "L_BRACKET", 
                                 "R_BRACKET", "TAXON_NAMESPACE_DELIMITER", 
                                 "TAXON_TAG_DELIMITER", "FN_PARAMETER_DELIMITER", 
                                 "OR", "AND", "EQ", "NEQ", "GT", "LT", "GTEQ", 
                                 "LTEQ", "PLUS", "MINUS", "MULT", "DIV", 
                                 "OPTIONAL_TAXON_OPERATOR", "WS" ];

TelLexer.prototype.grammarFileName = "Tel.g4";


exports.TelLexer = TelLexer;


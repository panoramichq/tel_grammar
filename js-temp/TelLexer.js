// Generated from grammar/Tel.g4 by ANTLR 4.8
// jshint ignore: start
var antlr4 = require('antlr4/index');



var serializedATN = ["\u0003\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964",
    "\u0002\u001b\u0099\b\u0001\u0004\u0002\t\u0002\u0004\u0003\t\u0003\u0004",
    "\u0004\t\u0004\u0004\u0005\t\u0005\u0004\u0006\t\u0006\u0004\u0007\t",
    "\u0007\u0004\b\t\b\u0004\t\t\t\u0004\n\t\n\u0004\u000b\t\u000b\u0004",
    "\f\t\f\u0004\r\t\r\u0004\u000e\t\u000e\u0004\u000f\t\u000f\u0004\u0010",
    "\t\u0010\u0004\u0011\t\u0011\u0004\u0012\t\u0012\u0004\u0013\t\u0013",
    "\u0004\u0014\t\u0014\u0004\u0015\t\u0015\u0004\u0016\t\u0016\u0004\u0017",
    "\t\u0017\u0004\u0018\t\u0018\u0004\u0019\t\u0019\u0004\u001a\t\u001a",
    "\u0003\u0002\u0005\u00027\n\u0002\u0003\u0002\u0006\u0002:\n\u0002\r",
    "\u0002\u000e\u0002;\u0003\u0003\u0005\u0003?\n\u0003\u0003\u0003\u0006",
    "\u0003B\n\u0003\r\u0003\u000e\u0003C\u0003\u0003\u0003\u0003\u0006\u0003",
    "H\n\u0003\r\u0003\u000e\u0003I\u0003\u0004\u0003\u0004\u0003\u0004\u0003",
    "\u0004\u0003\u0004\u0003\u0005\u0003\u0005\u0003\u0005\u0003\u0005\u0003",
    "\u0005\u0003\u0005\u0003\u0006\u0003\u0006\u0003\u0006\u0003\u0006\u0003",
    "\u0007\u0006\u0007\\\n\u0007\r\u0007\u000e\u0007]\u0003\b\u0003\b\u0003",
    "\b\u0003\b\u0007\bd\n\b\f\b\u000e\bg\u000b\b\u0003\b\u0003\b\u0003\t",
    "\u0003\t\u0003\n\u0003\n\u0003\u000b\u0003\u000b\u0003\f\u0003\f\u0003",
    "\r\u0003\r\u0003\r\u0003\u000e\u0003\u000e\u0003\u000e\u0003\u000f\u0003",
    "\u000f\u0003\u000f\u0003\u0010\u0003\u0010\u0003\u0010\u0003\u0011\u0003",
    "\u0011\u0003\u0012\u0003\u0012\u0003\u0013\u0003\u0013\u0003\u0013\u0003",
    "\u0014\u0003\u0014\u0003\u0014\u0003\u0015\u0003\u0015\u0003\u0016\u0003",
    "\u0016\u0003\u0017\u0003\u0017\u0003\u0018\u0003\u0018\u0003\u0019\u0003",
    "\u0019\u0003\u001a\u0006\u001a\u0094\n\u001a\r\u001a\u000e\u001a\u0095",
    "\u0003\u001a\u0003\u001a\u0002\u0002\u001b\u0003\u0003\u0005\u0004\u0007",
    "\u0005\t\u0006\u000b\u0007\r\b\u000f\t\u0011\n\u0013\u000b\u0015\f\u0017",
    "\r\u0019\u000e\u001b\u000f\u001d\u0010\u001f\u0011!\u0012#\u0013%\u0014",
    "\'\u0015)\u0016+\u0017-\u0018/\u00191\u001a3\u001b\u0003\u0002\u0006",
    "\u0003\u00022;\u0006\u00022;C\\aac|\u0003\u0002$$\u0005\u0002\u000b",
    "\f\u000f\u000f\"\"\u0002\u00a1\u0002\u0003\u0003\u0002\u0002\u0002\u0002",
    "\u0005\u0003\u0002\u0002\u0002\u0002\u0007\u0003\u0002\u0002\u0002\u0002",
    "\t\u0003\u0002\u0002\u0002\u0002\u000b\u0003\u0002\u0002\u0002\u0002",
    "\r\u0003\u0002\u0002\u0002\u0002\u000f\u0003\u0002\u0002\u0002\u0002",
    "\u0011\u0003\u0002\u0002\u0002\u0002\u0013\u0003\u0002\u0002\u0002\u0002",
    "\u0015\u0003\u0002\u0002\u0002\u0002\u0017\u0003\u0002\u0002\u0002\u0002",
    "\u0019\u0003\u0002\u0002\u0002\u0002\u001b\u0003\u0002\u0002\u0002\u0002",
    "\u001d\u0003\u0002\u0002\u0002\u0002\u001f\u0003\u0002\u0002\u0002\u0002",
    "!\u0003\u0002\u0002\u0002\u0002#\u0003\u0002\u0002\u0002\u0002%\u0003",
    "\u0002\u0002\u0002\u0002\'\u0003\u0002\u0002\u0002\u0002)\u0003\u0002",
    "\u0002\u0002\u0002+\u0003\u0002\u0002\u0002\u0002-\u0003\u0002\u0002",
    "\u0002\u0002/\u0003\u0002\u0002\u0002\u00021\u0003\u0002\u0002\u0002",
    "\u00023\u0003\u0002\u0002\u0002\u00036\u0003\u0002\u0002\u0002\u0005",
    ">\u0003\u0002\u0002\u0002\u0007K\u0003\u0002\u0002\u0002\tP\u0003\u0002",
    "\u0002\u0002\u000bV\u0003\u0002\u0002\u0002\r[\u0003\u0002\u0002\u0002",
    "\u000f_\u0003\u0002\u0002\u0002\u0011j\u0003\u0002\u0002\u0002\u0013",
    "l\u0003\u0002\u0002\u0002\u0015n\u0003\u0002\u0002\u0002\u0017p\u0003",
    "\u0002\u0002\u0002\u0019r\u0003\u0002\u0002\u0002\u001bu\u0003\u0002",
    "\u0002\u0002\u001dx\u0003\u0002\u0002\u0002\u001f{\u0003\u0002\u0002",
    "\u0002!~\u0003\u0002\u0002\u0002#\u0080\u0003\u0002\u0002\u0002%\u0082",
    "\u0003\u0002\u0002\u0002\'\u0085\u0003\u0002\u0002\u0002)\u0088\u0003",
    "\u0002\u0002\u0002+\u008a\u0003\u0002\u0002\u0002-\u008c\u0003\u0002",
    "\u0002\u0002/\u008e\u0003\u0002\u0002\u00021\u0090\u0003\u0002\u0002",
    "\u00023\u0093\u0003\u0002\u0002\u000257\u0007/\u0002\u000265\u0003\u0002",
    "\u0002\u000267\u0003\u0002\u0002\u000279\u0003\u0002\u0002\u00028:\t",
    "\u0002\u0002\u000298\u0003\u0002\u0002\u0002:;\u0003\u0002\u0002\u0002",
    ";9\u0003\u0002\u0002\u0002;<\u0003\u0002\u0002\u0002<\u0004\u0003\u0002",
    "\u0002\u0002=?\u0007/\u0002\u0002>=\u0003\u0002\u0002\u0002>?\u0003",
    "\u0002\u0002\u0002?A\u0003\u0002\u0002\u0002@B\t\u0002\u0002\u0002A",
    "@\u0003\u0002\u0002\u0002BC\u0003\u0002\u0002\u0002CA\u0003\u0002\u0002",
    "\u0002CD\u0003\u0002\u0002\u0002DE\u0003\u0002\u0002\u0002EG\u00070",
    "\u0002\u0002FH\t\u0002\u0002\u0002GF\u0003\u0002\u0002\u0002HI\u0003",
    "\u0002\u0002\u0002IG\u0003\u0002\u0002\u0002IJ\u0003\u0002\u0002\u0002",
    "J\u0006\u0003\u0002\u0002\u0002KL\u0007v\u0002\u0002LM\u0007t\u0002",
    "\u0002MN\u0007w\u0002\u0002NO\u0007g\u0002\u0002O\b\u0003\u0002\u0002",
    "\u0002PQ\u0007h\u0002\u0002QR\u0007c\u0002\u0002RS\u0007n\u0002\u0002",
    "ST\u0007u\u0002\u0002TU\u0007g\u0002\u0002U\n\u0003\u0002\u0002\u0002",
    "VW\u0007p\u0002\u0002WX\u0007q\u0002\u0002XY\u0007v\u0002\u0002Y\f\u0003",
    "\u0002\u0002\u0002Z\\\t\u0003\u0002\u0002[Z\u0003\u0002\u0002\u0002",
    "\\]\u0003\u0002\u0002\u0002][\u0003\u0002\u0002\u0002]^\u0003\u0002",
    "\u0002\u0002^\u000e\u0003\u0002\u0002\u0002_e\u0007$\u0002\u0002`a\u0007",
    "^\u0002\u0002ad\u0007$\u0002\u0002bd\n\u0004\u0002\u0002c`\u0003\u0002",
    "\u0002\u0002cb\u0003\u0002\u0002\u0002dg\u0003\u0002\u0002\u0002ec\u0003",
    "\u0002\u0002\u0002ef\u0003\u0002\u0002\u0002fh\u0003\u0002\u0002\u0002",
    "ge\u0003\u0002\u0002\u0002hi\u0007$\u0002\u0002i\u0010\u0003\u0002\u0002",
    "\u0002jk\u0007*\u0002\u0002k\u0012\u0003\u0002\u0002\u0002lm\u0007+",
    "\u0002\u0002m\u0014\u0003\u0002\u0002\u0002no\u0007~\u0002\u0002o\u0016",
    "\u0003\u0002\u0002\u0002pq\u0007.\u0002\u0002q\u0018\u0003\u0002\u0002",
    "\u0002rs\u0007~\u0002\u0002st\u0007~\u0002\u0002t\u001a\u0003\u0002",
    "\u0002\u0002uv\u0007(\u0002\u0002vw\u0007(\u0002\u0002w\u001c\u0003",
    "\u0002\u0002\u0002xy\u0007?\u0002\u0002yz\u0007?\u0002\u0002z\u001e",
    "\u0003\u0002\u0002\u0002{|\u0007#\u0002\u0002|}\u0007?\u0002\u0002}",
    " \u0003\u0002\u0002\u0002~\u007f\u0007@\u0002\u0002\u007f\"\u0003\u0002",
    "\u0002\u0002\u0080\u0081\u0007>\u0002\u0002\u0081$\u0003\u0002\u0002",
    "\u0002\u0082\u0083\u0007@\u0002\u0002\u0083\u0084\u0007?\u0002\u0002",
    "\u0084&\u0003\u0002\u0002\u0002\u0085\u0086\u0007>\u0002\u0002\u0086",
    "\u0087\u0007?\u0002\u0002\u0087(\u0003\u0002\u0002\u0002\u0088\u0089",
    "\u0007-\u0002\u0002\u0089*\u0003\u0002\u0002\u0002\u008a\u008b\u0007",
    "/\u0002\u0002\u008b,\u0003\u0002\u0002\u0002\u008c\u008d\u0007,\u0002",
    "\u0002\u008d.\u0003\u0002\u0002\u0002\u008e\u008f\u00071\u0002\u0002",
    "\u008f0\u0003\u0002\u0002\u0002\u0090\u0091\u0007A\u0002\u0002\u0091",
    "2\u0003\u0002\u0002\u0002\u0092\u0094\t\u0005\u0002\u0002\u0093\u0092",
    "\u0003\u0002\u0002\u0002\u0094\u0095\u0003\u0002\u0002\u0002\u0095\u0093",
    "\u0003\u0002\u0002\u0002\u0095\u0096\u0003\u0002\u0002\u0002\u0096\u0097",
    "\u0003\u0002\u0002\u0002\u0097\u0098\b\u001a\u0002\u0002\u00984\u0003",
    "\u0002\u0002\u0002\f\u00026;>CI]ce\u0095\u0003\b\u0002\u0002"].join("");


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
TelLexer.FN_PARAMETER_DELIMITER = 11;
TelLexer.OR = 12;
TelLexer.AND = 13;
TelLexer.EQ = 14;
TelLexer.NEQ = 15;
TelLexer.GT = 16;
TelLexer.LT = 17;
TelLexer.GTEQ = 18;
TelLexer.LTEQ = 19;
TelLexer.PLUS = 20;
TelLexer.MINUS = 21;
TelLexer.MULT = 22;
TelLexer.DIV = 23;
TelLexer.OPTIONAL_TAXON_OPERATOR = 24;
TelLexer.WS = 25;

TelLexer.prototype.channelNames = [ "DEFAULT_TOKEN_CHANNEL", "HIDDEN" ];

TelLexer.prototype.modeNames = [ "DEFAULT_MODE" ];

TelLexer.prototype.literalNames = [ null, null, null, "'true'", "'false'", 
                                    "'not'", null, null, "'('", "')'", "'|'", 
                                    "','", "'||'", "'&&'", "'=='", "'!='", 
                                    "'>'", "'<'", "'>='", "'<='", "'+'", 
                                    "'-'", "'*'", "'/'", "'?'" ];

TelLexer.prototype.symbolicNames = [ null, "INT", "REAL", "TRUE", "FALSE", 
                                     "NOT", "WORD", "STRING_CONSTANT", "L_BRACKET", 
                                     "R_BRACKET", "TAXON_NAMESPACE_DELIMITER", 
                                     "FN_PARAMETER_DELIMITER", "OR", "AND", 
                                     "EQ", "NEQ", "GT", "LT", "GTEQ", "LTEQ", 
                                     "PLUS", "MINUS", "MULT", "DIV", "OPTIONAL_TAXON_OPERATOR", 
                                     "WS" ];

TelLexer.prototype.ruleNames = [ "INT", "REAL", "TRUE", "FALSE", "NOT", 
                                 "WORD", "STRING_CONSTANT", "L_BRACKET", 
                                 "R_BRACKET", "TAXON_NAMESPACE_DELIMITER", 
                                 "FN_PARAMETER_DELIMITER", "OR", "AND", 
                                 "EQ", "NEQ", "GT", "LT", "GTEQ", "LTEQ", 
                                 "PLUS", "MINUS", "MULT", "DIV", "OPTIONAL_TAXON_OPERATOR", 
                                 "WS" ];

TelLexer.prototype.grammarFileName = "Tel.g4";


exports.TelLexer = TelLexer;


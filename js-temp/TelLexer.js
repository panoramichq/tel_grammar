// Generated from grammar/Tel.g4 by ANTLR 4.8
// jshint ignore: start
var antlr4 = require('antlr4/index');



var serializedATN = ["\u0003\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964",
    "\u0002\u001a\u0095\b\u0001\u0004\u0002\t\u0002\u0004\u0003\t\u0003\u0004",
    "\u0004\t\u0004\u0004\u0005\t\u0005\u0004\u0006\t\u0006\u0004\u0007\t",
    "\u0007\u0004\b\t\b\u0004\t\t\t\u0004\n\t\n\u0004\u000b\t\u000b\u0004",
    "\f\t\f\u0004\r\t\r\u0004\u000e\t\u000e\u0004\u000f\t\u000f\u0004\u0010",
    "\t\u0010\u0004\u0011\t\u0011\u0004\u0012\t\u0012\u0004\u0013\t\u0013",
    "\u0004\u0014\t\u0014\u0004\u0015\t\u0015\u0004\u0016\t\u0016\u0004\u0017",
    "\t\u0017\u0004\u0018\t\u0018\u0004\u0019\t\u0019\u0003\u0002\u0005\u0002",
    "5\n\u0002\u0003\u0002\u0006\u00028\n\u0002\r\u0002\u000e\u00029\u0003",
    "\u0003\u0005\u0003=\n\u0003\u0003\u0003\u0006\u0003@\n\u0003\r\u0003",
    "\u000e\u0003A\u0003\u0003\u0003\u0003\u0006\u0003F\n\u0003\r\u0003\u000e",
    "\u0003G\u0003\u0004\u0003\u0004\u0003\u0004\u0003\u0004\u0003\u0004",
    "\u0003\u0005\u0003\u0005\u0003\u0005\u0003\u0005\u0003\u0005\u0003\u0005",
    "\u0003\u0006\u0003\u0006\u0003\u0006\u0003\u0006\u0003\u0007\u0006\u0007",
    "Z\n\u0007\r\u0007\u000e\u0007[\u0003\b\u0003\b\u0003\b\u0003\b\u0007",
    "\bb\n\b\f\b\u000e\be\u000b\b\u0003\b\u0003\b\u0003\t\u0003\t\u0003\n",
    "\u0003\n\u0003\u000b\u0003\u000b\u0003\f\u0003\f\u0003\r\u0003\r\u0003",
    "\r\u0003\u000e\u0003\u000e\u0003\u000e\u0003\u000f\u0003\u000f\u0003",
    "\u000f\u0003\u0010\u0003\u0010\u0003\u0010\u0003\u0011\u0003\u0011\u0003",
    "\u0012\u0003\u0012\u0003\u0013\u0003\u0013\u0003\u0013\u0003\u0014\u0003",
    "\u0014\u0003\u0014\u0003\u0015\u0003\u0015\u0003\u0016\u0003\u0016\u0003",
    "\u0017\u0003\u0017\u0003\u0018\u0003\u0018\u0003\u0019\u0006\u0019\u0090",
    "\n\u0019\r\u0019\u000e\u0019\u0091\u0003\u0019\u0003\u0019\u0002\u0002",
    "\u001a\u0003\u0003\u0005\u0004\u0007\u0005\t\u0006\u000b\u0007\r\b\u000f",
    "\t\u0011\n\u0013\u000b\u0015\f\u0017\r\u0019\u000e\u001b\u000f\u001d",
    "\u0010\u001f\u0011!\u0012#\u0013%\u0014\'\u0015)\u0016+\u0017-\u0018",
    "/\u00191\u001a\u0003\u0002\u0006\u0003\u00022;\u0006\u00022;C\\aac|",
    "\u0003\u0002$$\u0005\u0002\u000b\f\u000f\u000f\"\"\u0002\u009d\u0002",
    "\u0003\u0003\u0002\u0002\u0002\u0002\u0005\u0003\u0002\u0002\u0002\u0002",
    "\u0007\u0003\u0002\u0002\u0002\u0002\t\u0003\u0002\u0002\u0002\u0002",
    "\u000b\u0003\u0002\u0002\u0002\u0002\r\u0003\u0002\u0002\u0002\u0002",
    "\u000f\u0003\u0002\u0002\u0002\u0002\u0011\u0003\u0002\u0002\u0002\u0002",
    "\u0013\u0003\u0002\u0002\u0002\u0002\u0015\u0003\u0002\u0002\u0002\u0002",
    "\u0017\u0003\u0002\u0002\u0002\u0002\u0019\u0003\u0002\u0002\u0002\u0002",
    "\u001b\u0003\u0002\u0002\u0002\u0002\u001d\u0003\u0002\u0002\u0002\u0002",
    "\u001f\u0003\u0002\u0002\u0002\u0002!\u0003\u0002\u0002\u0002\u0002",
    "#\u0003\u0002\u0002\u0002\u0002%\u0003\u0002\u0002\u0002\u0002\'\u0003",
    "\u0002\u0002\u0002\u0002)\u0003\u0002\u0002\u0002\u0002+\u0003\u0002",
    "\u0002\u0002\u0002-\u0003\u0002\u0002\u0002\u0002/\u0003\u0002\u0002",
    "\u0002\u00021\u0003\u0002\u0002\u0002\u00034\u0003\u0002\u0002\u0002",
    "\u0005<\u0003\u0002\u0002\u0002\u0007I\u0003\u0002\u0002\u0002\tN\u0003",
    "\u0002\u0002\u0002\u000bT\u0003\u0002\u0002\u0002\rY\u0003\u0002\u0002",
    "\u0002\u000f]\u0003\u0002\u0002\u0002\u0011h\u0003\u0002\u0002\u0002",
    "\u0013j\u0003\u0002\u0002\u0002\u0015l\u0003\u0002\u0002\u0002\u0017",
    "n\u0003\u0002\u0002\u0002\u0019p\u0003\u0002\u0002\u0002\u001bs\u0003",
    "\u0002\u0002\u0002\u001dv\u0003\u0002\u0002\u0002\u001fy\u0003\u0002",
    "\u0002\u0002!|\u0003\u0002\u0002\u0002#~\u0003\u0002\u0002\u0002%\u0080",
    "\u0003\u0002\u0002\u0002\'\u0083\u0003\u0002\u0002\u0002)\u0086\u0003",
    "\u0002\u0002\u0002+\u0088\u0003\u0002\u0002\u0002-\u008a\u0003\u0002",
    "\u0002\u0002/\u008c\u0003\u0002\u0002\u00021\u008f\u0003\u0002\u0002",
    "\u000235\u0007/\u0002\u000243\u0003\u0002\u0002\u000245\u0003\u0002",
    "\u0002\u000257\u0003\u0002\u0002\u000268\t\u0002\u0002\u000276\u0003",
    "\u0002\u0002\u000289\u0003\u0002\u0002\u000297\u0003\u0002\u0002\u0002",
    "9:\u0003\u0002\u0002\u0002:\u0004\u0003\u0002\u0002\u0002;=\u0007/\u0002",
    "\u0002<;\u0003\u0002\u0002\u0002<=\u0003\u0002\u0002\u0002=?\u0003\u0002",
    "\u0002\u0002>@\t\u0002\u0002\u0002?>\u0003\u0002\u0002\u0002@A\u0003",
    "\u0002\u0002\u0002A?\u0003\u0002\u0002\u0002AB\u0003\u0002\u0002\u0002",
    "BC\u0003\u0002\u0002\u0002CE\u00070\u0002\u0002DF\t\u0002\u0002\u0002",
    "ED\u0003\u0002\u0002\u0002FG\u0003\u0002\u0002\u0002GE\u0003\u0002\u0002",
    "\u0002GH\u0003\u0002\u0002\u0002H\u0006\u0003\u0002\u0002\u0002IJ\u0007",
    "v\u0002\u0002JK\u0007t\u0002\u0002KL\u0007w\u0002\u0002LM\u0007g\u0002",
    "\u0002M\b\u0003\u0002\u0002\u0002NO\u0007h\u0002\u0002OP\u0007c\u0002",
    "\u0002PQ\u0007n\u0002\u0002QR\u0007u\u0002\u0002RS\u0007g\u0002\u0002",
    "S\n\u0003\u0002\u0002\u0002TU\u0007p\u0002\u0002UV\u0007q\u0002\u0002",
    "VW\u0007v\u0002\u0002W\f\u0003\u0002\u0002\u0002XZ\t\u0003\u0002\u0002",
    "YX\u0003\u0002\u0002\u0002Z[\u0003\u0002\u0002\u0002[Y\u0003\u0002\u0002",
    "\u0002[\\\u0003\u0002\u0002\u0002\\\u000e\u0003\u0002\u0002\u0002]c",
    "\u0007$\u0002\u0002^_\u0007^\u0002\u0002_b\u0007$\u0002\u0002`b\n\u0004",
    "\u0002\u0002a^\u0003\u0002\u0002\u0002a`\u0003\u0002\u0002\u0002be\u0003",
    "\u0002\u0002\u0002ca\u0003\u0002\u0002\u0002cd\u0003\u0002\u0002\u0002",
    "df\u0003\u0002\u0002\u0002ec\u0003\u0002\u0002\u0002fg\u0007$\u0002",
    "\u0002g\u0010\u0003\u0002\u0002\u0002hi\u0007*\u0002\u0002i\u0012\u0003",
    "\u0002\u0002\u0002jk\u0007+\u0002\u0002k\u0014\u0003\u0002\u0002\u0002",
    "lm\u0007~\u0002\u0002m\u0016\u0003\u0002\u0002\u0002no\u0007.\u0002",
    "\u0002o\u0018\u0003\u0002\u0002\u0002pq\u0007~\u0002\u0002qr\u0007~",
    "\u0002\u0002r\u001a\u0003\u0002\u0002\u0002st\u0007(\u0002\u0002tu\u0007",
    "(\u0002\u0002u\u001c\u0003\u0002\u0002\u0002vw\u0007?\u0002\u0002wx",
    "\u0007?\u0002\u0002x\u001e\u0003\u0002\u0002\u0002yz\u0007#\u0002\u0002",
    "z{\u0007?\u0002\u0002{ \u0003\u0002\u0002\u0002|}\u0007@\u0002\u0002",
    "}\"\u0003\u0002\u0002\u0002~\u007f\u0007>\u0002\u0002\u007f$\u0003\u0002",
    "\u0002\u0002\u0080\u0081\u0007@\u0002\u0002\u0081\u0082\u0007?\u0002",
    "\u0002\u0082&\u0003\u0002\u0002\u0002\u0083\u0084\u0007>\u0002\u0002",
    "\u0084\u0085\u0007?\u0002\u0002\u0085(\u0003\u0002\u0002\u0002\u0086",
    "\u0087\u0007-\u0002\u0002\u0087*\u0003\u0002\u0002\u0002\u0088\u0089",
    "\u0007/\u0002\u0002\u0089,\u0003\u0002\u0002\u0002\u008a\u008b\u0007",
    ",\u0002\u0002\u008b.\u0003\u0002\u0002\u0002\u008c\u008d\u00071\u0002",
    "\u0002\u008d0\u0003\u0002\u0002\u0002\u008e\u0090\t\u0005\u0002\u0002",
    "\u008f\u008e\u0003\u0002\u0002\u0002\u0090\u0091\u0003\u0002\u0002\u0002",
    "\u0091\u008f\u0003\u0002\u0002\u0002\u0091\u0092\u0003\u0002\u0002\u0002",
    "\u0092\u0093\u0003\u0002\u0002\u0002\u0093\u0094\b\u0019\u0002\u0002",
    "\u00942\u0003\u0002\u0002\u0002\f\u000249<AG[ac\u0091\u0003\b\u0002",
    "\u0002"].join("");


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
TelLexer.WS = 24;

TelLexer.prototype.channelNames = [ "DEFAULT_TOKEN_CHANNEL", "HIDDEN" ];

TelLexer.prototype.modeNames = [ "DEFAULT_MODE" ];

TelLexer.prototype.literalNames = [ null, null, null, "'true'", "'false'", 
                                    "'not'", null, null, "'('", "')'", "'|'", 
                                    "','", "'||'", "'&&'", "'=='", "'!='", 
                                    "'>'", "'<'", "'>='", "'<='", "'+'", 
                                    "'-'", "'*'", "'/'" ];

TelLexer.prototype.symbolicNames = [ null, "INT", "REAL", "TRUE", "FALSE", 
                                     "NOT", "WORD", "STRING_CONSTANT", "L_BRACKET", 
                                     "R_BRACKET", "TAXON_NAMESPACE_DELIMITER", 
                                     "FN_PARAMETER_DELIMITER", "OR", "AND", 
                                     "EQ", "NEQ", "GT", "LT", "GTEQ", "LTEQ", 
                                     "PLUS", "MINUS", "MULT", "DIV", "WS" ];

TelLexer.prototype.ruleNames = [ "INT", "REAL", "TRUE", "FALSE", "NOT", 
                                 "WORD", "STRING_CONSTANT", "L_BRACKET", 
                                 "R_BRACKET", "TAXON_NAMESPACE_DELIMITER", 
                                 "FN_PARAMETER_DELIMITER", "OR", "AND", 
                                 "EQ", "NEQ", "GT", "LT", "GTEQ", "LTEQ", 
                                 "PLUS", "MINUS", "MULT", "DIV", "WS" ];

TelLexer.prototype.grammarFileName = "Tel.g4";


exports.TelLexer = TelLexer;


// Generated from grammar/PqlLexer.g4 by ANTLR 4.8
// jshint ignore: start
var antlr4 = require('antlr4/index');



var serializedATN = ["\u0003\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964",
    "\u0002:\u01fd\b\u0001\u0004\u0002\t\u0002\u0004\u0003\t\u0003\u0004",
    "\u0004\t\u0004\u0004\u0005\t\u0005\u0004\u0006\t\u0006\u0004\u0007\t",
    "\u0007\u0004\b\t\b\u0004\t\t\t\u0004\n\t\n\u0004\u000b\t\u000b\u0004",
    "\f\t\f\u0004\r\t\r\u0004\u000e\t\u000e\u0004\u000f\t\u000f\u0004\u0010",
    "\t\u0010\u0004\u0011\t\u0011\u0004\u0012\t\u0012\u0004\u0013\t\u0013",
    "\u0004\u0014\t\u0014\u0004\u0015\t\u0015\u0004\u0016\t\u0016\u0004\u0017",
    "\t\u0017\u0004\u0018\t\u0018\u0004\u0019\t\u0019\u0004\u001a\t\u001a",
    "\u0004\u001b\t\u001b\u0004\u001c\t\u001c\u0004\u001d\t\u001d\u0004\u001e",
    "\t\u001e\u0004\u001f\t\u001f\u0004 \t \u0004!\t!\u0004\"\t\"\u0004#",
    "\t#\u0004$\t$\u0004%\t%\u0004&\t&\u0004\'\t\'\u0004(\t(\u0004)\t)\u0004",
    "*\t*\u0004+\t+\u0004,\t,\u0004-\t-\u0004.\t.\u0004/\t/\u00040\t0\u0004",
    "1\t1\u00042\t2\u00043\t3\u00044\t4\u00045\t5\u00046\t6\u00047\t7\u0004",
    "8\t8\u00049\t9\u0004:\t:\u0004;\t;\u0004<\t<\u0004=\t=\u0004>\t>\u0004",
    "?\t?\u0004@\t@\u0004A\tA\u0004B\tB\u0004C\tC\u0004D\tD\u0004E\tE\u0004",
    "F\tF\u0004G\tG\u0004H\tH\u0004I\tI\u0004J\tJ\u0004K\tK\u0004L\tL\u0004",
    "M\tM\u0004N\tN\u0004O\tO\u0004P\tP\u0004Q\tQ\u0004R\tR\u0004S\tS\u0004",
    "T\tT\u0003\u0002\u0003\u0002\u0003\u0003\u0003\u0003\u0003\u0004\u0003",
    "\u0004\u0003\u0004\u0003\u0005\u0003\u0005\u0003\u0005\u0003\u0006\u0003",
    "\u0006\u0003\u0006\u0003\u0007\u0003\u0007\u0003\u0007\u0003\b\u0003",
    "\b\u0003\b\u0003\t\u0003\t\u0003\t\u0003\n\u0003\n\u0003\n\u0003\u000b",
    "\u0003\u000b\u0003\u000b\u0003\f\u0003\f\u0003\f\u0003\r\u0003\r\u0003",
    "\u000e\u0003\u000e\u0003\u000f\u0003\u000f\u0003\u0010\u0003\u0010\u0003",
    "\u0011\u0003\u0011\u0003\u0012\u0003\u0012\u0003\u0013\u0003\u0013\u0003",
    "\u0014\u0003\u0014\u0003\u0015\u0003\u0015\u0003\u0016\u0003\u0016\u0003",
    "\u0017\u0003\u0017\u0003\u0018\u0003\u0018\u0003\u0019\u0003\u0019\u0003",
    "\u001a\u0003\u001a\u0003\u001b\u0003\u001b\u0003\u001c\u0003\u001c\u0003",
    "\u001d\u0003\u001d\u0003\u001e\u0003\u001e\u0003\u001e\u0003\u001e\u0003",
    "\u001f\u0003\u001f\u0003\u001f\u0003\u001f\u0003 \u0003 \u0003 \u0003",
    "!\u0003!\u0003!\u0003!\u0003!\u0003\"\u0003\"\u0003\"\u0003\"\u0003",
    "\"\u0003\"\u0003#\u0003#\u0003#\u0003$\u0003$\u0003$\u0003$\u0003$\u0003",
    "$\u0003$\u0003%\u0003%\u0003%\u0003%\u0003%\u0003&\u0003&\u0003&\u0003",
    "&\u0003&\u0003&\u0003\'\u0003\'\u0003\'\u0003\'\u0003(\u0003(\u0003",
    "(\u0003(\u0003(\u0003(\u0003(\u0003(\u0003)\u0003)\u0003)\u0003)\u0003",
    ")\u0003*\u0003*\u0003*\u0003+\u0003+\u0003+\u0003+\u0003+\u0003+\u0003",
    ",\u0003,\u0003,\u0003,\u0003,\u0003,\u0003,\u0003-\u0003-\u0003-\u0003",
    "-\u0003-\u0003.\u0003.\u0003.\u0003.\u0003.\u0003.\u0003/\u0006/\u0143",
    "\n/\r/\u000e/\u0144\u0003/\u0003/\u0007/\u0149\n/\f/\u000e/\u014c\u000b",
    "/\u0005/\u014e\n/\u0003/\u0003/\u0005/\u0152\n/\u0003/\u0006/\u0155",
    "\n/\r/\u000e/\u0156\u0005/\u0159\n/\u0003/\u0003/\u0006/\u015d\n/\r",
    "/\u000e/\u015e\u0003/\u0003/\u0005/\u0163\n/\u0003/\u0006/\u0166\n/",
    "\r/\u000e/\u0167\u0005/\u016a\n/\u0005/\u016c\n/\u00030\u00030\u0003",
    "1\u00031\u00031\u00031\u00071\u0174\n1\f1\u000e1\u0177\u000b1\u0003",
    "1\u00031\u00032\u00032\u00032\u00032\u00072\u017f\n2\f2\u000e2\u0182",
    "\u000b2\u00032\u00032\u00033\u00033\u00034\u00034\u00034\u00034\u0007",
    "4\u018c\n4\f4\u000e4\u018f\u000b4\u00034\u00034\u00035\u00035\u0003",
    "5\u00035\u00075\u0197\n5\f5\u000e5\u019a\u000b5\u00035\u00035\u0003",
    "6\u00036\u00036\u00036\u00036\u00056\u01a3\n6\u00036\u00076\u01a6\n",
    "6\f6\u000e6\u01a9\u000b6\u00036\u00036\u00037\u00037\u00037\u00037\u0007",
    "7\u01b1\n7\f7\u000e7\u01b4\u000b7\u00037\u00037\u00037\u00057\u01b9",
    "\n7\u00037\u00037\u00038\u00038\u00038\u00038\u00039\u00039\u00079\u01c3",
    "\n9\f9\u000e9\u01c6\u000b9\u0003:\u0003:\u0003;\u0003;\u0003<\u0003",
    "<\u0003=\u0003=\u0003>\u0003>\u0003?\u0003?\u0003@\u0003@\u0003A\u0003",
    "A\u0003B\u0003B\u0003C\u0003C\u0003D\u0003D\u0003E\u0003E\u0003F\u0003",
    "F\u0003G\u0003G\u0003H\u0003H\u0003I\u0003I\u0003J\u0003J\u0003K\u0003",
    "K\u0003L\u0003L\u0003M\u0003M\u0003N\u0003N\u0003O\u0003O\u0003P\u0003",
    "P\u0003Q\u0003Q\u0003R\u0003R\u0003S\u0003S\u0003T\u0003T\u0003\u01b2",
    "\u0002U\u0003\u0003\u0005\u0004\u0007\u0005\t\u0006\u000b\u0007\r\b",
    "\u000f\t\u0011\n\u0013\u000b\u0015\f\u0017\r\u0019\u000e\u001b\u000f",
    "\u001d\u0010\u001f\u0011!\u0012#\u0013%\u0014\'\u0015)\u0016+\u0017",
    "-\u0018/\u00191\u001a3\u001b5\u001c7\u001d9\u001e;\u001f= ?!A\"C#E$",
    "G%I&K\'M(O)Q*S+U,W-Y.[/]0_1a2c3e4g5i6k7m8o9q:s\u0002u\u0002w\u0002y",
    "\u0002{\u0002}\u0002\u007f\u0002\u0081\u0002\u0083\u0002\u0085\u0002",
    "\u0087\u0002\u0089\u0002\u008b\u0002\u008d\u0002\u008f\u0002\u0091\u0002",
    "\u0093\u0002\u0095\u0002\u0097\u0002\u0099\u0002\u009b\u0002\u009d\u0002",
    "\u009f\u0002\u00a1\u0002\u00a3\u0002\u00a5\u0002\u00a7\u0002\u0003\u0002",
    "$\u0004\u0002--//\u0003\u0002$$\u0003\u0002))\u0004\u0002\f\f\u000f",
    "\u000f\u0005\u0002\u000b\r\u000f\u000f\"\"\u0005\u0002C\\aac|\u0006",
    "\u00022;C\\aac|\u0003\u00022;\u0004\u0002CCcc\u0004\u0002DDdd\u0004",
    "\u0002EEee\u0004\u0002FFff\u0004\u0002GGgg\u0004\u0002HHhh\u0004\u0002",
    "IIii\u0004\u0002JJjj\u0004\u0002KKkk\u0004\u0002LLll\u0004\u0002MMm",
    "m\u0004\u0002NNnn\u0004\u0002OOoo\u0004\u0002PPpp\u0004\u0002QQqq\u0004",
    "\u0002RRrr\u0004\u0002SSss\u0004\u0002TTtt\u0004\u0002UUuu\u0004\u0002",
    "VVvv\u0004\u0002WWww\u0004\u0002XXxx\u0004\u0002YYyy\u0004\u0002ZZz",
    "z\u0004\u0002[[{{\u0004\u0002\\\\||\u0002\u01fa\u0002\u0003\u0003\u0002",
    "\u0002\u0002\u0002\u0005\u0003\u0002\u0002\u0002\u0002\u0007\u0003\u0002",
    "\u0002\u0002\u0002\t\u0003\u0002\u0002\u0002\u0002\u000b\u0003\u0002",
    "\u0002\u0002\u0002\r\u0003\u0002\u0002\u0002\u0002\u000f\u0003\u0002",
    "\u0002\u0002\u0002\u0011\u0003\u0002\u0002\u0002\u0002\u0013\u0003\u0002",
    "\u0002\u0002\u0002\u0015\u0003\u0002\u0002\u0002\u0002\u0017\u0003\u0002",
    "\u0002\u0002\u0002\u0019\u0003\u0002\u0002\u0002\u0002\u001b\u0003\u0002",
    "\u0002\u0002\u0002\u001d\u0003\u0002\u0002\u0002\u0002\u001f\u0003\u0002",
    "\u0002\u0002\u0002!\u0003\u0002\u0002\u0002\u0002#\u0003\u0002\u0002",
    "\u0002\u0002%\u0003\u0002\u0002\u0002\u0002\'\u0003\u0002\u0002\u0002",
    "\u0002)\u0003\u0002\u0002\u0002\u0002+\u0003\u0002\u0002\u0002\u0002",
    "-\u0003\u0002\u0002\u0002\u0002/\u0003\u0002\u0002\u0002\u00021\u0003",
    "\u0002\u0002\u0002\u00023\u0003\u0002\u0002\u0002\u00025\u0003\u0002",
    "\u0002\u0002\u00027\u0003\u0002\u0002\u0002\u00029\u0003\u0002\u0002",
    "\u0002\u0002;\u0003\u0002\u0002\u0002\u0002=\u0003\u0002\u0002\u0002",
    "\u0002?\u0003\u0002\u0002\u0002\u0002A\u0003\u0002\u0002\u0002\u0002",
    "C\u0003\u0002\u0002\u0002\u0002E\u0003\u0002\u0002\u0002\u0002G\u0003",
    "\u0002\u0002\u0002\u0002I\u0003\u0002\u0002\u0002\u0002K\u0003\u0002",
    "\u0002\u0002\u0002M\u0003\u0002\u0002\u0002\u0002O\u0003\u0002\u0002",
    "\u0002\u0002Q\u0003\u0002\u0002\u0002\u0002S\u0003\u0002\u0002\u0002",
    "\u0002U\u0003\u0002\u0002\u0002\u0002W\u0003\u0002\u0002\u0002\u0002",
    "Y\u0003\u0002\u0002\u0002\u0002[\u0003\u0002\u0002\u0002\u0002]\u0003",
    "\u0002\u0002\u0002\u0002_\u0003\u0002\u0002\u0002\u0002a\u0003\u0002",
    "\u0002\u0002\u0002c\u0003\u0002\u0002\u0002\u0002e\u0003\u0002\u0002",
    "\u0002\u0002g\u0003\u0002\u0002\u0002\u0002i\u0003\u0002\u0002\u0002",
    "\u0002k\u0003\u0002\u0002\u0002\u0002m\u0003\u0002\u0002\u0002\u0002",
    "o\u0003\u0002\u0002\u0002\u0002q\u0003\u0002\u0002\u0002\u0003\u00a9",
    "\u0003\u0002\u0002\u0002\u0005\u00ab\u0003\u0002\u0002\u0002\u0007\u00ad",
    "\u0003\u0002\u0002\u0002\t\u00b0\u0003\u0002\u0002\u0002\u000b\u00b3",
    "\u0003\u0002\u0002\u0002\r\u00b6\u0003\u0002\u0002\u0002\u000f\u00b9",
    "\u0003\u0002\u0002\u0002\u0011\u00bc\u0003\u0002\u0002\u0002\u0013\u00bf",
    "\u0003\u0002\u0002\u0002\u0015\u00c2\u0003\u0002\u0002\u0002\u0017\u00c5",
    "\u0003\u0002\u0002\u0002\u0019\u00c8\u0003\u0002\u0002\u0002\u001b\u00ca",
    "\u0003\u0002\u0002\u0002\u001d\u00cc\u0003\u0002\u0002\u0002\u001f\u00ce",
    "\u0003\u0002\u0002\u0002!\u00d0\u0003\u0002\u0002\u0002#\u00d2\u0003",
    "\u0002\u0002\u0002%\u00d4\u0003\u0002\u0002\u0002\'\u00d6\u0003\u0002",
    "\u0002\u0002)\u00d8\u0003\u0002\u0002\u0002+\u00da\u0003\u0002\u0002",
    "\u0002-\u00dc\u0003\u0002\u0002\u0002/\u00de\u0003\u0002\u0002\u0002",
    "1\u00e0\u0003\u0002\u0002\u00023\u00e2\u0003\u0002\u0002\u00025\u00e4",
    "\u0003\u0002\u0002\u00027\u00e6\u0003\u0002\u0002\u00029\u00e8\u0003",
    "\u0002\u0002\u0002;\u00ea\u0003\u0002\u0002\u0002=\u00ee\u0003\u0002",
    "\u0002\u0002?\u00f2\u0003\u0002\u0002\u0002A\u00f5\u0003\u0002\u0002",
    "\u0002C\u00fa\u0003\u0002\u0002\u0002E\u0100\u0003\u0002\u0002\u0002",
    "G\u0103\u0003\u0002\u0002\u0002I\u010a\u0003\u0002\u0002\u0002K\u010f",
    "\u0003\u0002\u0002\u0002M\u0115\u0003\u0002\u0002\u0002O\u0119\u0003",
    "\u0002\u0002\u0002Q\u0121\u0003\u0002\u0002\u0002S\u0126\u0003\u0002",
    "\u0002\u0002U\u0129\u0003\u0002\u0002\u0002W\u012f\u0003\u0002\u0002",
    "\u0002Y\u0136\u0003\u0002\u0002\u0002[\u013b\u0003\u0002\u0002\u0002",
    "]\u016b\u0003\u0002\u0002\u0002_\u016d\u0003\u0002\u0002\u0002a\u016f",
    "\u0003\u0002\u0002\u0002c\u017a\u0003\u0002\u0002\u0002e\u0185\u0003",
    "\u0002\u0002\u0002g\u0187\u0003\u0002\u0002\u0002i\u0192\u0003\u0002",
    "\u0002\u0002k\u01a2\u0003\u0002\u0002\u0002m\u01ac\u0003\u0002\u0002",
    "\u0002o\u01bc\u0003\u0002\u0002\u0002q\u01c0\u0003\u0002\u0002\u0002",
    "s\u01c7\u0003\u0002\u0002\u0002u\u01c9\u0003\u0002\u0002\u0002w\u01cb",
    "\u0003\u0002\u0002\u0002y\u01cd\u0003\u0002\u0002\u0002{\u01cf\u0003",
    "\u0002\u0002\u0002}\u01d1\u0003\u0002\u0002\u0002\u007f\u01d3\u0003",
    "\u0002\u0002\u0002\u0081\u01d5\u0003\u0002\u0002\u0002\u0083\u01d7\u0003",
    "\u0002\u0002\u0002\u0085\u01d9\u0003\u0002\u0002\u0002\u0087\u01db\u0003",
    "\u0002\u0002\u0002\u0089\u01dd\u0003\u0002\u0002\u0002\u008b\u01df\u0003",
    "\u0002\u0002\u0002\u008d\u01e1\u0003\u0002\u0002\u0002\u008f\u01e3\u0003",
    "\u0002\u0002\u0002\u0091\u01e5\u0003\u0002\u0002\u0002\u0093\u01e7\u0003",
    "\u0002\u0002\u0002\u0095\u01e9\u0003\u0002\u0002\u0002\u0097\u01eb\u0003",
    "\u0002\u0002\u0002\u0099\u01ed\u0003\u0002\u0002\u0002\u009b\u01ef\u0003",
    "\u0002\u0002\u0002\u009d\u01f1\u0003\u0002\u0002\u0002\u009f\u01f3\u0003",
    "\u0002\u0002\u0002\u00a1\u01f5\u0003\u0002\u0002\u0002\u00a3\u01f7\u0003",
    "\u0002\u0002\u0002\u00a5\u01f9\u0003\u0002\u0002\u0002\u00a7\u01fb\u0003",
    "\u0002\u0002\u0002\u00a9\u00aa\u0007<\u0002\u0002\u00aa\u0004\u0003",
    "\u0002\u0002\u0002\u00ab\u00ac\u0007A\u0002\u0002\u00ac\u0006\u0003",
    "\u0002\u0002\u0002\u00ad\u00ae\u0007(\u0002\u0002\u00ae\u00af\u0007",
    "(\u0002\u0002\u00af\b\u0003\u0002\u0002\u0002\u00b0\u00b1\u0007?\u0002",
    "\u0002\u00b1\u00b2\u0007?\u0002\u0002\u00b2\n\u0003\u0002\u0002\u0002",
    "\u00b3\u00b4\u0007@\u0002\u0002\u00b4\u00b5\u0007?\u0002\u0002\u00b5",
    "\f\u0003\u0002\u0002\u0002\u00b6\u00b7\u0007>\u0002\u0002\u00b7\u00b8",
    "\u0007?\u0002\u0002\u00b8\u000e\u0003\u0002\u0002\u0002\u00b9\u00ba",
    "\u0007#\u0002\u0002\u00ba\u00bb\u0007?\u0002\u0002\u00bb\u0010\u0003",
    "\u0002\u0002\u0002\u00bc\u00bd\u0007>\u0002\u0002\u00bd\u00be\u0007",
    "@\u0002\u0002\u00be\u0012\u0003\u0002\u0002\u0002\u00bf\u00c0\u0007",
    "~\u0002\u0002\u00c0\u00c1\u0007~\u0002\u0002\u00c1\u0014\u0003\u0002",
    "\u0002\u0002\u00c2\u00c3\u0007>\u0002\u0002\u00c3\u00c4\u0007>\u0002",
    "\u0002\u00c4\u0016\u0003\u0002\u0002\u0002\u00c5\u00c6\u0007@\u0002",
    "\u0002\u00c6\u00c7\u0007@\u0002\u0002\u00c7\u0018\u0003\u0002\u0002",
    "\u0002\u00c8\u00c9\u0007(\u0002\u0002\u00c9\u001a\u0003\u0002\u0002",
    "\u0002\u00ca\u00cb\u0007?\u0002\u0002\u00cb\u001c\u0003\u0002\u0002",
    "\u0002\u00cc\u00cd\u0007+\u0002\u0002\u00cd\u001e\u0003\u0002\u0002",
    "\u0002\u00ce\u00cf\u0007.\u0002\u0002\u00cf \u0003\u0002\u0002\u0002",
    "\u00d0\u00d1\u00070\u0002\u0002\u00d1\"\u0003\u0002\u0002\u0002\u00d2",
    "\u00d3\u00071\u0002\u0002\u00d3$\u0003\u0002\u0002\u0002\u00d4\u00d5",
    "\u0007@\u0002\u0002\u00d5&\u0003\u0002\u0002\u0002\u00d6\u00d7\u0007",
    ">\u0002\u0002\u00d7(\u0003\u0002\u0002\u0002\u00d8\u00d9\u0007/\u0002",
    "\u0002\u00d9*\u0003\u0002\u0002\u0002\u00da\u00db\u0007\'\u0002\u0002",
    "\u00db,\u0003\u0002\u0002\u0002\u00dc\u00dd\u0007*\u0002\u0002\u00dd",
    ".\u0003\u0002\u0002\u0002\u00de\u00df\u0007~\u0002\u0002\u00df0\u0003",
    "\u0002\u0002\u0002\u00e0\u00e1\u0007-\u0002\u0002\u00e12\u0003\u0002",
    "\u0002\u0002\u00e2\u00e3\u0007=\u0002\u0002\u00e34\u0003\u0002\u0002",
    "\u0002\u00e4\u00e5\u0007,\u0002\u0002\u00e56\u0003\u0002\u0002\u0002",
    "\u00e6\u00e7\u0007\u0080\u0002\u0002\u00e78\u0003\u0002\u0002\u0002",
    "\u00e8\u00e9\u0007a\u0002\u0002\u00e9:\u0003\u0002\u0002\u0002\u00ea",
    "\u00eb\u0005u;\u0002\u00eb\u00ec\u0005\u008fH\u0002\u00ec\u00ed\u0005",
    "{>\u0002\u00ed<\u0003\u0002\u0002\u0002\u00ee\u00ef\u0005u;\u0002\u00ef",
    "\u00f0\u0005\u0099M\u0002\u00f0\u00f1\u0005y=\u0002\u00f1>\u0003\u0002",
    "\u0002\u0002\u00f2\u00f3\u0005w<\u0002\u00f3\u00f4\u0005\u00a5S\u0002",
    "\u00f4@\u0003\u0002\u0002\u0002\u00f5\u00f6\u0005{>\u0002\u00f6\u00f7",
    "\u0005}?\u0002\u00f7\u00f8\u0005\u0099M\u0002\u00f8\u00f9\u0005y=\u0002",
    "\u00f9B\u0003\u0002\u0002\u0002\u00fa\u00fb\u0005\u007f@\u0002\u00fb",
    "\u00fc\u0005u;\u0002\u00fc\u00fd\u0005\u008bF\u0002\u00fd\u00fe\u0005",
    "\u0099M\u0002\u00fe\u00ff\u0005}?\u0002\u00ffD\u0003\u0002\u0002\u0002",
    "\u0100\u0101\u0005\u0085C\u0002\u0101\u0102\u0005\u0099M\u0002\u0102",
    "F\u0003\u0002\u0002\u0002\u0103\u0104\u0005\u0085C\u0002\u0104\u0105",
    "\u0005\u0099M\u0002\u0105\u0106\u0005\u008fH\u0002\u0106\u0107\u0005",
    "\u009dO\u0002\u0107\u0108\u0005\u008bF\u0002\u0108\u0109\u0005\u008b",
    "F\u0002\u0109H\u0003\u0002\u0002\u0002\u010a\u010b\u0005\u008bF\u0002",
    "\u010b\u010c\u0005\u0085C\u0002\u010c\u010d\u0005\u0089E\u0002\u010d",
    "\u010e\u0005}?\u0002\u010eJ\u0003\u0002\u0002\u0002\u010f\u0110\u0005",
    "\u008bF\u0002\u0110\u0111\u0005\u0085C\u0002\u0111\u0112\u0005\u008d",
    "G\u0002\u0112\u0113\u0005\u0085C\u0002\u0113\u0114\u0005\u009bN\u0002",
    "\u0114L\u0003\u0002\u0002\u0002\u0115\u0116\u0005\u008fH\u0002\u0116",
    "\u0117\u0005\u0091I\u0002\u0117\u0118\u0005\u009bN\u0002\u0118N\u0003",
    "\u0002\u0002\u0002\u0119\u011a\u0005\u008fH\u0002\u011a\u011b\u0005",
    "\u0091I\u0002\u011b\u011c\u0005\u009bN\u0002\u011c\u011d\u0005\u008f",
    "H\u0002\u011d\u011e\u0005\u009dO\u0002\u011e\u011f\u0005\u008bF\u0002",
    "\u011f\u0120\u0005\u008bF\u0002\u0120P\u0003\u0002\u0002\u0002\u0121",
    "\u0122\u0005\u008fH\u0002\u0122\u0123\u0005\u009dO\u0002\u0123\u0124",
    "\u0005\u008bF\u0002\u0124\u0125\u0005\u008bF\u0002\u0125R\u0003\u0002",
    "\u0002\u0002\u0126\u0127\u0005\u0091I\u0002\u0127\u0128\u0005\u0097",
    "L\u0002\u0128T\u0003\u0002\u0002\u0002\u0129\u012a\u0005\u0091I\u0002",
    "\u012a\u012b\u0005\u0097L\u0002\u012b\u012c\u0005{>\u0002\u012c\u012d",
    "\u0005}?\u0002\u012d\u012e\u0005\u0097L\u0002\u012eV\u0003\u0002\u0002",
    "\u0002\u012f\u0130\u0005\u0099M\u0002\u0130\u0131\u0005}?\u0002\u0131",
    "\u0132\u0005\u008bF\u0002\u0132\u0133\u0005}?\u0002\u0133\u0134\u0005",
    "y=\u0002\u0134\u0135\u0005\u009bN\u0002\u0135X\u0003\u0002\u0002\u0002",
    "\u0136\u0137\u0005\u009bN\u0002\u0137\u0138\u0005\u0097L\u0002\u0138",
    "\u0139\u0005\u009dO\u0002\u0139\u013a\u0005}?\u0002\u013aZ\u0003\u0002",
    "\u0002\u0002\u013b\u013c\u0005\u00a1Q\u0002\u013c\u013d\u0005\u0083",
    "B\u0002\u013d\u013e\u0005}?\u0002\u013e\u013f\u0005\u0097L\u0002\u013f",
    "\u0140\u0005}?\u0002\u0140\\\u0003\u0002\u0002\u0002\u0141\u0143\u0005",
    "s:\u0002\u0142\u0141\u0003\u0002\u0002\u0002\u0143\u0144\u0003\u0002",
    "\u0002\u0002\u0144\u0142\u0003\u0002\u0002\u0002\u0144\u0145\u0003\u0002",
    "\u0002\u0002\u0145\u014d\u0003\u0002\u0002\u0002\u0146\u014a\u00070",
    "\u0002\u0002\u0147\u0149\u0005s:\u0002\u0148\u0147\u0003\u0002\u0002",
    "\u0002\u0149\u014c\u0003\u0002\u0002\u0002\u014a\u0148\u0003\u0002\u0002",
    "\u0002\u014a\u014b\u0003\u0002\u0002\u0002\u014b\u014e\u0003\u0002\u0002",
    "\u0002\u014c\u014a\u0003\u0002\u0002\u0002\u014d\u0146\u0003\u0002\u0002",
    "\u0002\u014d\u014e\u0003\u0002\u0002\u0002\u014e\u0158\u0003\u0002\u0002",
    "\u0002\u014f\u0151\u0005}?\u0002\u0150\u0152\t\u0002\u0002\u0002\u0151",
    "\u0150\u0003\u0002\u0002\u0002\u0151\u0152\u0003\u0002\u0002\u0002\u0152",
    "\u0154\u0003\u0002\u0002\u0002\u0153\u0155\u0005s:\u0002\u0154\u0153",
    "\u0003\u0002\u0002\u0002\u0155\u0156\u0003\u0002\u0002\u0002\u0156\u0154",
    "\u0003\u0002\u0002\u0002\u0156\u0157\u0003\u0002\u0002\u0002\u0157\u0159",
    "\u0003\u0002\u0002\u0002\u0158\u014f\u0003\u0002\u0002\u0002\u0158\u0159",
    "\u0003\u0002\u0002\u0002\u0159\u016c\u0003\u0002\u0002\u0002\u015a\u015c",
    "\u00070\u0002\u0002\u015b\u015d\u0005s:\u0002\u015c\u015b\u0003\u0002",
    "\u0002\u0002\u015d\u015e\u0003\u0002\u0002\u0002\u015e\u015c\u0003\u0002",
    "\u0002\u0002\u015e\u015f\u0003\u0002\u0002\u0002\u015f\u0169\u0003\u0002",
    "\u0002\u0002\u0160\u0162\u0005}?\u0002\u0161\u0163\t\u0002\u0002\u0002",
    "\u0162\u0161\u0003\u0002\u0002\u0002\u0162\u0163\u0003\u0002\u0002\u0002",
    "\u0163\u0165\u0003\u0002\u0002\u0002\u0164\u0166\u0005s:\u0002\u0165",
    "\u0164\u0003\u0002\u0002\u0002\u0166\u0167\u0003\u0002\u0002\u0002\u0167",
    "\u0165\u0003\u0002\u0002\u0002\u0167\u0168\u0003\u0002\u0002\u0002\u0168",
    "\u016a\u0003\u0002\u0002\u0002\u0169\u0160\u0003\u0002\u0002\u0002\u0169",
    "\u016a\u0003\u0002\u0002\u0002\u016a\u016c\u0003\u0002\u0002\u0002\u016b",
    "\u0142\u0003\u0002\u0002\u0002\u016b\u015a\u0003\u0002\u0002\u0002\u016c",
    "^\u0003\u0002\u0002\u0002\u016d\u016e\u0005a1\u0002\u016e`\u0003\u0002",
    "\u0002\u0002\u016f\u0175\u0007$\u0002\u0002\u0170\u0171\u0007^\u0002",
    "\u0002\u0171\u0174\u0007$\u0002\u0002\u0172\u0174\n\u0003\u0002\u0002",
    "\u0173\u0170\u0003\u0002\u0002\u0002\u0173\u0172\u0003\u0002\u0002\u0002",
    "\u0174\u0177\u0003\u0002\u0002\u0002\u0175\u0173\u0003\u0002\u0002\u0002",
    "\u0175\u0176\u0003\u0002\u0002\u0002\u0176\u0178\u0003\u0002\u0002\u0002",
    "\u0177\u0175\u0003\u0002\u0002\u0002\u0178\u0179\u0007$\u0002\u0002",
    "\u0179b\u0003\u0002\u0002\u0002\u017a\u0180\u0007$\u0002\u0002\u017b",
    "\u017c\u0007$\u0002\u0002\u017c\u017f\u0007$\u0002\u0002\u017d\u017f",
    "\n\u0003\u0002\u0002\u017e\u017b\u0003\u0002\u0002\u0002\u017e\u017d",
    "\u0003\u0002\u0002\u0002\u017f\u0182\u0003\u0002\u0002\u0002\u0180\u017e",
    "\u0003\u0002\u0002\u0002\u0180\u0181\u0003\u0002\u0002\u0002\u0181\u0183",
    "\u0003\u0002\u0002\u0002\u0182\u0180\u0003\u0002\u0002\u0002\u0183\u0184",
    "\u0007$\u0002\u0002\u0184d\u0003\u0002\u0002\u0002\u0185\u0186\u0005",
    "g4\u0002\u0186f\u0003\u0002\u0002\u0002\u0187\u018d\u0007)\u0002\u0002",
    "\u0188\u0189\u0007^\u0002\u0002\u0189\u018c\u0007)\u0002\u0002\u018a",
    "\u018c\n\u0004\u0002\u0002\u018b\u0188\u0003\u0002\u0002\u0002\u018b",
    "\u018a\u0003\u0002\u0002\u0002\u018c\u018f\u0003\u0002\u0002\u0002\u018d",
    "\u018b\u0003\u0002\u0002\u0002\u018d\u018e\u0003\u0002\u0002\u0002\u018e",
    "\u0190\u0003\u0002\u0002\u0002\u018f\u018d\u0003\u0002\u0002\u0002\u0190",
    "\u0191\u0007)\u0002\u0002\u0191h\u0003\u0002\u0002\u0002\u0192\u0198",
    "\u0007)\u0002\u0002\u0193\u0194\u0007)\u0002\u0002\u0194\u0197\u0007",
    ")\u0002\u0002\u0195\u0197\n\u0004\u0002\u0002\u0196\u0193\u0003\u0002",
    "\u0002\u0002\u0196\u0195\u0003\u0002\u0002\u0002\u0197\u019a\u0003\u0002",
    "\u0002\u0002\u0198\u0196\u0003\u0002\u0002\u0002\u0198\u0199\u0003\u0002",
    "\u0002\u0002\u0199\u019b\u0003\u0002\u0002\u0002\u019a\u0198\u0003\u0002",
    "\u0002\u0002\u019b\u019c\u0007)\u0002\u0002\u019cj\u0003\u0002\u0002",
    "\u0002\u019d\u019e\u0007/\u0002\u0002\u019e\u01a3\u0007/\u0002\u0002",
    "\u019f\u01a0\u00071\u0002\u0002\u01a0\u01a3\u00071\u0002\u0002\u01a1",
    "\u01a3\u0007%\u0002\u0002\u01a2\u019d\u0003\u0002\u0002\u0002\u01a2",
    "\u019f\u0003\u0002\u0002\u0002\u01a2\u01a1\u0003\u0002\u0002\u0002\u01a3",
    "\u01a7\u0003\u0002\u0002\u0002\u01a4\u01a6\n\u0005\u0002\u0002\u01a5",
    "\u01a4\u0003\u0002\u0002\u0002\u01a6\u01a9\u0003\u0002\u0002\u0002\u01a7",
    "\u01a5\u0003\u0002\u0002\u0002\u01a7\u01a8\u0003\u0002\u0002\u0002\u01a8",
    "\u01aa\u0003\u0002\u0002\u0002\u01a9\u01a7\u0003\u0002\u0002\u0002\u01aa",
    "\u01ab\b6\u0002\u0002\u01abl\u0003\u0002\u0002\u0002\u01ac\u01ad\u0007",
    "1\u0002\u0002\u01ad\u01ae\u0007,\u0002\u0002\u01ae\u01b2\u0003\u0002",
    "\u0002\u0002\u01af\u01b1\u000b\u0002\u0002\u0002\u01b0\u01af\u0003\u0002",
    "\u0002\u0002\u01b1\u01b4\u0003\u0002\u0002\u0002\u01b2\u01b3\u0003\u0002",
    "\u0002\u0002\u01b2\u01b0\u0003\u0002\u0002\u0002\u01b3\u01b8\u0003\u0002",
    "\u0002\u0002\u01b4\u01b2\u0003\u0002\u0002\u0002\u01b5\u01b6\u0007,",
    "\u0002\u0002\u01b6\u01b9\u00071\u0002\u0002\u01b7\u01b9\u0007\u0002",
    "\u0002\u0003\u01b8\u01b5\u0003\u0002\u0002\u0002\u01b8\u01b7\u0003\u0002",
    "\u0002\u0002\u01b9\u01ba\u0003\u0002\u0002\u0002\u01ba\u01bb\b7\u0002",
    "\u0002\u01bbn\u0003\u0002\u0002\u0002\u01bc\u01bd\t\u0006\u0002\u0002",
    "\u01bd\u01be\u0003\u0002\u0002\u0002\u01be\u01bf\b8\u0002\u0002\u01bf",
    "p\u0003\u0002\u0002\u0002\u01c0\u01c4\t\u0007\u0002\u0002\u01c1\u01c3",
    "\t\b\u0002\u0002\u01c2\u01c1\u0003\u0002\u0002\u0002\u01c3\u01c6\u0003",
    "\u0002\u0002\u0002\u01c4\u01c2\u0003\u0002\u0002\u0002\u01c4\u01c5\u0003",
    "\u0002\u0002\u0002\u01c5r\u0003\u0002\u0002\u0002\u01c6\u01c4\u0003",
    "\u0002\u0002\u0002\u01c7\u01c8\t\t\u0002\u0002\u01c8t\u0003\u0002\u0002",
    "\u0002\u01c9\u01ca\t\n\u0002\u0002\u01cav\u0003\u0002\u0002\u0002\u01cb",
    "\u01cc\t\u000b\u0002\u0002\u01ccx\u0003\u0002\u0002\u0002\u01cd\u01ce",
    "\t\f\u0002\u0002\u01cez\u0003\u0002\u0002\u0002\u01cf\u01d0\t\r\u0002",
    "\u0002\u01d0|\u0003\u0002\u0002\u0002\u01d1\u01d2\t\u000e\u0002\u0002",
    "\u01d2~\u0003\u0002\u0002\u0002\u01d3\u01d4\t\u000f\u0002\u0002\u01d4",
    "\u0080\u0003\u0002\u0002\u0002\u01d5\u01d6\t\u0010\u0002\u0002\u01d6",
    "\u0082\u0003\u0002\u0002\u0002\u01d7\u01d8\t\u0011\u0002\u0002\u01d8",
    "\u0084\u0003\u0002\u0002\u0002\u01d9\u01da\t\u0012\u0002\u0002\u01da",
    "\u0086\u0003\u0002\u0002\u0002\u01db\u01dc\t\u0013\u0002\u0002\u01dc",
    "\u0088\u0003\u0002\u0002\u0002\u01dd\u01de\t\u0014\u0002\u0002\u01de",
    "\u008a\u0003\u0002\u0002\u0002\u01df\u01e0\t\u0015\u0002\u0002\u01e0",
    "\u008c\u0003\u0002\u0002\u0002\u01e1\u01e2\t\u0016\u0002\u0002\u01e2",
    "\u008e\u0003\u0002\u0002\u0002\u01e3\u01e4\t\u0017\u0002\u0002\u01e4",
    "\u0090\u0003\u0002\u0002\u0002\u01e5\u01e6\t\u0018\u0002\u0002\u01e6",
    "\u0092\u0003\u0002\u0002\u0002\u01e7\u01e8\t\u0019\u0002\u0002\u01e8",
    "\u0094\u0003\u0002\u0002\u0002\u01e9\u01ea\t\u001a\u0002\u0002\u01ea",
    "\u0096\u0003\u0002\u0002\u0002\u01eb\u01ec\t\u001b\u0002\u0002\u01ec",
    "\u0098\u0003\u0002\u0002\u0002\u01ed\u01ee\t\u001c\u0002\u0002\u01ee",
    "\u009a\u0003\u0002\u0002\u0002\u01ef\u01f0\t\u001d\u0002\u0002\u01f0",
    "\u009c\u0003\u0002\u0002\u0002\u01f1\u01f2\t\u001e\u0002\u0002\u01f2",
    "\u009e\u0003\u0002\u0002\u0002\u01f3\u01f4\t\u001f\u0002\u0002\u01f4",
    "\u00a0\u0003\u0002\u0002\u0002\u01f5\u01f6\t \u0002\u0002\u01f6\u00a2",
    "\u0003\u0002\u0002\u0002\u01f7\u01f8\t!\u0002\u0002\u01f8\u00a4\u0003",
    "\u0002\u0002\u0002\u01f9\u01fa\t\"\u0002\u0002\u01fa\u00a6\u0003\u0002",
    "\u0002\u0002\u01fb\u01fc\t#\u0002\u0002\u01fc\u00a8\u0003\u0002\u0002",
    "\u0002\u001b\u0002\u0144\u014a\u014d\u0151\u0156\u0158\u015e\u0162\u0167",
    "\u0169\u016b\u0173\u0175\u017e\u0180\u018b\u018d\u0196\u0198\u01a2\u01a7",
    "\u01b2\u01b8\u01c4\u0003\u0002\u0003\u0002"].join("");


var atn = new antlr4.atn.ATNDeserializer().deserialize(serializedATN);

var decisionsToDFA = atn.decisionToState.map( function(ds, index) { return new antlr4.dfa.DFA(ds, index); });

function PqlLexer(input) {
	antlr4.Lexer.call(this, input);
    this._interp = new antlr4.atn.LexerATNSimulator(this, atn, decisionsToDFA, new antlr4.PredictionContextCache());
    return this;
}

PqlLexer.prototype = Object.create(antlr4.Lexer.prototype);
PqlLexer.prototype.constructor = PqlLexer;

Object.defineProperty(PqlLexer.prototype, "atn", {
        get : function() {
                return atn;
        }
});

PqlLexer.EOF = antlr4.Token.EOF;
PqlLexer.TAXON_TAG_DELIMITER = 1;
PqlLexer.TAXON_OPTIONAL_OPERATOR = 2;
PqlLexer.AND = 3;
PqlLexer.EQ = 4;
PqlLexer.GT_EQ = 5;
PqlLexer.LT_EQ = 6;
PqlLexer.NOT_EQ1 = 7;
PqlLexer.NOT_EQ2 = 8;
PqlLexer.OR = 9;
PqlLexer.SHIFT_LEFT = 10;
PqlLexer.SHIFT_RIGHT = 11;
PqlLexer.AMP = 12;
PqlLexer.ASSIGN = 13;
PqlLexer.CLOSE_PAREN = 14;
PqlLexer.COMMA = 15;
PqlLexer.DOT = 16;
PqlLexer.FORWARD_SLASH = 17;
PqlLexer.GT = 18;
PqlLexer.LT = 19;
PqlLexer.MINUS = 20;
PqlLexer.MOD = 21;
PqlLexer.OPEN_PAREN = 22;
PqlLexer.PIPE = 23;
PqlLexer.PLUS = 24;
PqlLexer.SCOL = 25;
PqlLexer.STAR = 26;
PqlLexer.TILDE = 27;
PqlLexer.UNDER = 28;
PqlLexer.K_AND = 29;
PqlLexer.K_ASC = 30;
PqlLexer.K_BY = 31;
PqlLexer.K_DESC = 32;
PqlLexer.K_FALSE = 33;
PqlLexer.K_IS = 34;
PqlLexer.K_ISNULL = 35;
PqlLexer.K_LIKE = 36;
PqlLexer.K_LIMIT = 37;
PqlLexer.K_NOT = 38;
PqlLexer.K_NOTNULL = 39;
PqlLexer.K_NULL = 40;
PqlLexer.K_OR = 41;
PqlLexer.K_ORDER = 42;
PqlLexer.K_SELECT = 43;
PqlLexer.K_TRUE = 44;
PqlLexer.K_WHERE = 45;
PqlLexer.NUMERIC_LITERAL = 46;
PqlLexer.DOUBLE_QUOTED_STRING = 47;
PqlLexer.DOUBLE_QUOTED_STRING_TEL = 48;
PqlLexer.DOUBLE_QUOTED_STRING_SQL = 49;
PqlLexer.SINGLE_QUOTED_STRING = 50;
PqlLexer.SINGLE_QUOTED_STRING_TEL = 51;
PqlLexer.SINGLE_QUOTED_STRING_SQL = 52;
PqlLexer.SINGLE_LINE_COMMENT = 53;
PqlLexer.MULTILINE_COMMENT = 54;
PqlLexer.SPACES = 55;
PqlLexer.WORD = 56;

PqlLexer.prototype.channelNames = [ "DEFAULT_TOKEN_CHANNEL", "HIDDEN" ];

PqlLexer.prototype.modeNames = [ "DEFAULT_MODE" ];

PqlLexer.prototype.literalNames = [ null, "':'", "'?'", "'&&'", "'=='", 
                                    "'>='", "'<='", "'!='", "'<>'", "'||'", 
                                    "'<<'", "'>>'", "'&'", "'='", "')'", 
                                    "','", "'.'", "'/'", "'>'", "'<'", "'-'", 
                                    "'%'", "'('", "'|'", "'+'", "';'", "'*'", 
                                    "'~'", "'_'" ];

PqlLexer.prototype.symbolicNames = [ null, "TAXON_TAG_DELIMITER", "TAXON_OPTIONAL_OPERATOR", 
                                     "AND", "EQ", "GT_EQ", "LT_EQ", "NOT_EQ1", 
                                     "NOT_EQ2", "OR", "SHIFT_LEFT", "SHIFT_RIGHT", 
                                     "AMP", "ASSIGN", "CLOSE_PAREN", "COMMA", 
                                     "DOT", "FORWARD_SLASH", "GT", "LT", 
                                     "MINUS", "MOD", "OPEN_PAREN", "PIPE", 
                                     "PLUS", "SCOL", "STAR", "TILDE", "UNDER", 
                                     "K_AND", "K_ASC", "K_BY", "K_DESC", 
                                     "K_FALSE", "K_IS", "K_ISNULL", "K_LIKE", 
                                     "K_LIMIT", "K_NOT", "K_NOTNULL", "K_NULL", 
                                     "K_OR", "K_ORDER", "K_SELECT", "K_TRUE", 
                                     "K_WHERE", "NUMERIC_LITERAL", "DOUBLE_QUOTED_STRING", 
                                     "DOUBLE_QUOTED_STRING_TEL", "DOUBLE_QUOTED_STRING_SQL", 
                                     "SINGLE_QUOTED_STRING", "SINGLE_QUOTED_STRING_TEL", 
                                     "SINGLE_QUOTED_STRING_SQL", "SINGLE_LINE_COMMENT", 
                                     "MULTILINE_COMMENT", "SPACES", "WORD" ];

PqlLexer.prototype.ruleNames = [ "TAXON_TAG_DELIMITER", "TAXON_OPTIONAL_OPERATOR", 
                                 "AND", "EQ", "GT_EQ", "LT_EQ", "NOT_EQ1", 
                                 "NOT_EQ2", "OR", "SHIFT_LEFT", "SHIFT_RIGHT", 
                                 "AMP", "ASSIGN", "CLOSE_PAREN", "COMMA", 
                                 "DOT", "FORWARD_SLASH", "GT", "LT", "MINUS", 
                                 "MOD", "OPEN_PAREN", "PIPE", "PLUS", "SCOL", 
                                 "STAR", "TILDE", "UNDER", "K_AND", "K_ASC", 
                                 "K_BY", "K_DESC", "K_FALSE", "K_IS", "K_ISNULL", 
                                 "K_LIKE", "K_LIMIT", "K_NOT", "K_NOTNULL", 
                                 "K_NULL", "K_OR", "K_ORDER", "K_SELECT", 
                                 "K_TRUE", "K_WHERE", "NUMERIC_LITERAL", 
                                 "DOUBLE_QUOTED_STRING", "DOUBLE_QUOTED_STRING_TEL", 
                                 "DOUBLE_QUOTED_STRING_SQL", "SINGLE_QUOTED_STRING", 
                                 "SINGLE_QUOTED_STRING_TEL", "SINGLE_QUOTED_STRING_SQL", 
                                 "SINGLE_LINE_COMMENT", "MULTILINE_COMMENT", 
                                 "SPACES", "WORD", "DIGIT", "A", "B", "C", 
                                 "D", "E", "F", "G", "H", "I", "J", "K", 
                                 "L", "M", "N", "O", "P", "Q", "R", "S", 
                                 "T", "U", "V", "W", "X", "Y", "Z" ];

PqlLexer.prototype.grammarFileName = "PqlLexer.g4";


exports.PqlLexer = PqlLexer;


// Generated from grammar/PqlLexer.g4 by ANTLR 4.8
// jshint ignore: start
var antlr4 = require('antlr4/index');



var serializedATN = ["\u0003\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964",
    "\u00026\u01e1\b\u0001\u0004\u0002\t\u0002\u0004\u0003\t\u0003\u0004",
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
    "M\tM\u0004N\tN\u0004O\tO\u0004P\tP\u0003\u0002\u0003\u0002\u0003\u0002",
    "\u0003\u0003\u0003\u0003\u0003\u0003\u0003\u0004\u0003\u0004\u0003\u0004",
    "\u0003\u0005\u0003\u0005\u0003\u0005\u0003\u0006\u0003\u0006\u0003\u0006",
    "\u0003\u0007\u0003\u0007\u0003\u0007\u0003\b\u0003\b\u0003\b\u0003\t",
    "\u0003\t\u0003\t\u0003\n\u0003\n\u0003\n\u0003\u000b\u0003\u000b\u0003",
    "\f\u0003\f\u0003\r\u0003\r\u0003\u000e\u0003\u000e\u0003\u000f\u0003",
    "\u000f\u0003\u0010\u0003\u0010\u0003\u0011\u0003\u0011\u0003\u0012\u0003",
    "\u0012\u0003\u0013\u0003\u0013\u0003\u0014\u0003\u0014\u0003\u0015\u0003",
    "\u0015\u0003\u0016\u0003\u0016\u0003\u0017\u0003\u0017\u0003\u0018\u0003",
    "\u0018\u0003\u0019\u0003\u0019\u0003\u001a\u0003\u001a\u0003\u001b\u0003",
    "\u001b\u0003\u001c\u0003\u001c\u0003\u001d\u0003\u001d\u0003\u001e\u0003",
    "\u001e\u0003\u001e\u0003\u001e\u0003\u001f\u0003\u001f\u0003\u001f\u0003",
    "\u001f\u0003\u001f\u0003\u001f\u0003\u001f\u0003\u001f\u0003 \u0003",
    " \u0003 \u0003 \u0003 \u0003 \u0003!\u0003!\u0003!\u0003!\u0003!\u0003",
    "!\u0003\"\u0003\"\u0003\"\u0003#\u0003#\u0003#\u0003$\u0003$\u0003$",
    "\u0003$\u0003$\u0003$\u0003$\u0003%\u0003%\u0003%\u0003%\u0003%\u0003",
    "&\u0003&\u0003&\u0003&\u0003\'\u0003\'\u0003\'\u0003\'\u0003\'\u0003",
    "\'\u0003\'\u0003\'\u0003(\u0003(\u0003(\u0003(\u0003(\u0003)\u0003)",
    "\u0003)\u0003*\u0003*\u0003*\u0003*\u0003*\u0003+\u0006+\u0127\n+\r",
    "+\u000e+\u0128\u0003+\u0003+\u0007+\u012d\n+\f+\u000e+\u0130\u000b+",
    "\u0005+\u0132\n+\u0003+\u0003+\u0005+\u0136\n+\u0003+\u0006+\u0139\n",
    "+\r+\u000e+\u013a\u0005+\u013d\n+\u0003+\u0003+\u0006+\u0141\n+\r+\u000e",
    "+\u0142\u0003+\u0003+\u0005+\u0147\n+\u0003+\u0006+\u014a\n+\r+\u000e",
    "+\u014b\u0005+\u014e\n+\u0005+\u0150\n+\u0003,\u0003,\u0003-\u0003-",
    "\u0003-\u0003-\u0007-\u0158\n-\f-\u000e-\u015b\u000b-\u0003-\u0003-",
    "\u0003.\u0003.\u0003.\u0003.\u0007.\u0163\n.\f.\u000e.\u0166\u000b.",
    "\u0003.\u0003.\u0003/\u0003/\u00030\u00030\u00030\u00030\u00070\u0170",
    "\n0\f0\u000e0\u0173\u000b0\u00030\u00030\u00031\u00031\u00031\u0003",
    "1\u00071\u017b\n1\f1\u000e1\u017e\u000b1\u00031\u00031\u00032\u0003",
    "2\u00032\u00032\u00032\u00052\u0187\n2\u00032\u00072\u018a\n2\f2\u000e",
    "2\u018d\u000b2\u00032\u00032\u00033\u00033\u00033\u00033\u00073\u0195",
    "\n3\f3\u000e3\u0198\u000b3\u00033\u00033\u00033\u00053\u019d\n3\u0003",
    "3\u00033\u00034\u00034\u00034\u00034\u00035\u00035\u00075\u01a7\n5\f",
    "5\u000e5\u01aa\u000b5\u00036\u00036\u00037\u00037\u00038\u00038\u0003",
    "9\u00039\u0003:\u0003:\u0003;\u0003;\u0003<\u0003<\u0003=\u0003=\u0003",
    ">\u0003>\u0003?\u0003?\u0003@\u0003@\u0003A\u0003A\u0003B\u0003B\u0003",
    "C\u0003C\u0003D\u0003D\u0003E\u0003E\u0003F\u0003F\u0003G\u0003G\u0003",
    "H\u0003H\u0003I\u0003I\u0003J\u0003J\u0003K\u0003K\u0003L\u0003L\u0003",
    "M\u0003M\u0003N\u0003N\u0003O\u0003O\u0003P\u0003P\u0003\u0196\u0002",
    "Q\u0003\u0003\u0005\u0004\u0007\u0005\t\u0006\u000b\u0007\r\b\u000f",
    "\t\u0011\n\u0013\u000b\u0015\f\u0017\r\u0019\u000e\u001b\u000f\u001d",
    "\u0010\u001f\u0011!\u0012#\u0013%\u0014\'\u0015)\u0016+\u0017-\u0018",
    "/\u00191\u001a3\u001b5\u001c7\u001d9\u001e;\u001f= ?!A\"C#E$G%I&K\'",
    "M(O)Q*S+U,W-Y.[/]0_1a2c3e4g5i6k\u0002m\u0002o\u0002q\u0002s\u0002u\u0002",
    "w\u0002y\u0002{\u0002}\u0002\u007f\u0002\u0081\u0002\u0083\u0002\u0085",
    "\u0002\u0087\u0002\u0089\u0002\u008b\u0002\u008d\u0002\u008f\u0002\u0091",
    "\u0002\u0093\u0002\u0095\u0002\u0097\u0002\u0099\u0002\u009b\u0002\u009d",
    "\u0002\u009f\u0002\u0003\u0002$\u0004\u0002--//\u0003\u0002$$\u0003",
    "\u0002))\u0004\u0002\f\f\u000f\u000f\u0005\u0002\u000b\r\u000f\u000f",
    "\"\"\u0005\u0002C\\aac|\u0006\u00022;C\\aac|\u0003\u00022;\u0004\u0002",
    "CCcc\u0004\u0002DDdd\u0004\u0002EEee\u0004\u0002FFff\u0004\u0002GGg",
    "g\u0004\u0002HHhh\u0004\u0002IIii\u0004\u0002JJjj\u0004\u0002KKkk\u0004",
    "\u0002LLll\u0004\u0002MMmm\u0004\u0002NNnn\u0004\u0002OOoo\u0004\u0002",
    "PPpp\u0004\u0002QQqq\u0004\u0002RRrr\u0004\u0002SSss\u0004\u0002TTt",
    "t\u0004\u0002UUuu\u0004\u0002VVvv\u0004\u0002WWww\u0004\u0002XXxx\u0004",
    "\u0002YYyy\u0004\u0002ZZzz\u0004\u0002[[{{\u0004\u0002\\\\||\u0002\u01de",
    "\u0002\u0003\u0003\u0002\u0002\u0002\u0002\u0005\u0003\u0002\u0002\u0002",
    "\u0002\u0007\u0003\u0002\u0002\u0002\u0002\t\u0003\u0002\u0002\u0002",
    "\u0002\u000b\u0003\u0002\u0002\u0002\u0002\r\u0003\u0002\u0002\u0002",
    "\u0002\u000f\u0003\u0002\u0002\u0002\u0002\u0011\u0003\u0002\u0002\u0002",
    "\u0002\u0013\u0003\u0002\u0002\u0002\u0002\u0015\u0003\u0002\u0002\u0002",
    "\u0002\u0017\u0003\u0002\u0002\u0002\u0002\u0019\u0003\u0002\u0002\u0002",
    "\u0002\u001b\u0003\u0002\u0002\u0002\u0002\u001d\u0003\u0002\u0002\u0002",
    "\u0002\u001f\u0003\u0002\u0002\u0002\u0002!\u0003\u0002\u0002\u0002",
    "\u0002#\u0003\u0002\u0002\u0002\u0002%\u0003\u0002\u0002\u0002\u0002",
    "\'\u0003\u0002\u0002\u0002\u0002)\u0003\u0002\u0002\u0002\u0002+\u0003",
    "\u0002\u0002\u0002\u0002-\u0003\u0002\u0002\u0002\u0002/\u0003\u0002",
    "\u0002\u0002\u00021\u0003\u0002\u0002\u0002\u00023\u0003\u0002\u0002",
    "\u0002\u00025\u0003\u0002\u0002\u0002\u00027\u0003\u0002\u0002\u0002",
    "\u00029\u0003\u0002\u0002\u0002\u0002;\u0003\u0002\u0002\u0002\u0002",
    "=\u0003\u0002\u0002\u0002\u0002?\u0003\u0002\u0002\u0002\u0002A\u0003",
    "\u0002\u0002\u0002\u0002C\u0003\u0002\u0002\u0002\u0002E\u0003\u0002",
    "\u0002\u0002\u0002G\u0003\u0002\u0002\u0002\u0002I\u0003\u0002\u0002",
    "\u0002\u0002K\u0003\u0002\u0002\u0002\u0002M\u0003\u0002\u0002\u0002",
    "\u0002O\u0003\u0002\u0002\u0002\u0002Q\u0003\u0002\u0002\u0002\u0002",
    "S\u0003\u0002\u0002\u0002\u0002U\u0003\u0002\u0002\u0002\u0002W\u0003",
    "\u0002\u0002\u0002\u0002Y\u0003\u0002\u0002\u0002\u0002[\u0003\u0002",
    "\u0002\u0002\u0002]\u0003\u0002\u0002\u0002\u0002_\u0003\u0002\u0002",
    "\u0002\u0002a\u0003\u0002\u0002\u0002\u0002c\u0003\u0002\u0002\u0002",
    "\u0002e\u0003\u0002\u0002\u0002\u0002g\u0003\u0002\u0002\u0002\u0002",
    "i\u0003\u0002\u0002\u0002\u0003\u00a1\u0003\u0002\u0002\u0002\u0005",
    "\u00a4\u0003\u0002\u0002\u0002\u0007\u00a7\u0003\u0002\u0002\u0002\t",
    "\u00aa\u0003\u0002\u0002\u0002\u000b\u00ad\u0003\u0002\u0002\u0002\r",
    "\u00b0\u0003\u0002\u0002\u0002\u000f\u00b3\u0003\u0002\u0002\u0002\u0011",
    "\u00b6\u0003\u0002\u0002\u0002\u0013\u00b9\u0003\u0002\u0002\u0002\u0015",
    "\u00bc\u0003\u0002\u0002\u0002\u0017\u00be\u0003\u0002\u0002\u0002\u0019",
    "\u00c0\u0003\u0002\u0002\u0002\u001b\u00c2\u0003\u0002\u0002\u0002\u001d",
    "\u00c4\u0003\u0002\u0002\u0002\u001f\u00c6\u0003\u0002\u0002\u0002!",
    "\u00c8\u0003\u0002\u0002\u0002#\u00ca\u0003\u0002\u0002\u0002%\u00cc",
    "\u0003\u0002\u0002\u0002\'\u00ce\u0003\u0002\u0002\u0002)\u00d0\u0003",
    "\u0002\u0002\u0002+\u00d2\u0003\u0002\u0002\u0002-\u00d4\u0003\u0002",
    "\u0002\u0002/\u00d6\u0003\u0002\u0002\u00021\u00d8\u0003\u0002\u0002",
    "\u00023\u00da\u0003\u0002\u0002\u00025\u00dc\u0003\u0002\u0002\u0002",
    "7\u00de\u0003\u0002\u0002\u00029\u00e0\u0003\u0002\u0002\u0002;\u00e2",
    "\u0003\u0002\u0002\u0002=\u00e6\u0003\u0002\u0002\u0002?\u00ee\u0003",
    "\u0002\u0002\u0002A\u00f4\u0003\u0002\u0002\u0002C\u00fa\u0003\u0002",
    "\u0002\u0002E\u00fd\u0003\u0002\u0002\u0002G\u0100\u0003\u0002\u0002",
    "\u0002I\u0107\u0003\u0002\u0002\u0002K\u010c\u0003\u0002\u0002\u0002",
    "M\u0110\u0003\u0002\u0002\u0002O\u0118\u0003\u0002\u0002\u0002Q\u011d",
    "\u0003\u0002\u0002\u0002S\u0120\u0003\u0002\u0002\u0002U\u014f\u0003",
    "\u0002\u0002\u0002W\u0151\u0003\u0002\u0002\u0002Y\u0153\u0003\u0002",
    "\u0002\u0002[\u015e\u0003\u0002\u0002\u0002]\u0169\u0003\u0002\u0002",
    "\u0002_\u016b\u0003\u0002\u0002\u0002a\u0176\u0003\u0002\u0002\u0002",
    "c\u0186\u0003\u0002\u0002\u0002e\u0190\u0003\u0002\u0002\u0002g\u01a0",
    "\u0003\u0002\u0002\u0002i\u01a4\u0003\u0002\u0002\u0002k\u01ab\u0003",
    "\u0002\u0002\u0002m\u01ad\u0003\u0002\u0002\u0002o\u01af\u0003\u0002",
    "\u0002\u0002q\u01b1\u0003\u0002\u0002\u0002s\u01b3\u0003\u0002\u0002",
    "\u0002u\u01b5\u0003\u0002\u0002\u0002w\u01b7\u0003\u0002\u0002\u0002",
    "y\u01b9\u0003\u0002\u0002\u0002{\u01bb\u0003\u0002\u0002\u0002}\u01bd",
    "\u0003\u0002\u0002\u0002\u007f\u01bf\u0003\u0002\u0002\u0002\u0081\u01c1",
    "\u0003\u0002\u0002\u0002\u0083\u01c3\u0003\u0002\u0002\u0002\u0085\u01c5",
    "\u0003\u0002\u0002\u0002\u0087\u01c7\u0003\u0002\u0002\u0002\u0089\u01c9",
    "\u0003\u0002\u0002\u0002\u008b\u01cb\u0003\u0002\u0002\u0002\u008d\u01cd",
    "\u0003\u0002\u0002\u0002\u008f\u01cf\u0003\u0002\u0002\u0002\u0091\u01d1",
    "\u0003\u0002\u0002\u0002\u0093\u01d3\u0003\u0002\u0002\u0002\u0095\u01d5",
    "\u0003\u0002\u0002\u0002\u0097\u01d7\u0003\u0002\u0002\u0002\u0099\u01d9",
    "\u0003\u0002\u0002\u0002\u009b\u01db\u0003\u0002\u0002\u0002\u009d\u01dd",
    "\u0003\u0002\u0002\u0002\u009f\u01df\u0003\u0002\u0002\u0002\u00a1\u00a2",
    "\u0007(\u0002\u0002\u00a2\u00a3\u0007(\u0002\u0002\u00a3\u0004\u0003",
    "\u0002\u0002\u0002\u00a4\u00a5\u0007?\u0002\u0002\u00a5\u00a6\u0007",
    "?\u0002\u0002\u00a6\u0006\u0003\u0002\u0002\u0002\u00a7\u00a8\u0007",
    "@\u0002\u0002\u00a8\u00a9\u0007?\u0002\u0002\u00a9\b\u0003\u0002\u0002",
    "\u0002\u00aa\u00ab\u0007>\u0002\u0002\u00ab\u00ac\u0007?\u0002\u0002",
    "\u00ac\n\u0003\u0002\u0002\u0002\u00ad\u00ae\u0007#\u0002\u0002\u00ae",
    "\u00af\u0007?\u0002\u0002\u00af\f\u0003\u0002\u0002\u0002\u00b0\u00b1",
    "\u0007>\u0002\u0002\u00b1\u00b2\u0007@\u0002\u0002\u00b2\u000e\u0003",
    "\u0002\u0002\u0002\u00b3\u00b4\u0007~\u0002\u0002\u00b4\u00b5\u0007",
    "~\u0002\u0002\u00b5\u0010\u0003\u0002\u0002\u0002\u00b6\u00b7\u0007",
    ">\u0002\u0002\u00b7\u00b8\u0007>\u0002\u0002\u00b8\u0012\u0003\u0002",
    "\u0002\u0002\u00b9\u00ba\u0007@\u0002\u0002\u00ba\u00bb\u0007@\u0002",
    "\u0002\u00bb\u0014\u0003\u0002\u0002\u0002\u00bc\u00bd\u0007(\u0002",
    "\u0002\u00bd\u0016\u0003\u0002\u0002\u0002\u00be\u00bf\u0007?\u0002",
    "\u0002\u00bf\u0018\u0003\u0002\u0002\u0002\u00c0\u00c1\u0007+\u0002",
    "\u0002\u00c1\u001a\u0003\u0002\u0002\u0002\u00c2\u00c3\u0007<\u0002",
    "\u0002\u00c3\u001c\u0003\u0002\u0002\u0002\u00c4\u00c5\u0007.\u0002",
    "\u0002\u00c5\u001e\u0003\u0002\u0002\u0002\u00c6\u00c7\u00070\u0002",
    "\u0002\u00c7 \u0003\u0002\u0002\u0002\u00c8\u00c9\u00071\u0002\u0002",
    "\u00c9\"\u0003\u0002\u0002\u0002\u00ca\u00cb\u0007@\u0002\u0002\u00cb",
    "$\u0003\u0002\u0002\u0002\u00cc\u00cd\u0007>\u0002\u0002\u00cd&\u0003",
    "\u0002\u0002\u0002\u00ce\u00cf\u0007/\u0002\u0002\u00cf(\u0003\u0002",
    "\u0002\u0002\u00d0\u00d1\u0007\'\u0002\u0002\u00d1*\u0003\u0002\u0002",
    "\u0002\u00d2\u00d3\u0007*\u0002\u0002\u00d3,\u0003\u0002\u0002\u0002",
    "\u00d4\u00d5\u0007~\u0002\u0002\u00d5.\u0003\u0002\u0002\u0002\u00d6",
    "\u00d7\u0007-\u0002\u0002\u00d70\u0003\u0002\u0002\u0002\u00d8\u00d9",
    "\u0007A\u0002\u0002\u00d92\u0003\u0002\u0002\u0002\u00da\u00db\u0007",
    "=\u0002\u0002\u00db4\u0003\u0002\u0002\u0002\u00dc\u00dd\u0007,\u0002",
    "\u0002\u00dd6\u0003\u0002\u0002\u0002\u00de\u00df\u0007\u0080\u0002",
    "\u0002\u00df8\u0003\u0002\u0002\u0002\u00e0\u00e1\u0007a\u0002\u0002",
    "\u00e1:\u0003\u0002\u0002\u0002\u00e2\u00e3\u0005m7\u0002\u00e3\u00e4",
    "\u0005\u0087D\u0002\u00e4\u00e5\u0005s:\u0002\u00e5<\u0003\u0002\u0002",
    "\u0002\u00e6\u00e7\u0005o8\u0002\u00e7\u00e8\u0005u;\u0002\u00e8\u00e9",
    "\u0005\u0093J\u0002\u00e9\u00ea\u0005\u0099M\u0002\u00ea\u00eb\u0005",
    "u;\u0002\u00eb\u00ec\u0005u;\u0002\u00ec\u00ed\u0005\u0087D\u0002\u00ed",
    ">\u0003\u0002\u0002\u0002\u00ee\u00ef\u0005w<\u0002\u00ef\u00f0\u0005",
    "m7\u0002\u00f0\u00f1\u0005\u0083B\u0002\u00f1\u00f2\u0005\u0091I\u0002",
    "\u00f2\u00f3\u0005u;\u0002\u00f3@\u0003\u0002\u0002\u0002\u00f4\u00f5",
    "\u0005}?\u0002\u00f5\u00f6\u0005\u0083B\u0002\u00f6\u00f7\u0005}?\u0002",
    "\u00f7\u00f8\u0005\u0081A\u0002\u00f8\u00f9\u0005u;\u0002\u00f9B\u0003",
    "\u0002\u0002\u0002\u00fa\u00fb\u0005}?\u0002\u00fb\u00fc\u0005\u0087",
    "D\u0002\u00fcD\u0003\u0002\u0002\u0002\u00fd\u00fe\u0005}?\u0002\u00fe",
    "\u00ff\u0005\u0091I\u0002\u00ffF\u0003\u0002\u0002\u0002\u0100\u0101",
    "\u0005}?\u0002\u0101\u0102\u0005\u0091I\u0002\u0102\u0103\u0005\u0087",
    "D\u0002\u0103\u0104\u0005\u0095K\u0002\u0104\u0105\u0005\u0083B\u0002",
    "\u0105\u0106\u0005\u0083B\u0002\u0106H\u0003\u0002\u0002\u0002\u0107",
    "\u0108\u0005\u0083B\u0002\u0108\u0109\u0005}?\u0002\u0109\u010a\u0005",
    "\u0081A\u0002\u010a\u010b\u0005u;\u0002\u010bJ\u0003\u0002\u0002\u0002",
    "\u010c\u010d\u0005\u0087D\u0002\u010d\u010e\u0005\u0089E\u0002\u010e",
    "\u010f\u0005\u0093J\u0002\u010fL\u0003\u0002\u0002\u0002\u0110\u0111",
    "\u0005\u0087D\u0002\u0111\u0112\u0005\u0089E\u0002\u0112\u0113\u0005",
    "\u0093J\u0002\u0113\u0114\u0005\u0087D\u0002\u0114\u0115\u0005\u0095",
    "K\u0002\u0115\u0116\u0005\u0083B\u0002\u0116\u0117\u0005\u0083B\u0002",
    "\u0117N\u0003\u0002\u0002\u0002\u0118\u0119\u0005\u0087D\u0002\u0119",
    "\u011a\u0005\u0095K\u0002\u011a\u011b\u0005\u0083B\u0002\u011b\u011c",
    "\u0005\u0083B\u0002\u011cP\u0003\u0002\u0002\u0002\u011d\u011e\u0005",
    "\u0089E\u0002\u011e\u011f\u0005\u008fH\u0002\u011fR\u0003\u0002\u0002",
    "\u0002\u0120\u0121\u0005\u0093J\u0002\u0121\u0122\u0005\u008fH\u0002",
    "\u0122\u0123\u0005\u0095K\u0002\u0123\u0124\u0005u;\u0002\u0124T\u0003",
    "\u0002\u0002\u0002\u0125\u0127\u0005k6\u0002\u0126\u0125\u0003\u0002",
    "\u0002\u0002\u0127\u0128\u0003\u0002\u0002\u0002\u0128\u0126\u0003\u0002",
    "\u0002\u0002\u0128\u0129\u0003\u0002\u0002\u0002\u0129\u0131\u0003\u0002",
    "\u0002\u0002\u012a\u012e\u00070\u0002\u0002\u012b\u012d\u0005k6\u0002",
    "\u012c\u012b\u0003\u0002\u0002\u0002\u012d\u0130\u0003\u0002\u0002\u0002",
    "\u012e\u012c\u0003\u0002\u0002\u0002\u012e\u012f\u0003\u0002\u0002\u0002",
    "\u012f\u0132\u0003\u0002\u0002\u0002\u0130\u012e\u0003\u0002\u0002\u0002",
    "\u0131\u012a\u0003\u0002\u0002\u0002\u0131\u0132\u0003\u0002\u0002\u0002",
    "\u0132\u013c\u0003\u0002\u0002\u0002\u0133\u0135\u0005u;\u0002\u0134",
    "\u0136\t\u0002\u0002\u0002\u0135\u0134\u0003\u0002\u0002\u0002\u0135",
    "\u0136\u0003\u0002\u0002\u0002\u0136\u0138\u0003\u0002\u0002\u0002\u0137",
    "\u0139\u0005k6\u0002\u0138\u0137\u0003\u0002\u0002\u0002\u0139\u013a",
    "\u0003\u0002\u0002\u0002\u013a\u0138\u0003\u0002\u0002\u0002\u013a\u013b",
    "\u0003\u0002\u0002\u0002\u013b\u013d\u0003\u0002\u0002\u0002\u013c\u0133",
    "\u0003\u0002\u0002\u0002\u013c\u013d\u0003\u0002\u0002\u0002\u013d\u0150",
    "\u0003\u0002\u0002\u0002\u013e\u0140\u00070\u0002\u0002\u013f\u0141",
    "\u0005k6\u0002\u0140\u013f\u0003\u0002\u0002\u0002\u0141\u0142\u0003",
    "\u0002\u0002\u0002\u0142\u0140\u0003\u0002\u0002\u0002\u0142\u0143\u0003",
    "\u0002\u0002\u0002\u0143\u014d\u0003\u0002\u0002\u0002\u0144\u0146\u0005",
    "u;\u0002\u0145\u0147\t\u0002\u0002\u0002\u0146\u0145\u0003\u0002\u0002",
    "\u0002\u0146\u0147\u0003\u0002\u0002\u0002\u0147\u0149\u0003\u0002\u0002",
    "\u0002\u0148\u014a\u0005k6\u0002\u0149\u0148\u0003\u0002\u0002\u0002",
    "\u014a\u014b\u0003\u0002\u0002\u0002\u014b\u0149\u0003\u0002\u0002\u0002",
    "\u014b\u014c\u0003\u0002\u0002\u0002\u014c\u014e\u0003\u0002\u0002\u0002",
    "\u014d\u0144\u0003\u0002\u0002\u0002\u014d\u014e\u0003\u0002\u0002\u0002",
    "\u014e\u0150\u0003\u0002\u0002\u0002\u014f\u0126\u0003\u0002\u0002\u0002",
    "\u014f\u013e\u0003\u0002\u0002\u0002\u0150V\u0003\u0002\u0002\u0002",
    "\u0151\u0152\u0005Y-\u0002\u0152X\u0003\u0002\u0002\u0002\u0153\u0159",
    "\u0007$\u0002\u0002\u0154\u0155\u0007^\u0002\u0002\u0155\u0158\u0007",
    "$\u0002\u0002\u0156\u0158\n\u0003\u0002\u0002\u0157\u0154\u0003\u0002",
    "\u0002\u0002\u0157\u0156\u0003\u0002\u0002\u0002\u0158\u015b\u0003\u0002",
    "\u0002\u0002\u0159\u0157\u0003\u0002\u0002\u0002\u0159\u015a\u0003\u0002",
    "\u0002\u0002\u015a\u015c\u0003\u0002\u0002\u0002\u015b\u0159\u0003\u0002",
    "\u0002\u0002\u015c\u015d\u0007$\u0002\u0002\u015dZ\u0003\u0002\u0002",
    "\u0002\u015e\u0164\u0007$\u0002\u0002\u015f\u0160\u0007$\u0002\u0002",
    "\u0160\u0163\u0007$\u0002\u0002\u0161\u0163\n\u0003\u0002\u0002\u0162",
    "\u015f\u0003\u0002\u0002\u0002\u0162\u0161\u0003\u0002\u0002\u0002\u0163",
    "\u0166\u0003\u0002\u0002\u0002\u0164\u0162\u0003\u0002\u0002\u0002\u0164",
    "\u0165\u0003\u0002\u0002\u0002\u0165\u0167\u0003\u0002\u0002\u0002\u0166",
    "\u0164\u0003\u0002\u0002\u0002\u0167\u0168\u0007$\u0002\u0002\u0168",
    "\\\u0003\u0002\u0002\u0002\u0169\u016a\u0005_0\u0002\u016a^\u0003\u0002",
    "\u0002\u0002\u016b\u0171\u0007)\u0002\u0002\u016c\u016d\u0007^\u0002",
    "\u0002\u016d\u0170\u0007)\u0002\u0002\u016e\u0170\n\u0004\u0002\u0002",
    "\u016f\u016c\u0003\u0002\u0002\u0002\u016f\u016e\u0003\u0002\u0002\u0002",
    "\u0170\u0173\u0003\u0002\u0002\u0002\u0171\u016f\u0003\u0002\u0002\u0002",
    "\u0171\u0172\u0003\u0002\u0002\u0002\u0172\u0174\u0003\u0002\u0002\u0002",
    "\u0173\u0171\u0003\u0002\u0002\u0002\u0174\u0175\u0007)\u0002\u0002",
    "\u0175`\u0003\u0002\u0002\u0002\u0176\u017c\u0007)\u0002\u0002\u0177",
    "\u0178\u0007)\u0002\u0002\u0178\u017b\u0007)\u0002\u0002\u0179\u017b",
    "\n\u0004\u0002\u0002\u017a\u0177\u0003\u0002\u0002\u0002\u017a\u0179",
    "\u0003\u0002\u0002\u0002\u017b\u017e\u0003\u0002\u0002\u0002\u017c\u017a",
    "\u0003\u0002\u0002\u0002\u017c\u017d\u0003\u0002\u0002\u0002\u017d\u017f",
    "\u0003\u0002\u0002\u0002\u017e\u017c\u0003\u0002\u0002\u0002\u017f\u0180",
    "\u0007)\u0002\u0002\u0180b\u0003\u0002\u0002\u0002\u0181\u0182\u0007",
    "/\u0002\u0002\u0182\u0187\u0007/\u0002\u0002\u0183\u0184\u00071\u0002",
    "\u0002\u0184\u0187\u00071\u0002\u0002\u0185\u0187\u0007%\u0002\u0002",
    "\u0186\u0181\u0003\u0002\u0002\u0002\u0186\u0183\u0003\u0002\u0002\u0002",
    "\u0186\u0185\u0003\u0002\u0002\u0002\u0187\u018b\u0003\u0002\u0002\u0002",
    "\u0188\u018a\n\u0005\u0002\u0002\u0189\u0188\u0003\u0002\u0002\u0002",
    "\u018a\u018d\u0003\u0002\u0002\u0002\u018b\u0189\u0003\u0002\u0002\u0002",
    "\u018b\u018c\u0003\u0002\u0002\u0002\u018c\u018e\u0003\u0002\u0002\u0002",
    "\u018d\u018b\u0003\u0002\u0002\u0002\u018e\u018f\b2\u0002\u0002\u018f",
    "d\u0003\u0002\u0002\u0002\u0190\u0191\u00071\u0002\u0002\u0191\u0192",
    "\u0007,\u0002\u0002\u0192\u0196\u0003\u0002\u0002\u0002\u0193\u0195",
    "\u000b\u0002\u0002\u0002\u0194\u0193\u0003\u0002\u0002\u0002\u0195\u0198",
    "\u0003\u0002\u0002\u0002\u0196\u0197\u0003\u0002\u0002\u0002\u0196\u0194",
    "\u0003\u0002\u0002\u0002\u0197\u019c\u0003\u0002\u0002\u0002\u0198\u0196",
    "\u0003\u0002\u0002\u0002\u0199\u019a\u0007,\u0002\u0002\u019a\u019d",
    "\u00071\u0002\u0002\u019b\u019d\u0007\u0002\u0002\u0003\u019c\u0199",
    "\u0003\u0002\u0002\u0002\u019c\u019b\u0003\u0002\u0002\u0002\u019d\u019e",
    "\u0003\u0002\u0002\u0002\u019e\u019f\b3\u0002\u0002\u019ff\u0003\u0002",
    "\u0002\u0002\u01a0\u01a1\t\u0006\u0002\u0002\u01a1\u01a2\u0003\u0002",
    "\u0002\u0002\u01a2\u01a3\b4\u0002\u0002\u01a3h\u0003\u0002\u0002\u0002",
    "\u01a4\u01a8\t\u0007\u0002\u0002\u01a5\u01a7\t\b\u0002\u0002\u01a6\u01a5",
    "\u0003\u0002\u0002\u0002\u01a7\u01aa\u0003\u0002\u0002\u0002\u01a8\u01a6",
    "\u0003\u0002\u0002\u0002\u01a8\u01a9\u0003\u0002\u0002\u0002\u01a9j",
    "\u0003\u0002\u0002\u0002\u01aa\u01a8\u0003\u0002\u0002\u0002\u01ab\u01ac",
    "\t\t\u0002\u0002\u01acl\u0003\u0002\u0002\u0002\u01ad\u01ae\t\n\u0002",
    "\u0002\u01aen\u0003\u0002\u0002\u0002\u01af\u01b0\t\u000b\u0002\u0002",
    "\u01b0p\u0003\u0002\u0002\u0002\u01b1\u01b2\t\f\u0002\u0002\u01b2r\u0003",
    "\u0002\u0002\u0002\u01b3\u01b4\t\r\u0002\u0002\u01b4t\u0003\u0002\u0002",
    "\u0002\u01b5\u01b6\t\u000e\u0002\u0002\u01b6v\u0003\u0002\u0002\u0002",
    "\u01b7\u01b8\t\u000f\u0002\u0002\u01b8x\u0003\u0002\u0002\u0002\u01b9",
    "\u01ba\t\u0010\u0002\u0002\u01baz\u0003\u0002\u0002\u0002\u01bb\u01bc",
    "\t\u0011\u0002\u0002\u01bc|\u0003\u0002\u0002\u0002\u01bd\u01be\t\u0012",
    "\u0002\u0002\u01be~\u0003\u0002\u0002\u0002\u01bf\u01c0\t\u0013\u0002",
    "\u0002\u01c0\u0080\u0003\u0002\u0002\u0002\u01c1\u01c2\t\u0014\u0002",
    "\u0002\u01c2\u0082\u0003\u0002\u0002\u0002\u01c3\u01c4\t\u0015\u0002",
    "\u0002\u01c4\u0084\u0003\u0002\u0002\u0002\u01c5\u01c6\t\u0016\u0002",
    "\u0002\u01c6\u0086\u0003\u0002\u0002\u0002\u01c7\u01c8\t\u0017\u0002",
    "\u0002\u01c8\u0088\u0003\u0002\u0002\u0002\u01c9\u01ca\t\u0018\u0002",
    "\u0002\u01ca\u008a\u0003\u0002\u0002\u0002\u01cb\u01cc\t\u0019\u0002",
    "\u0002\u01cc\u008c\u0003\u0002\u0002\u0002\u01cd\u01ce\t\u001a\u0002",
    "\u0002\u01ce\u008e\u0003\u0002\u0002\u0002\u01cf\u01d0\t\u001b\u0002",
    "\u0002\u01d0\u0090\u0003\u0002\u0002\u0002\u01d1\u01d2\t\u001c\u0002",
    "\u0002\u01d2\u0092\u0003\u0002\u0002\u0002\u01d3\u01d4\t\u001d\u0002",
    "\u0002\u01d4\u0094\u0003\u0002\u0002\u0002\u01d5\u01d6\t\u001e\u0002",
    "\u0002\u01d6\u0096\u0003\u0002\u0002\u0002\u01d7\u01d8\t\u001f\u0002",
    "\u0002\u01d8\u0098\u0003\u0002\u0002\u0002\u01d9\u01da\t \u0002\u0002",
    "\u01da\u009a\u0003\u0002\u0002\u0002\u01db\u01dc\t!\u0002\u0002\u01dc",
    "\u009c\u0003\u0002\u0002\u0002\u01dd\u01de\t\"\u0002\u0002\u01de\u009e",
    "\u0003\u0002\u0002\u0002\u01df\u01e0\t#\u0002\u0002\u01e0\u00a0\u0003",
    "\u0002\u0002\u0002\u001b\u0002\u0128\u012e\u0131\u0135\u013a\u013c\u0142",
    "\u0146\u014b\u014d\u014f\u0157\u0159\u0162\u0164\u016f\u0171\u017a\u017c",
    "\u0186\u018b\u0196\u019c\u01a8\u0003\u0002\u0003\u0002"].join("");


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
PqlLexer.AND = 1;
PqlLexer.EQ = 2;
PqlLexer.GT_EQ = 3;
PqlLexer.LT_EQ = 4;
PqlLexer.NOT_EQ1 = 5;
PqlLexer.NOT_EQ2 = 6;
PqlLexer.OR = 7;
PqlLexer.SHIFT_LEFT = 8;
PqlLexer.SHIFT_RIGHT = 9;
PqlLexer.AMP = 10;
PqlLexer.ASSIGN = 11;
PqlLexer.CLOSE_PAREN = 12;
PqlLexer.COLON = 13;
PqlLexer.COMMA = 14;
PqlLexer.DOT = 15;
PqlLexer.FORWARD_SLASH = 16;
PqlLexer.GT = 17;
PqlLexer.LT = 18;
PqlLexer.MINUS = 19;
PqlLexer.MOD = 20;
PqlLexer.OPEN_PAREN = 21;
PqlLexer.PIPE = 22;
PqlLexer.PLUS = 23;
PqlLexer.QUESTION_MARK = 24;
PqlLexer.SCOL = 25;
PqlLexer.STAR = 26;
PqlLexer.TILDE = 27;
PqlLexer.UNDER = 28;
PqlLexer.K_AND = 29;
PqlLexer.K_BETWEEN = 30;
PqlLexer.K_FALSE = 31;
PqlLexer.K_ILIKE = 32;
PqlLexer.K_IN = 33;
PqlLexer.K_IS = 34;
PqlLexer.K_ISNULL = 35;
PqlLexer.K_LIKE = 36;
PqlLexer.K_NOT = 37;
PqlLexer.K_NOTNULL = 38;
PqlLexer.K_NULL = 39;
PqlLexer.K_OR = 40;
PqlLexer.K_TRUE = 41;
PqlLexer.NUMERIC_LITERAL = 42;
PqlLexer.DOUBLE_QUOTED_STRING = 43;
PqlLexer.DOUBLE_QUOTED_STRING_TEL = 44;
PqlLexer.DOUBLE_QUOTED_STRING_SQL = 45;
PqlLexer.SINGLE_QUOTED_STRING = 46;
PqlLexer.SINGLE_QUOTED_STRING_TEL = 47;
PqlLexer.SINGLE_QUOTED_STRING_SQL = 48;
PqlLexer.SINGLE_LINE_COMMENT = 49;
PqlLexer.MULTILINE_COMMENT = 50;
PqlLexer.SPACES = 51;
PqlLexer.WORD = 52;

PqlLexer.prototype.channelNames = [ "DEFAULT_TOKEN_CHANNEL", "HIDDEN" ];

PqlLexer.prototype.modeNames = [ "DEFAULT_MODE" ];

PqlLexer.prototype.literalNames = [ null, "'&&'", "'=='", "'>='", "'<='", 
                                    "'!='", "'<>'", "'||'", "'<<'", "'>>'", 
                                    "'&'", "'='", "')'", "':'", "','", "'.'", 
                                    "'/'", "'>'", "'<'", "'-'", "'%'", "'('", 
                                    "'|'", "'+'", "'?'", "';'", "'*'", "'~'", 
                                    "'_'" ];

PqlLexer.prototype.symbolicNames = [ null, "AND", "EQ", "GT_EQ", "LT_EQ", 
                                     "NOT_EQ1", "NOT_EQ2", "OR", "SHIFT_LEFT", 
                                     "SHIFT_RIGHT", "AMP", "ASSIGN", "CLOSE_PAREN", 
                                     "COLON", "COMMA", "DOT", "FORWARD_SLASH", 
                                     "GT", "LT", "MINUS", "MOD", "OPEN_PAREN", 
                                     "PIPE", "PLUS", "QUESTION_MARK", "SCOL", 
                                     "STAR", "TILDE", "UNDER", "K_AND", 
                                     "K_BETWEEN", "K_FALSE", "K_ILIKE", 
                                     "K_IN", "K_IS", "K_ISNULL", "K_LIKE", 
                                     "K_NOT", "K_NOTNULL", "K_NULL", "K_OR", 
                                     "K_TRUE", "NUMERIC_LITERAL", "DOUBLE_QUOTED_STRING", 
                                     "DOUBLE_QUOTED_STRING_TEL", "DOUBLE_QUOTED_STRING_SQL", 
                                     "SINGLE_QUOTED_STRING", "SINGLE_QUOTED_STRING_TEL", 
                                     "SINGLE_QUOTED_STRING_SQL", "SINGLE_LINE_COMMENT", 
                                     "MULTILINE_COMMENT", "SPACES", "WORD" ];

PqlLexer.prototype.ruleNames = [ "AND", "EQ", "GT_EQ", "LT_EQ", "NOT_EQ1", 
                                 "NOT_EQ2", "OR", "SHIFT_LEFT", "SHIFT_RIGHT", 
                                 "AMP", "ASSIGN", "CLOSE_PAREN", "COLON", 
                                 "COMMA", "DOT", "FORWARD_SLASH", "GT", 
                                 "LT", "MINUS", "MOD", "OPEN_PAREN", "PIPE", 
                                 "PLUS", "QUESTION_MARK", "SCOL", "STAR", 
                                 "TILDE", "UNDER", "K_AND", "K_BETWEEN", 
                                 "K_FALSE", "K_ILIKE", "K_IN", "K_IS", "K_ISNULL", 
                                 "K_LIKE", "K_NOT", "K_NOTNULL", "K_NULL", 
                                 "K_OR", "K_TRUE", "NUMERIC_LITERAL", "DOUBLE_QUOTED_STRING", 
                                 "DOUBLE_QUOTED_STRING_TEL", "DOUBLE_QUOTED_STRING_SQL", 
                                 "SINGLE_QUOTED_STRING", "SINGLE_QUOTED_STRING_TEL", 
                                 "SINGLE_QUOTED_STRING_SQL", "SINGLE_LINE_COMMENT", 
                                 "MULTILINE_COMMENT", "SPACES", "WORD", 
                                 "DIGIT", "A", "B", "C", "D", "E", "F", 
                                 "G", "H", "I", "J", "K", "L", "M", "N", 
                                 "O", "P", "Q", "R", "S", "T", "U", "V", 
                                 "W", "X", "Y", "Z" ];

PqlLexer.prototype.grammarFileName = "PqlLexer.g4";


exports.PqlLexer = PqlLexer;


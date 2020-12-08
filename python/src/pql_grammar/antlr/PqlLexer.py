# Generated from grammar/PqlLexer.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\66")
        buf.write("\u01e1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\3\2\3\2\3\2\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3")
        buf.write("\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3&\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3)\3)\3")
        buf.write(")\3*\3*\3*\3*\3*\3+\6+\u0127\n+\r+\16+\u0128\3+\3+\7+")
        buf.write("\u012d\n+\f+\16+\u0130\13+\5+\u0132\n+\3+\3+\5+\u0136")
        buf.write("\n+\3+\6+\u0139\n+\r+\16+\u013a\5+\u013d\n+\3+\3+\6+\u0141")
        buf.write("\n+\r+\16+\u0142\3+\3+\5+\u0147\n+\3+\6+\u014a\n+\r+\16")
        buf.write("+\u014b\5+\u014e\n+\5+\u0150\n+\3,\3,\3-\3-\3-\3-\7-\u0158")
        buf.write("\n-\f-\16-\u015b\13-\3-\3-\3.\3.\3.\3.\7.\u0163\n.\f.")
        buf.write("\16.\u0166\13.\3.\3.\3/\3/\3\60\3\60\3\60\3\60\7\60\u0170")
        buf.write("\n\60\f\60\16\60\u0173\13\60\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\61\7\61\u017b\n\61\f\61\16\61\u017e\13\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\3\62\3\62\5\62\u0187\n\62\3\62\7\62\u018a")
        buf.write("\n\62\f\62\16\62\u018d\13\62\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\63\7\63\u0195\n\63\f\63\16\63\u0198\13\63\3\63\3\63")
        buf.write("\3\63\5\63\u019d\n\63\3\63\3\63\3\64\3\64\3\64\3\64\3")
        buf.write("\65\3\65\7\65\u01a7\n\65\f\65\16\65\u01aa\13\65\3\66\3")
        buf.write("\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3")
        buf.write(">\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3")
        buf.write("G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3P\3")
        buf.write("P\3\u0196\2Q\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#")
        buf.write("E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66")
        buf.write("k\2m\2o\2q\2s\2u\2w\2y\2{\2}\2\177\2\u0081\2\u0083\2\u0085")
        buf.write("\2\u0087\2\u0089\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093")
        buf.write("\2\u0095\2\u0097\2\u0099\2\u009b\2\u009d\2\u009f\2\3\2")
        buf.write("$\4\2--//\3\2$$\3\2))\4\2\f\f\17\17\5\2\13\r\17\17\"\"")
        buf.write("\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2CCcc\4\2DDdd\4\2")
        buf.write("EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4")
        buf.write("\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRr")
        buf.write("r\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2")
        buf.write("YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\2\u01de\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\3\u00a1\3\2\2\2\5\u00a4\3\2\2\2\7\u00a7\3\2\2\2\t\u00aa")
        buf.write("\3\2\2\2\13\u00ad\3\2\2\2\r\u00b0\3\2\2\2\17\u00b3\3\2")
        buf.write("\2\2\21\u00b6\3\2\2\2\23\u00b9\3\2\2\2\25\u00bc\3\2\2")
        buf.write("\2\27\u00be\3\2\2\2\31\u00c0\3\2\2\2\33\u00c2\3\2\2\2")
        buf.write("\35\u00c4\3\2\2\2\37\u00c6\3\2\2\2!\u00c8\3\2\2\2#\u00ca")
        buf.write("\3\2\2\2%\u00cc\3\2\2\2\'\u00ce\3\2\2\2)\u00d0\3\2\2\2")
        buf.write("+\u00d2\3\2\2\2-\u00d4\3\2\2\2/\u00d6\3\2\2\2\61\u00d8")
        buf.write("\3\2\2\2\63\u00da\3\2\2\2\65\u00dc\3\2\2\2\67\u00de\3")
        buf.write("\2\2\29\u00e0\3\2\2\2;\u00e2\3\2\2\2=\u00e6\3\2\2\2?\u00ee")
        buf.write("\3\2\2\2A\u00f4\3\2\2\2C\u00fa\3\2\2\2E\u00fd\3\2\2\2")
        buf.write("G\u0100\3\2\2\2I\u0107\3\2\2\2K\u010c\3\2\2\2M\u0110\3")
        buf.write("\2\2\2O\u0118\3\2\2\2Q\u011d\3\2\2\2S\u0120\3\2\2\2U\u014f")
        buf.write("\3\2\2\2W\u0151\3\2\2\2Y\u0153\3\2\2\2[\u015e\3\2\2\2")
        buf.write("]\u0169\3\2\2\2_\u016b\3\2\2\2a\u0176\3\2\2\2c\u0186\3")
        buf.write("\2\2\2e\u0190\3\2\2\2g\u01a0\3\2\2\2i\u01a4\3\2\2\2k\u01ab")
        buf.write("\3\2\2\2m\u01ad\3\2\2\2o\u01af\3\2\2\2q\u01b1\3\2\2\2")
        buf.write("s\u01b3\3\2\2\2u\u01b5\3\2\2\2w\u01b7\3\2\2\2y\u01b9\3")
        buf.write("\2\2\2{\u01bb\3\2\2\2}\u01bd\3\2\2\2\177\u01bf\3\2\2\2")
        buf.write("\u0081\u01c1\3\2\2\2\u0083\u01c3\3\2\2\2\u0085\u01c5\3")
        buf.write("\2\2\2\u0087\u01c7\3\2\2\2\u0089\u01c9\3\2\2\2\u008b\u01cb")
        buf.write("\3\2\2\2\u008d\u01cd\3\2\2\2\u008f\u01cf\3\2\2\2\u0091")
        buf.write("\u01d1\3\2\2\2\u0093\u01d3\3\2\2\2\u0095\u01d5\3\2\2\2")
        buf.write("\u0097\u01d7\3\2\2\2\u0099\u01d9\3\2\2\2\u009b\u01db\3")
        buf.write("\2\2\2\u009d\u01dd\3\2\2\2\u009f\u01df\3\2\2\2\u00a1\u00a2")
        buf.write("\7(\2\2\u00a2\u00a3\7(\2\2\u00a3\4\3\2\2\2\u00a4\u00a5")
        buf.write("\7?\2\2\u00a5\u00a6\7?\2\2\u00a6\6\3\2\2\2\u00a7\u00a8")
        buf.write("\7@\2\2\u00a8\u00a9\7?\2\2\u00a9\b\3\2\2\2\u00aa\u00ab")
        buf.write("\7>\2\2\u00ab\u00ac\7?\2\2\u00ac\n\3\2\2\2\u00ad\u00ae")
        buf.write("\7#\2\2\u00ae\u00af\7?\2\2\u00af\f\3\2\2\2\u00b0\u00b1")
        buf.write("\7>\2\2\u00b1\u00b2\7@\2\2\u00b2\16\3\2\2\2\u00b3\u00b4")
        buf.write("\7~\2\2\u00b4\u00b5\7~\2\2\u00b5\20\3\2\2\2\u00b6\u00b7")
        buf.write("\7>\2\2\u00b7\u00b8\7>\2\2\u00b8\22\3\2\2\2\u00b9\u00ba")
        buf.write("\7@\2\2\u00ba\u00bb\7@\2\2\u00bb\24\3\2\2\2\u00bc\u00bd")
        buf.write("\7(\2\2\u00bd\26\3\2\2\2\u00be\u00bf\7?\2\2\u00bf\30\3")
        buf.write("\2\2\2\u00c0\u00c1\7+\2\2\u00c1\32\3\2\2\2\u00c2\u00c3")
        buf.write("\7<\2\2\u00c3\34\3\2\2\2\u00c4\u00c5\7.\2\2\u00c5\36\3")
        buf.write("\2\2\2\u00c6\u00c7\7\60\2\2\u00c7 \3\2\2\2\u00c8\u00c9")
        buf.write("\7\61\2\2\u00c9\"\3\2\2\2\u00ca\u00cb\7@\2\2\u00cb$\3")
        buf.write("\2\2\2\u00cc\u00cd\7>\2\2\u00cd&\3\2\2\2\u00ce\u00cf\7")
        buf.write("/\2\2\u00cf(\3\2\2\2\u00d0\u00d1\7\'\2\2\u00d1*\3\2\2")
        buf.write("\2\u00d2\u00d3\7*\2\2\u00d3,\3\2\2\2\u00d4\u00d5\7~\2")
        buf.write("\2\u00d5.\3\2\2\2\u00d6\u00d7\7-\2\2\u00d7\60\3\2\2\2")
        buf.write("\u00d8\u00d9\7A\2\2\u00d9\62\3\2\2\2\u00da\u00db\7=\2")
        buf.write("\2\u00db\64\3\2\2\2\u00dc\u00dd\7,\2\2\u00dd\66\3\2\2")
        buf.write("\2\u00de\u00df\7\u0080\2\2\u00df8\3\2\2\2\u00e0\u00e1")
        buf.write("\7a\2\2\u00e1:\3\2\2\2\u00e2\u00e3\5m\67\2\u00e3\u00e4")
        buf.write("\5\u0087D\2\u00e4\u00e5\5s:\2\u00e5<\3\2\2\2\u00e6\u00e7")
        buf.write("\5o8\2\u00e7\u00e8\5u;\2\u00e8\u00e9\5\u0093J\2\u00e9")
        buf.write("\u00ea\5\u0099M\2\u00ea\u00eb\5u;\2\u00eb\u00ec\5u;\2")
        buf.write("\u00ec\u00ed\5\u0087D\2\u00ed>\3\2\2\2\u00ee\u00ef\5w")
        buf.write("<\2\u00ef\u00f0\5m\67\2\u00f0\u00f1\5\u0083B\2\u00f1\u00f2")
        buf.write("\5\u0091I\2\u00f2\u00f3\5u;\2\u00f3@\3\2\2\2\u00f4\u00f5")
        buf.write("\5}?\2\u00f5\u00f6\5\u0083B\2\u00f6\u00f7\5}?\2\u00f7")
        buf.write("\u00f8\5\u0081A\2\u00f8\u00f9\5u;\2\u00f9B\3\2\2\2\u00fa")
        buf.write("\u00fb\5}?\2\u00fb\u00fc\5\u0087D\2\u00fcD\3\2\2\2\u00fd")
        buf.write("\u00fe\5}?\2\u00fe\u00ff\5\u0091I\2\u00ffF\3\2\2\2\u0100")
        buf.write("\u0101\5}?\2\u0101\u0102\5\u0091I\2\u0102\u0103\5\u0087")
        buf.write("D\2\u0103\u0104\5\u0095K\2\u0104\u0105\5\u0083B\2\u0105")
        buf.write("\u0106\5\u0083B\2\u0106H\3\2\2\2\u0107\u0108\5\u0083B")
        buf.write("\2\u0108\u0109\5}?\2\u0109\u010a\5\u0081A\2\u010a\u010b")
        buf.write("\5u;\2\u010bJ\3\2\2\2\u010c\u010d\5\u0087D\2\u010d\u010e")
        buf.write("\5\u0089E\2\u010e\u010f\5\u0093J\2\u010fL\3\2\2\2\u0110")
        buf.write("\u0111\5\u0087D\2\u0111\u0112\5\u0089E\2\u0112\u0113\5")
        buf.write("\u0093J\2\u0113\u0114\5\u0087D\2\u0114\u0115\5\u0095K")
        buf.write("\2\u0115\u0116\5\u0083B\2\u0116\u0117\5\u0083B\2\u0117")
        buf.write("N\3\2\2\2\u0118\u0119\5\u0087D\2\u0119\u011a\5\u0095K")
        buf.write("\2\u011a\u011b\5\u0083B\2\u011b\u011c\5\u0083B\2\u011c")
        buf.write("P\3\2\2\2\u011d\u011e\5\u0089E\2\u011e\u011f\5\u008fH")
        buf.write("\2\u011fR\3\2\2\2\u0120\u0121\5\u0093J\2\u0121\u0122\5")
        buf.write("\u008fH\2\u0122\u0123\5\u0095K\2\u0123\u0124\5u;\2\u0124")
        buf.write("T\3\2\2\2\u0125\u0127\5k\66\2\u0126\u0125\3\2\2\2\u0127")
        buf.write("\u0128\3\2\2\2\u0128\u0126\3\2\2\2\u0128\u0129\3\2\2\2")
        buf.write("\u0129\u0131\3\2\2\2\u012a\u012e\7\60\2\2\u012b\u012d")
        buf.write("\5k\66\2\u012c\u012b\3\2\2\2\u012d\u0130\3\2\2\2\u012e")
        buf.write("\u012c\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0132\3\2\2\2")
        buf.write("\u0130\u012e\3\2\2\2\u0131\u012a\3\2\2\2\u0131\u0132\3")
        buf.write("\2\2\2\u0132\u013c\3\2\2\2\u0133\u0135\5u;\2\u0134\u0136")
        buf.write("\t\2\2\2\u0135\u0134\3\2\2\2\u0135\u0136\3\2\2\2\u0136")
        buf.write("\u0138\3\2\2\2\u0137\u0139\5k\66\2\u0138\u0137\3\2\2\2")
        buf.write("\u0139\u013a\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u013b\3")
        buf.write("\2\2\2\u013b\u013d\3\2\2\2\u013c\u0133\3\2\2\2\u013c\u013d")
        buf.write("\3\2\2\2\u013d\u0150\3\2\2\2\u013e\u0140\7\60\2\2\u013f")
        buf.write("\u0141\5k\66\2\u0140\u013f\3\2\2\2\u0141\u0142\3\2\2\2")
        buf.write("\u0142\u0140\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u014d\3")
        buf.write("\2\2\2\u0144\u0146\5u;\2\u0145\u0147\t\2\2\2\u0146\u0145")
        buf.write("\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0149\3\2\2\2\u0148")
        buf.write("\u014a\5k\66\2\u0149\u0148\3\2\2\2\u014a\u014b\3\2\2\2")
        buf.write("\u014b\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014e\3")
        buf.write("\2\2\2\u014d\u0144\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u0150")
        buf.write("\3\2\2\2\u014f\u0126\3\2\2\2\u014f\u013e\3\2\2\2\u0150")
        buf.write("V\3\2\2\2\u0151\u0152\5Y-\2\u0152X\3\2\2\2\u0153\u0159")
        buf.write("\7$\2\2\u0154\u0155\7^\2\2\u0155\u0158\7$\2\2\u0156\u0158")
        buf.write("\n\3\2\2\u0157\u0154\3\2\2\2\u0157\u0156\3\2\2\2\u0158")
        buf.write("\u015b\3\2\2\2\u0159\u0157\3\2\2\2\u0159\u015a\3\2\2\2")
        buf.write("\u015a\u015c\3\2\2\2\u015b\u0159\3\2\2\2\u015c\u015d\7")
        buf.write("$\2\2\u015dZ\3\2\2\2\u015e\u0164\7$\2\2\u015f\u0160\7")
        buf.write("$\2\2\u0160\u0163\7$\2\2\u0161\u0163\n\3\2\2\u0162\u015f")
        buf.write("\3\2\2\2\u0162\u0161\3\2\2\2\u0163\u0166\3\2\2\2\u0164")
        buf.write("\u0162\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0167\3\2\2\2")
        buf.write("\u0166\u0164\3\2\2\2\u0167\u0168\7$\2\2\u0168\\\3\2\2")
        buf.write("\2\u0169\u016a\5_\60\2\u016a^\3\2\2\2\u016b\u0171\7)\2")
        buf.write("\2\u016c\u016d\7^\2\2\u016d\u0170\7)\2\2\u016e\u0170\n")
        buf.write("\4\2\2\u016f\u016c\3\2\2\2\u016f\u016e\3\2\2\2\u0170\u0173")
        buf.write("\3\2\2\2\u0171\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172")
        buf.write("\u0174\3\2\2\2\u0173\u0171\3\2\2\2\u0174\u0175\7)\2\2")
        buf.write("\u0175`\3\2\2\2\u0176\u017c\7)\2\2\u0177\u0178\7)\2\2")
        buf.write("\u0178\u017b\7)\2\2\u0179\u017b\n\4\2\2\u017a\u0177\3")
        buf.write("\2\2\2\u017a\u0179\3\2\2\2\u017b\u017e\3\2\2\2\u017c\u017a")
        buf.write("\3\2\2\2\u017c\u017d\3\2\2\2\u017d\u017f\3\2\2\2\u017e")
        buf.write("\u017c\3\2\2\2\u017f\u0180\7)\2\2\u0180b\3\2\2\2\u0181")
        buf.write("\u0182\7/\2\2\u0182\u0187\7/\2\2\u0183\u0184\7\61\2\2")
        buf.write("\u0184\u0187\7\61\2\2\u0185\u0187\7%\2\2\u0186\u0181\3")
        buf.write("\2\2\2\u0186\u0183\3\2\2\2\u0186\u0185\3\2\2\2\u0187\u018b")
        buf.write("\3\2\2\2\u0188\u018a\n\5\2\2\u0189\u0188\3\2\2\2\u018a")
        buf.write("\u018d\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018c\3\2\2\2")
        buf.write("\u018c\u018e\3\2\2\2\u018d\u018b\3\2\2\2\u018e\u018f\b")
        buf.write("\62\2\2\u018fd\3\2\2\2\u0190\u0191\7\61\2\2\u0191\u0192")
        buf.write("\7,\2\2\u0192\u0196\3\2\2\2\u0193\u0195\13\2\2\2\u0194")
        buf.write("\u0193\3\2\2\2\u0195\u0198\3\2\2\2\u0196\u0197\3\2\2\2")
        buf.write("\u0196\u0194\3\2\2\2\u0197\u019c\3\2\2\2\u0198\u0196\3")
        buf.write("\2\2\2\u0199\u019a\7,\2\2\u019a\u019d\7\61\2\2\u019b\u019d")
        buf.write("\7\2\2\3\u019c\u0199\3\2\2\2\u019c\u019b\3\2\2\2\u019d")
        buf.write("\u019e\3\2\2\2\u019e\u019f\b\63\2\2\u019ff\3\2\2\2\u01a0")
        buf.write("\u01a1\t\6\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a3\b\64\2")
        buf.write("\2\u01a3h\3\2\2\2\u01a4\u01a8\t\7\2\2\u01a5\u01a7\t\b")
        buf.write("\2\2\u01a6\u01a5\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01a6")
        buf.write("\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9j\3\2\2\2\u01aa\u01a8")
        buf.write("\3\2\2\2\u01ab\u01ac\t\t\2\2\u01acl\3\2\2\2\u01ad\u01ae")
        buf.write("\t\n\2\2\u01aen\3\2\2\2\u01af\u01b0\t\13\2\2\u01b0p\3")
        buf.write("\2\2\2\u01b1\u01b2\t\f\2\2\u01b2r\3\2\2\2\u01b3\u01b4")
        buf.write("\t\r\2\2\u01b4t\3\2\2\2\u01b5\u01b6\t\16\2\2\u01b6v\3")
        buf.write("\2\2\2\u01b7\u01b8\t\17\2\2\u01b8x\3\2\2\2\u01b9\u01ba")
        buf.write("\t\20\2\2\u01baz\3\2\2\2\u01bb\u01bc\t\21\2\2\u01bc|\3")
        buf.write("\2\2\2\u01bd\u01be\t\22\2\2\u01be~\3\2\2\2\u01bf\u01c0")
        buf.write("\t\23\2\2\u01c0\u0080\3\2\2\2\u01c1\u01c2\t\24\2\2\u01c2")
        buf.write("\u0082\3\2\2\2\u01c3\u01c4\t\25\2\2\u01c4\u0084\3\2\2")
        buf.write("\2\u01c5\u01c6\t\26\2\2\u01c6\u0086\3\2\2\2\u01c7\u01c8")
        buf.write("\t\27\2\2\u01c8\u0088\3\2\2\2\u01c9\u01ca\t\30\2\2\u01ca")
        buf.write("\u008a\3\2\2\2\u01cb\u01cc\t\31\2\2\u01cc\u008c\3\2\2")
        buf.write("\2\u01cd\u01ce\t\32\2\2\u01ce\u008e\3\2\2\2\u01cf\u01d0")
        buf.write("\t\33\2\2\u01d0\u0090\3\2\2\2\u01d1\u01d2\t\34\2\2\u01d2")
        buf.write("\u0092\3\2\2\2\u01d3\u01d4\t\35\2\2\u01d4\u0094\3\2\2")
        buf.write("\2\u01d5\u01d6\t\36\2\2\u01d6\u0096\3\2\2\2\u01d7\u01d8")
        buf.write("\t\37\2\2\u01d8\u0098\3\2\2\2\u01d9\u01da\t \2\2\u01da")
        buf.write("\u009a\3\2\2\2\u01db\u01dc\t!\2\2\u01dc\u009c\3\2\2\2")
        buf.write("\u01dd\u01de\t\"\2\2\u01de\u009e\3\2\2\2\u01df\u01e0\t")
        buf.write("#\2\2\u01e0\u00a0\3\2\2\2\33\2\u0128\u012e\u0131\u0135")
        buf.write("\u013a\u013c\u0142\u0146\u014b\u014d\u014f\u0157\u0159")
        buf.write("\u0162\u0164\u016f\u0171\u017a\u017c\u0186\u018b\u0196")
        buf.write("\u019c\u01a8\3\2\3\2")
        return buf.getvalue()


class PqlLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AND = 1
    EQ = 2
    GT_EQ = 3
    LT_EQ = 4
    NOT_EQ1 = 5
    NOT_EQ2 = 6
    OR = 7
    SHIFT_LEFT = 8
    SHIFT_RIGHT = 9
    AMP = 10
    ASSIGN = 11
    CLOSE_PAREN = 12
    COLON = 13
    COMMA = 14
    DOT = 15
    FORWARD_SLASH = 16
    GT = 17
    LT = 18
    MINUS = 19
    MOD = 20
    OPEN_PAREN = 21
    PIPE = 22
    PLUS = 23
    QUESTION_MARK = 24
    SCOL = 25
    STAR = 26
    TILDE = 27
    UNDER = 28
    K_AND = 29
    K_BETWEEN = 30
    K_FALSE = 31
    K_ILIKE = 32
    K_IN = 33
    K_IS = 34
    K_ISNULL = 35
    K_LIKE = 36
    K_NOT = 37
    K_NOTNULL = 38
    K_NULL = 39
    K_OR = 40
    K_TRUE = 41
    NUMERIC_LITERAL = 42
    DOUBLE_QUOTED_STRING = 43
    DOUBLE_QUOTED_STRING_TEL = 44
    DOUBLE_QUOTED_STRING_SQL = 45
    SINGLE_QUOTED_STRING = 46
    SINGLE_QUOTED_STRING_TEL = 47
    SINGLE_QUOTED_STRING_SQL = 48
    SINGLE_LINE_COMMENT = 49
    MULTILINE_COMMENT = 50
    SPACES = 51
    WORD = 52

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'&&'", "'=='", "'>='", "'<='", "'!='", "'<>'", "'||'", "'<<'", 
            "'>>'", "'&'", "'='", "')'", "':'", "','", "'.'", "'/'", "'>'", 
            "'<'", "'-'", "'%'", "'('", "'|'", "'+'", "'?'", "';'", "'*'", 
            "'~'", "'_'" ]

    symbolicNames = [ "<INVALID>",
            "AND", "EQ", "GT_EQ", "LT_EQ", "NOT_EQ1", "NOT_EQ2", "OR", "SHIFT_LEFT", 
            "SHIFT_RIGHT", "AMP", "ASSIGN", "CLOSE_PAREN", "COLON", "COMMA", 
            "DOT", "FORWARD_SLASH", "GT", "LT", "MINUS", "MOD", "OPEN_PAREN", 
            "PIPE", "PLUS", "QUESTION_MARK", "SCOL", "STAR", "TILDE", "UNDER", 
            "K_AND", "K_BETWEEN", "K_FALSE", "K_ILIKE", "K_IN", "K_IS", 
            "K_ISNULL", "K_LIKE", "K_NOT", "K_NOTNULL", "K_NULL", "K_OR", 
            "K_TRUE", "NUMERIC_LITERAL", "DOUBLE_QUOTED_STRING", "DOUBLE_QUOTED_STRING_TEL", 
            "DOUBLE_QUOTED_STRING_SQL", "SINGLE_QUOTED_STRING", "SINGLE_QUOTED_STRING_TEL", 
            "SINGLE_QUOTED_STRING_SQL", "SINGLE_LINE_COMMENT", "MULTILINE_COMMENT", 
            "SPACES", "WORD" ]

    ruleNames = [ "AND", "EQ", "GT_EQ", "LT_EQ", "NOT_EQ1", "NOT_EQ2", "OR", 
                  "SHIFT_LEFT", "SHIFT_RIGHT", "AMP", "ASSIGN", "CLOSE_PAREN", 
                  "COLON", "COMMA", "DOT", "FORWARD_SLASH", "GT", "LT", 
                  "MINUS", "MOD", "OPEN_PAREN", "PIPE", "PLUS", "QUESTION_MARK", 
                  "SCOL", "STAR", "TILDE", "UNDER", "K_AND", "K_BETWEEN", 
                  "K_FALSE", "K_ILIKE", "K_IN", "K_IS", "K_ISNULL", "K_LIKE", 
                  "K_NOT", "K_NOTNULL", "K_NULL", "K_OR", "K_TRUE", "NUMERIC_LITERAL", 
                  "DOUBLE_QUOTED_STRING", "DOUBLE_QUOTED_STRING_TEL", "DOUBLE_QUOTED_STRING_SQL", 
                  "SINGLE_QUOTED_STRING", "SINGLE_QUOTED_STRING_TEL", "SINGLE_QUOTED_STRING_SQL", 
                  "SINGLE_LINE_COMMENT", "MULTILINE_COMMENT", "SPACES", 
                  "WORD", "DIGIT", "A", "B", "C", "D", "E", "F", "G", "H", 
                  "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", 
                  "T", "U", "V", "W", "X", "Y", "Z" ]

    grammarFileName = "PqlLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



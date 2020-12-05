# Generated from grammar/PqlLexer.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\65")
        buf.write("\u01d9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3")
        buf.write("\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 ")
        buf.write("\3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3)\3*\6*\u011f")
        buf.write("\n*\r*\16*\u0120\3*\3*\7*\u0125\n*\f*\16*\u0128\13*\5")
        buf.write("*\u012a\n*\3*\3*\5*\u012e\n*\3*\6*\u0131\n*\r*\16*\u0132")
        buf.write("\5*\u0135\n*\3*\3*\6*\u0139\n*\r*\16*\u013a\3*\3*\5*\u013f")
        buf.write("\n*\3*\6*\u0142\n*\r*\16*\u0143\5*\u0146\n*\5*\u0148\n")
        buf.write("*\3+\3+\3,\3,\3,\3,\7,\u0150\n,\f,\16,\u0153\13,\3,\3")
        buf.write(",\3-\3-\3-\3-\7-\u015b\n-\f-\16-\u015e\13-\3-\3-\3.\3")
        buf.write(".\3/\3/\3/\3/\7/\u0168\n/\f/\16/\u016b\13/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\60\7\60\u0173\n\60\f\60\16\60\u0176\13\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\61\3\61\5\61\u017f\n\61\3")
        buf.write("\61\7\61\u0182\n\61\f\61\16\61\u0185\13\61\3\61\3\61\3")
        buf.write("\62\3\62\3\62\3\62\7\62\u018d\n\62\f\62\16\62\u0190\13")
        buf.write("\62\3\62\3\62\3\62\5\62\u0195\n\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\63\3\64\3\64\7\64\u019f\n\64\f\64\16\64\u01a2")
        buf.write("\13\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3")
        buf.write(":\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3")
        buf.write("C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3")
        buf.write("L\3M\3M\3N\3N\3O\3O\3\u018e\2P\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\2k\2m\2o\2q\2s\2u\2w\2y\2{\2}\2\177")
        buf.write("\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089\2\u008b\2\u008d")
        buf.write("\2\u008f\2\u0091\2\u0093\2\u0095\2\u0097\2\u0099\2\u009b")
        buf.write("\2\u009d\2\3\2$\4\2--//\3\2$$\3\2))\4\2\f\f\17\17\5\2")
        buf.write("\13\r\17\17\"\"\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2")
        buf.write("CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4")
        buf.write("\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPp")
        buf.write("p\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2")
        buf.write("WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\2\u01d6")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\3\u009f\3\2\2\2\5\u00a2\3\2\2\2\7\u00a5\3\2\2\2")
        buf.write("\t\u00a8\3\2\2\2\13\u00ab\3\2\2\2\r\u00ae\3\2\2\2\17\u00b1")
        buf.write("\3\2\2\2\21\u00b4\3\2\2\2\23\u00b7\3\2\2\2\25\u00ba\3")
        buf.write("\2\2\2\27\u00bc\3\2\2\2\31\u00be\3\2\2\2\33\u00c0\3\2")
        buf.write("\2\2\35\u00c2\3\2\2\2\37\u00c4\3\2\2\2!\u00c6\3\2\2\2")
        buf.write("#\u00c8\3\2\2\2%\u00ca\3\2\2\2\'\u00cc\3\2\2\2)\u00ce")
        buf.write("\3\2\2\2+\u00d0\3\2\2\2-\u00d2\3\2\2\2/\u00d4\3\2\2\2")
        buf.write("\61\u00d6\3\2\2\2\63\u00d8\3\2\2\2\65\u00da\3\2\2\2\67")
        buf.write("\u00dc\3\2\2\29\u00de\3\2\2\2;\u00e0\3\2\2\2=\u00e4\3")
        buf.write("\2\2\2?\u00ec\3\2\2\2A\u00f2\3\2\2\2C\u00f5\3\2\2\2E\u00f8")
        buf.write("\3\2\2\2G\u00ff\3\2\2\2I\u0104\3\2\2\2K\u0108\3\2\2\2")
        buf.write("M\u0110\3\2\2\2O\u0115\3\2\2\2Q\u0118\3\2\2\2S\u0147\3")
        buf.write("\2\2\2U\u0149\3\2\2\2W\u014b\3\2\2\2Y\u0156\3\2\2\2[\u0161")
        buf.write("\3\2\2\2]\u0163\3\2\2\2_\u016e\3\2\2\2a\u017e\3\2\2\2")
        buf.write("c\u0188\3\2\2\2e\u0198\3\2\2\2g\u019c\3\2\2\2i\u01a3\3")
        buf.write("\2\2\2k\u01a5\3\2\2\2m\u01a7\3\2\2\2o\u01a9\3\2\2\2q\u01ab")
        buf.write("\3\2\2\2s\u01ad\3\2\2\2u\u01af\3\2\2\2w\u01b1\3\2\2\2")
        buf.write("y\u01b3\3\2\2\2{\u01b5\3\2\2\2}\u01b7\3\2\2\2\177\u01b9")
        buf.write("\3\2\2\2\u0081\u01bb\3\2\2\2\u0083\u01bd\3\2\2\2\u0085")
        buf.write("\u01bf\3\2\2\2\u0087\u01c1\3\2\2\2\u0089\u01c3\3\2\2\2")
        buf.write("\u008b\u01c5\3\2\2\2\u008d\u01c7\3\2\2\2\u008f\u01c9\3")
        buf.write("\2\2\2\u0091\u01cb\3\2\2\2\u0093\u01cd\3\2\2\2\u0095\u01cf")
        buf.write("\3\2\2\2\u0097\u01d1\3\2\2\2\u0099\u01d3\3\2\2\2\u009b")
        buf.write("\u01d5\3\2\2\2\u009d\u01d7\3\2\2\2\u009f\u00a0\7(\2\2")
        buf.write("\u00a0\u00a1\7(\2\2\u00a1\4\3\2\2\2\u00a2\u00a3\7?\2\2")
        buf.write("\u00a3\u00a4\7?\2\2\u00a4\6\3\2\2\2\u00a5\u00a6\7@\2\2")
        buf.write("\u00a6\u00a7\7?\2\2\u00a7\b\3\2\2\2\u00a8\u00a9\7>\2\2")
        buf.write("\u00a9\u00aa\7?\2\2\u00aa\n\3\2\2\2\u00ab\u00ac\7#\2\2")
        buf.write("\u00ac\u00ad\7?\2\2\u00ad\f\3\2\2\2\u00ae\u00af\7>\2\2")
        buf.write("\u00af\u00b0\7@\2\2\u00b0\16\3\2\2\2\u00b1\u00b2\7~\2")
        buf.write("\2\u00b2\u00b3\7~\2\2\u00b3\20\3\2\2\2\u00b4\u00b5\7>")
        buf.write("\2\2\u00b5\u00b6\7>\2\2\u00b6\22\3\2\2\2\u00b7\u00b8\7")
        buf.write("@\2\2\u00b8\u00b9\7@\2\2\u00b9\24\3\2\2\2\u00ba\u00bb")
        buf.write("\7(\2\2\u00bb\26\3\2\2\2\u00bc\u00bd\7?\2\2\u00bd\30\3")
        buf.write("\2\2\2\u00be\u00bf\7+\2\2\u00bf\32\3\2\2\2\u00c0\u00c1")
        buf.write("\7<\2\2\u00c1\34\3\2\2\2\u00c2\u00c3\7.\2\2\u00c3\36\3")
        buf.write("\2\2\2\u00c4\u00c5\7\60\2\2\u00c5 \3\2\2\2\u00c6\u00c7")
        buf.write("\7\61\2\2\u00c7\"\3\2\2\2\u00c8\u00c9\7@\2\2\u00c9$\3")
        buf.write("\2\2\2\u00ca\u00cb\7>\2\2\u00cb&\3\2\2\2\u00cc\u00cd\7")
        buf.write("/\2\2\u00cd(\3\2\2\2\u00ce\u00cf\7\'\2\2\u00cf*\3\2\2")
        buf.write("\2\u00d0\u00d1\7*\2\2\u00d1,\3\2\2\2\u00d2\u00d3\7~\2")
        buf.write("\2\u00d3.\3\2\2\2\u00d4\u00d5\7-\2\2\u00d5\60\3\2\2\2")
        buf.write("\u00d6\u00d7\7A\2\2\u00d7\62\3\2\2\2\u00d8\u00d9\7=\2")
        buf.write("\2\u00d9\64\3\2\2\2\u00da\u00db\7,\2\2\u00db\66\3\2\2")
        buf.write("\2\u00dc\u00dd\7\u0080\2\2\u00dd8\3\2\2\2\u00de\u00df")
        buf.write("\7a\2\2\u00df:\3\2\2\2\u00e0\u00e1\5k\66\2\u00e1\u00e2")
        buf.write("\5\u0085C\2\u00e2\u00e3\5q9\2\u00e3<\3\2\2\2\u00e4\u00e5")
        buf.write("\5m\67\2\u00e5\u00e6\5s:\2\u00e6\u00e7\5\u0091I\2\u00e7")
        buf.write("\u00e8\5\u0097L\2\u00e8\u00e9\5s:\2\u00e9\u00ea\5s:\2")
        buf.write("\u00ea\u00eb\5\u0085C\2\u00eb>\3\2\2\2\u00ec\u00ed\5u")
        buf.write(";\2\u00ed\u00ee\5k\66\2\u00ee\u00ef\5\u0081A\2\u00ef\u00f0")
        buf.write("\5\u008fH\2\u00f0\u00f1\5s:\2\u00f1@\3\2\2\2\u00f2\u00f3")
        buf.write("\5{>\2\u00f3\u00f4\5\u0085C\2\u00f4B\3\2\2\2\u00f5\u00f6")
        buf.write("\5{>\2\u00f6\u00f7\5\u008fH\2\u00f7D\3\2\2\2\u00f8\u00f9")
        buf.write("\5{>\2\u00f9\u00fa\5\u008fH\2\u00fa\u00fb\5\u0085C\2\u00fb")
        buf.write("\u00fc\5\u0093J\2\u00fc\u00fd\5\u0081A\2\u00fd\u00fe\5")
        buf.write("\u0081A\2\u00feF\3\2\2\2\u00ff\u0100\5\u0081A\2\u0100")
        buf.write("\u0101\5{>\2\u0101\u0102\5\177@\2\u0102\u0103\5s:\2\u0103")
        buf.write("H\3\2\2\2\u0104\u0105\5\u0085C\2\u0105\u0106\5\u0087D")
        buf.write("\2\u0106\u0107\5\u0091I\2\u0107J\3\2\2\2\u0108\u0109\5")
        buf.write("\u0085C\2\u0109\u010a\5\u0087D\2\u010a\u010b\5\u0091I")
        buf.write("\2\u010b\u010c\5\u0085C\2\u010c\u010d\5\u0093J\2\u010d")
        buf.write("\u010e\5\u0081A\2\u010e\u010f\5\u0081A\2\u010fL\3\2\2")
        buf.write("\2\u0110\u0111\5\u0085C\2\u0111\u0112\5\u0093J\2\u0112")
        buf.write("\u0113\5\u0081A\2\u0113\u0114\5\u0081A\2\u0114N\3\2\2")
        buf.write("\2\u0115\u0116\5\u0087D\2\u0116\u0117\5\u008dG\2\u0117")
        buf.write("P\3\2\2\2\u0118\u0119\5\u0091I\2\u0119\u011a\5\u008dG")
        buf.write("\2\u011a\u011b\5\u0093J\2\u011b\u011c\5s:\2\u011cR\3\2")
        buf.write("\2\2\u011d\u011f\5i\65\2\u011e\u011d\3\2\2\2\u011f\u0120")
        buf.write("\3\2\2\2\u0120\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121")
        buf.write("\u0129\3\2\2\2\u0122\u0126\7\60\2\2\u0123\u0125\5i\65")
        buf.write("\2\u0124\u0123\3\2\2\2\u0125\u0128\3\2\2\2\u0126\u0124")
        buf.write("\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u012a\3\2\2\2\u0128")
        buf.write("\u0126\3\2\2\2\u0129\u0122\3\2\2\2\u0129\u012a\3\2\2\2")
        buf.write("\u012a\u0134\3\2\2\2\u012b\u012d\5s:\2\u012c\u012e\t\2")
        buf.write("\2\2\u012d\u012c\3\2\2\2\u012d\u012e\3\2\2\2\u012e\u0130")
        buf.write("\3\2\2\2\u012f\u0131\5i\65\2\u0130\u012f\3\2\2\2\u0131")
        buf.write("\u0132\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2")
        buf.write("\u0133\u0135\3\2\2\2\u0134\u012b\3\2\2\2\u0134\u0135\3")
        buf.write("\2\2\2\u0135\u0148\3\2\2\2\u0136\u0138\7\60\2\2\u0137")
        buf.write("\u0139\5i\65\2\u0138\u0137\3\2\2\2\u0139\u013a\3\2\2\2")
        buf.write("\u013a\u0138\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u0145\3")
        buf.write("\2\2\2\u013c\u013e\5s:\2\u013d\u013f\t\2\2\2\u013e\u013d")
        buf.write("\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0141\3\2\2\2\u0140")
        buf.write("\u0142\5i\65\2\u0141\u0140\3\2\2\2\u0142\u0143\3\2\2\2")
        buf.write("\u0143\u0141\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0146\3")
        buf.write("\2\2\2\u0145\u013c\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0148")
        buf.write("\3\2\2\2\u0147\u011e\3\2\2\2\u0147\u0136\3\2\2\2\u0148")
        buf.write("T\3\2\2\2\u0149\u014a\5W,\2\u014aV\3\2\2\2\u014b\u0151")
        buf.write("\7$\2\2\u014c\u014d\7^\2\2\u014d\u0150\7$\2\2\u014e\u0150")
        buf.write("\n\3\2\2\u014f\u014c\3\2\2\2\u014f\u014e\3\2\2\2\u0150")
        buf.write("\u0153\3\2\2\2\u0151\u014f\3\2\2\2\u0151\u0152\3\2\2\2")
        buf.write("\u0152\u0154\3\2\2\2\u0153\u0151\3\2\2\2\u0154\u0155\7")
        buf.write("$\2\2\u0155X\3\2\2\2\u0156\u015c\7$\2\2\u0157\u0158\7")
        buf.write("$\2\2\u0158\u015b\7$\2\2\u0159\u015b\n\3\2\2\u015a\u0157")
        buf.write("\3\2\2\2\u015a\u0159\3\2\2\2\u015b\u015e\3\2\2\2\u015c")
        buf.write("\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015f\3\2\2\2")
        buf.write("\u015e\u015c\3\2\2\2\u015f\u0160\7$\2\2\u0160Z\3\2\2\2")
        buf.write("\u0161\u0162\5]/\2\u0162\\\3\2\2\2\u0163\u0169\7)\2\2")
        buf.write("\u0164\u0165\7^\2\2\u0165\u0168\7)\2\2\u0166\u0168\n\4")
        buf.write("\2\2\u0167\u0164\3\2\2\2\u0167\u0166\3\2\2\2\u0168\u016b")
        buf.write("\3\2\2\2\u0169\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a")
        buf.write("\u016c\3\2\2\2\u016b\u0169\3\2\2\2\u016c\u016d\7)\2\2")
        buf.write("\u016d^\3\2\2\2\u016e\u0174\7)\2\2\u016f\u0170\7)\2\2")
        buf.write("\u0170\u0173\7)\2\2\u0171\u0173\n\4\2\2\u0172\u016f\3")
        buf.write("\2\2\2\u0172\u0171\3\2\2\2\u0173\u0176\3\2\2\2\u0174\u0172")
        buf.write("\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0177\3\2\2\2\u0176")
        buf.write("\u0174\3\2\2\2\u0177\u0178\7)\2\2\u0178`\3\2\2\2\u0179")
        buf.write("\u017a\7/\2\2\u017a\u017f\7/\2\2\u017b\u017c\7\61\2\2")
        buf.write("\u017c\u017f\7\61\2\2\u017d\u017f\7%\2\2\u017e\u0179\3")
        buf.write("\2\2\2\u017e\u017b\3\2\2\2\u017e\u017d\3\2\2\2\u017f\u0183")
        buf.write("\3\2\2\2\u0180\u0182\n\5\2\2\u0181\u0180\3\2\2\2\u0182")
        buf.write("\u0185\3\2\2\2\u0183\u0181\3\2\2\2\u0183\u0184\3\2\2\2")
        buf.write("\u0184\u0186\3\2\2\2\u0185\u0183\3\2\2\2\u0186\u0187\b")
        buf.write("\61\2\2\u0187b\3\2\2\2\u0188\u0189\7\61\2\2\u0189\u018a")
        buf.write("\7,\2\2\u018a\u018e\3\2\2\2\u018b\u018d\13\2\2\2\u018c")
        buf.write("\u018b\3\2\2\2\u018d\u0190\3\2\2\2\u018e\u018f\3\2\2\2")
        buf.write("\u018e\u018c\3\2\2\2\u018f\u0194\3\2\2\2\u0190\u018e\3")
        buf.write("\2\2\2\u0191\u0192\7,\2\2\u0192\u0195\7\61\2\2\u0193\u0195")
        buf.write("\7\2\2\3\u0194\u0191\3\2\2\2\u0194\u0193\3\2\2\2\u0195")
        buf.write("\u0196\3\2\2\2\u0196\u0197\b\62\2\2\u0197d\3\2\2\2\u0198")
        buf.write("\u0199\t\6\2\2\u0199\u019a\3\2\2\2\u019a\u019b\b\63\2")
        buf.write("\2\u019bf\3\2\2\2\u019c\u01a0\t\7\2\2\u019d\u019f\t\b")
        buf.write("\2\2\u019e\u019d\3\2\2\2\u019f\u01a2\3\2\2\2\u01a0\u019e")
        buf.write("\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1h\3\2\2\2\u01a2\u01a0")
        buf.write("\3\2\2\2\u01a3\u01a4\t\t\2\2\u01a4j\3\2\2\2\u01a5\u01a6")
        buf.write("\t\n\2\2\u01a6l\3\2\2\2\u01a7\u01a8\t\13\2\2\u01a8n\3")
        buf.write("\2\2\2\u01a9\u01aa\t\f\2\2\u01aap\3\2\2\2\u01ab\u01ac")
        buf.write("\t\r\2\2\u01acr\3\2\2\2\u01ad\u01ae\t\16\2\2\u01aet\3")
        buf.write("\2\2\2\u01af\u01b0\t\17\2\2\u01b0v\3\2\2\2\u01b1\u01b2")
        buf.write("\t\20\2\2\u01b2x\3\2\2\2\u01b3\u01b4\t\21\2\2\u01b4z\3")
        buf.write("\2\2\2\u01b5\u01b6\t\22\2\2\u01b6|\3\2\2\2\u01b7\u01b8")
        buf.write("\t\23\2\2\u01b8~\3\2\2\2\u01b9\u01ba\t\24\2\2\u01ba\u0080")
        buf.write("\3\2\2\2\u01bb\u01bc\t\25\2\2\u01bc\u0082\3\2\2\2\u01bd")
        buf.write("\u01be\t\26\2\2\u01be\u0084\3\2\2\2\u01bf\u01c0\t\27\2")
        buf.write("\2\u01c0\u0086\3\2\2\2\u01c1\u01c2\t\30\2\2\u01c2\u0088")
        buf.write("\3\2\2\2\u01c3\u01c4\t\31\2\2\u01c4\u008a\3\2\2\2\u01c5")
        buf.write("\u01c6\t\32\2\2\u01c6\u008c\3\2\2\2\u01c7\u01c8\t\33\2")
        buf.write("\2\u01c8\u008e\3\2\2\2\u01c9\u01ca\t\34\2\2\u01ca\u0090")
        buf.write("\3\2\2\2\u01cb\u01cc\t\35\2\2\u01cc\u0092\3\2\2\2\u01cd")
        buf.write("\u01ce\t\36\2\2\u01ce\u0094\3\2\2\2\u01cf\u01d0\t\37\2")
        buf.write("\2\u01d0\u0096\3\2\2\2\u01d1\u01d2\t \2\2\u01d2\u0098")
        buf.write("\3\2\2\2\u01d3\u01d4\t!\2\2\u01d4\u009a\3\2\2\2\u01d5")
        buf.write("\u01d6\t\"\2\2\u01d6\u009c\3\2\2\2\u01d7\u01d8\t#\2\2")
        buf.write("\u01d8\u009e\3\2\2\2\33\2\u0120\u0126\u0129\u012d\u0132")
        buf.write("\u0134\u013a\u013e\u0143\u0145\u0147\u014f\u0151\u015a")
        buf.write("\u015c\u0167\u0169\u0172\u0174\u017e\u0183\u018e\u0194")
        buf.write("\u01a0\3\2\3\2")
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
    K_IN = 32
    K_IS = 33
    K_ISNULL = 34
    K_LIKE = 35
    K_NOT = 36
    K_NOTNULL = 37
    K_NULL = 38
    K_OR = 39
    K_TRUE = 40
    NUMERIC_LITERAL = 41
    DOUBLE_QUOTED_STRING = 42
    DOUBLE_QUOTED_STRING_TEL = 43
    DOUBLE_QUOTED_STRING_SQL = 44
    SINGLE_QUOTED_STRING = 45
    SINGLE_QUOTED_STRING_TEL = 46
    SINGLE_QUOTED_STRING_SQL = 47
    SINGLE_LINE_COMMENT = 48
    MULTILINE_COMMENT = 49
    SPACES = 50
    WORD = 51

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
            "K_AND", "K_BETWEEN", "K_FALSE", "K_IN", "K_IS", "K_ISNULL", 
            "K_LIKE", "K_NOT", "K_NOTNULL", "K_NULL", "K_OR", "K_TRUE", 
            "NUMERIC_LITERAL", "DOUBLE_QUOTED_STRING", "DOUBLE_QUOTED_STRING_TEL", 
            "DOUBLE_QUOTED_STRING_SQL", "SINGLE_QUOTED_STRING", "SINGLE_QUOTED_STRING_TEL", 
            "SINGLE_QUOTED_STRING_SQL", "SINGLE_LINE_COMMENT", "MULTILINE_COMMENT", 
            "SPACES", "WORD" ]

    ruleNames = [ "AND", "EQ", "GT_EQ", "LT_EQ", "NOT_EQ1", "NOT_EQ2", "OR", 
                  "SHIFT_LEFT", "SHIFT_RIGHT", "AMP", "ASSIGN", "CLOSE_PAREN", 
                  "COLON", "COMMA", "DOT", "FORWARD_SLASH", "GT", "LT", 
                  "MINUS", "MOD", "OPEN_PAREN", "PIPE", "PLUS", "QUESTION_MARK", 
                  "SCOL", "STAR", "TILDE", "UNDER", "K_AND", "K_BETWEEN", 
                  "K_FALSE", "K_IN", "K_IS", "K_ISNULL", "K_LIKE", "K_NOT", 
                  "K_NOTNULL", "K_NULL", "K_OR", "K_TRUE", "NUMERIC_LITERAL", 
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



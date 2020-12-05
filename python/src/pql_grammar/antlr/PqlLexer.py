# Generated from grammar/PqlLexer.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\63")
        buf.write("\u01ca\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17")
        buf.write("\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\6")
        buf.write("(\u0110\n(\r(\16(\u0111\3(\3(\7(\u0116\n(\f(\16(\u0119")
        buf.write("\13(\5(\u011b\n(\3(\3(\5(\u011f\n(\3(\6(\u0122\n(\r(\16")
        buf.write("(\u0123\5(\u0126\n(\3(\3(\6(\u012a\n(\r(\16(\u012b\3(")
        buf.write("\3(\5(\u0130\n(\3(\6(\u0133\n(\r(\16(\u0134\5(\u0137\n")
        buf.write("(\5(\u0139\n(\3)\3)\3*\3*\3*\3*\7*\u0141\n*\f*\16*\u0144")
        buf.write("\13*\3*\3*\3+\3+\3+\3+\7+\u014c\n+\f+\16+\u014f\13+\3")
        buf.write("+\3+\3,\3,\3-\3-\3-\3-\7-\u0159\n-\f-\16-\u015c\13-\3")
        buf.write("-\3-\3.\3.\3.\3.\7.\u0164\n.\f.\16.\u0167\13.\3.\3.\3")
        buf.write("/\3/\3/\3/\3/\5/\u0170\n/\3/\7/\u0173\n/\f/\16/\u0176")
        buf.write("\13/\3/\3/\3\60\3\60\3\60\3\60\7\60\u017e\n\60\f\60\16")
        buf.write("\60\u0181\13\60\3\60\3\60\3\60\5\60\u0186\n\60\3\60\3")
        buf.write("\60\3\61\3\61\3\61\3\61\3\62\3\62\7\62\u0190\n\62\f\62")
        buf.write("\16\62\u0193\13\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3")
        buf.write(">\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3")
        buf.write("G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3L\3M\3M\3\u017f\2N\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\2g\2i\2k\2m\2o\2q\2s\2u\2")
        buf.write("w\2y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089")
        buf.write("\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095\2\u0097")
        buf.write("\2\u0099\2\3\2$\4\2--//\3\2$$\3\2))\4\2\f\f\17\17\5\2")
        buf.write("\13\r\17\17\"\"\5\2C\\aac|\6\2\62;C\\aac|\3\2\62;\4\2")
        buf.write("CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4")
        buf.write("\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPp")
        buf.write("p\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2")
        buf.write("WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\2\u01c7")
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
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\3\u009b\3\2\2\2")
        buf.write("\5\u009e\3\2\2\2\7\u00a1\3\2\2\2\t\u00a4\3\2\2\2\13\u00a7")
        buf.write("\3\2\2\2\r\u00aa\3\2\2\2\17\u00ad\3\2\2\2\21\u00b0\3\2")
        buf.write("\2\2\23\u00b3\3\2\2\2\25\u00b6\3\2\2\2\27\u00b8\3\2\2")
        buf.write("\2\31\u00ba\3\2\2\2\33\u00bc\3\2\2\2\35\u00be\3\2\2\2")
        buf.write("\37\u00c0\3\2\2\2!\u00c2\3\2\2\2#\u00c4\3\2\2\2%\u00c6")
        buf.write("\3\2\2\2\'\u00c8\3\2\2\2)\u00ca\3\2\2\2+\u00cc\3\2\2\2")
        buf.write("-\u00ce\3\2\2\2/\u00d0\3\2\2\2\61\u00d2\3\2\2\2\63\u00d4")
        buf.write("\3\2\2\2\65\u00d6\3\2\2\2\67\u00d8\3\2\2\29\u00da\3\2")
        buf.write("\2\2;\u00dc\3\2\2\2=\u00e0\3\2\2\2?\u00e6\3\2\2\2A\u00e9")
        buf.write("\3\2\2\2C\u00f0\3\2\2\2E\u00f5\3\2\2\2G\u00f9\3\2\2\2")
        buf.write("I\u0101\3\2\2\2K\u0106\3\2\2\2M\u0109\3\2\2\2O\u0138\3")
        buf.write("\2\2\2Q\u013a\3\2\2\2S\u013c\3\2\2\2U\u0147\3\2\2\2W\u0152")
        buf.write("\3\2\2\2Y\u0154\3\2\2\2[\u015f\3\2\2\2]\u016f\3\2\2\2")
        buf.write("_\u0179\3\2\2\2a\u0189\3\2\2\2c\u018d\3\2\2\2e\u0194\3")
        buf.write("\2\2\2g\u0196\3\2\2\2i\u0198\3\2\2\2k\u019a\3\2\2\2m\u019c")
        buf.write("\3\2\2\2o\u019e\3\2\2\2q\u01a0\3\2\2\2s\u01a2\3\2\2\2")
        buf.write("u\u01a4\3\2\2\2w\u01a6\3\2\2\2y\u01a8\3\2\2\2{\u01aa\3")
        buf.write("\2\2\2}\u01ac\3\2\2\2\177\u01ae\3\2\2\2\u0081\u01b0\3")
        buf.write("\2\2\2\u0083\u01b2\3\2\2\2\u0085\u01b4\3\2\2\2\u0087\u01b6")
        buf.write("\3\2\2\2\u0089\u01b8\3\2\2\2\u008b\u01ba\3\2\2\2\u008d")
        buf.write("\u01bc\3\2\2\2\u008f\u01be\3\2\2\2\u0091\u01c0\3\2\2\2")
        buf.write("\u0093\u01c2\3\2\2\2\u0095\u01c4\3\2\2\2\u0097\u01c6\3")
        buf.write("\2\2\2\u0099\u01c8\3\2\2\2\u009b\u009c\7(\2\2\u009c\u009d")
        buf.write("\7(\2\2\u009d\4\3\2\2\2\u009e\u009f\7?\2\2\u009f\u00a0")
        buf.write("\7?\2\2\u00a0\6\3\2\2\2\u00a1\u00a2\7@\2\2\u00a2\u00a3")
        buf.write("\7?\2\2\u00a3\b\3\2\2\2\u00a4\u00a5\7>\2\2\u00a5\u00a6")
        buf.write("\7?\2\2\u00a6\n\3\2\2\2\u00a7\u00a8\7#\2\2\u00a8\u00a9")
        buf.write("\7?\2\2\u00a9\f\3\2\2\2\u00aa\u00ab\7>\2\2\u00ab\u00ac")
        buf.write("\7@\2\2\u00ac\16\3\2\2\2\u00ad\u00ae\7~\2\2\u00ae\u00af")
        buf.write("\7~\2\2\u00af\20\3\2\2\2\u00b0\u00b1\7>\2\2\u00b1\u00b2")
        buf.write("\7>\2\2\u00b2\22\3\2\2\2\u00b3\u00b4\7@\2\2\u00b4\u00b5")
        buf.write("\7@\2\2\u00b5\24\3\2\2\2\u00b6\u00b7\7(\2\2\u00b7\26\3")
        buf.write("\2\2\2\u00b8\u00b9\7?\2\2\u00b9\30\3\2\2\2\u00ba\u00bb")
        buf.write("\7+\2\2\u00bb\32\3\2\2\2\u00bc\u00bd\7<\2\2\u00bd\34\3")
        buf.write("\2\2\2\u00be\u00bf\7.\2\2\u00bf\36\3\2\2\2\u00c0\u00c1")
        buf.write("\7\60\2\2\u00c1 \3\2\2\2\u00c2\u00c3\7\61\2\2\u00c3\"")
        buf.write("\3\2\2\2\u00c4\u00c5\7@\2\2\u00c5$\3\2\2\2\u00c6\u00c7")
        buf.write("\7>\2\2\u00c7&\3\2\2\2\u00c8\u00c9\7/\2\2\u00c9(\3\2\2")
        buf.write("\2\u00ca\u00cb\7\'\2\2\u00cb*\3\2\2\2\u00cc\u00cd\7*\2")
        buf.write("\2\u00cd,\3\2\2\2\u00ce\u00cf\7~\2\2\u00cf.\3\2\2\2\u00d0")
        buf.write("\u00d1\7-\2\2\u00d1\60\3\2\2\2\u00d2\u00d3\7A\2\2\u00d3")
        buf.write("\62\3\2\2\2\u00d4\u00d5\7=\2\2\u00d5\64\3\2\2\2\u00d6")
        buf.write("\u00d7\7,\2\2\u00d7\66\3\2\2\2\u00d8\u00d9\7\u0080\2\2")
        buf.write("\u00d98\3\2\2\2\u00da\u00db\7a\2\2\u00db:\3\2\2\2\u00dc")
        buf.write("\u00dd\5g\64\2\u00dd\u00de\5\u0081A\2\u00de\u00df\5m\67")
        buf.write("\2\u00df<\3\2\2\2\u00e0\u00e1\5q9\2\u00e1\u00e2\5g\64")
        buf.write("\2\u00e2\u00e3\5}?\2\u00e3\u00e4\5\u008bF\2\u00e4\u00e5")
        buf.write("\5o8\2\u00e5>\3\2\2\2\u00e6\u00e7\5w<\2\u00e7\u00e8\5")
        buf.write("\u008bF\2\u00e8@\3\2\2\2\u00e9\u00ea\5w<\2\u00ea\u00eb")
        buf.write("\5\u008bF\2\u00eb\u00ec\5\u0081A\2\u00ec\u00ed\5\u008f")
        buf.write("H\2\u00ed\u00ee\5}?\2\u00ee\u00ef\5}?\2\u00efB\3\2\2\2")
        buf.write("\u00f0\u00f1\5}?\2\u00f1\u00f2\5w<\2\u00f2\u00f3\5{>\2")
        buf.write("\u00f3\u00f4\5o8\2\u00f4D\3\2\2\2\u00f5\u00f6\5\u0081")
        buf.write("A\2\u00f6\u00f7\5\u0083B\2\u00f7\u00f8\5\u008dG\2\u00f8")
        buf.write("F\3\2\2\2\u00f9\u00fa\5\u0081A\2\u00fa\u00fb\5\u0083B")
        buf.write("\2\u00fb\u00fc\5\u008dG\2\u00fc\u00fd\5\u0081A\2\u00fd")
        buf.write("\u00fe\5\u008fH\2\u00fe\u00ff\5}?\2\u00ff\u0100\5}?\2")
        buf.write("\u0100H\3\2\2\2\u0101\u0102\5\u0081A\2\u0102\u0103\5\u008f")
        buf.write("H\2\u0103\u0104\5}?\2\u0104\u0105\5}?\2\u0105J\3\2\2\2")
        buf.write("\u0106\u0107\5\u0083B\2\u0107\u0108\5\u0089E\2\u0108L")
        buf.write("\3\2\2\2\u0109\u010a\5\u008dG\2\u010a\u010b\5\u0089E\2")
        buf.write("\u010b\u010c\5\u008fH\2\u010c\u010d\5o8\2\u010dN\3\2\2")
        buf.write("\2\u010e\u0110\5e\63\2\u010f\u010e\3\2\2\2\u0110\u0111")
        buf.write("\3\2\2\2\u0111\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112")
        buf.write("\u011a\3\2\2\2\u0113\u0117\7\60\2\2\u0114\u0116\5e\63")
        buf.write("\2\u0115\u0114\3\2\2\2\u0116\u0119\3\2\2\2\u0117\u0115")
        buf.write("\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u011b\3\2\2\2\u0119")
        buf.write("\u0117\3\2\2\2\u011a\u0113\3\2\2\2\u011a\u011b\3\2\2\2")
        buf.write("\u011b\u0125\3\2\2\2\u011c\u011e\5o8\2\u011d\u011f\t\2")
        buf.write("\2\2\u011e\u011d\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0121")
        buf.write("\3\2\2\2\u0120\u0122\5e\63\2\u0121\u0120\3\2\2\2\u0122")
        buf.write("\u0123\3\2\2\2\u0123\u0121\3\2\2\2\u0123\u0124\3\2\2\2")
        buf.write("\u0124\u0126\3\2\2\2\u0125\u011c\3\2\2\2\u0125\u0126\3")
        buf.write("\2\2\2\u0126\u0139\3\2\2\2\u0127\u0129\7\60\2\2\u0128")
        buf.write("\u012a\5e\63\2\u0129\u0128\3\2\2\2\u012a\u012b\3\2\2\2")
        buf.write("\u012b\u0129\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u0136\3")
        buf.write("\2\2\2\u012d\u012f\5o8\2\u012e\u0130\t\2\2\2\u012f\u012e")
        buf.write("\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u0132\3\2\2\2\u0131")
        buf.write("\u0133\5e\63\2\u0132\u0131\3\2\2\2\u0133\u0134\3\2\2\2")
        buf.write("\u0134\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0137\3")
        buf.write("\2\2\2\u0136\u012d\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0139")
        buf.write("\3\2\2\2\u0138\u010f\3\2\2\2\u0138\u0127\3\2\2\2\u0139")
        buf.write("P\3\2\2\2\u013a\u013b\5S*\2\u013bR\3\2\2\2\u013c\u0142")
        buf.write("\7$\2\2\u013d\u013e\7^\2\2\u013e\u0141\7$\2\2\u013f\u0141")
        buf.write("\n\3\2\2\u0140\u013d\3\2\2\2\u0140\u013f\3\2\2\2\u0141")
        buf.write("\u0144\3\2\2\2\u0142\u0140\3\2\2\2\u0142\u0143\3\2\2\2")
        buf.write("\u0143\u0145\3\2\2\2\u0144\u0142\3\2\2\2\u0145\u0146\7")
        buf.write("$\2\2\u0146T\3\2\2\2\u0147\u014d\7$\2\2\u0148\u0149\7")
        buf.write("$\2\2\u0149\u014c\7$\2\2\u014a\u014c\n\3\2\2\u014b\u0148")
        buf.write("\3\2\2\2\u014b\u014a\3\2\2\2\u014c\u014f\3\2\2\2\u014d")
        buf.write("\u014b\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u0150\3\2\2\2")
        buf.write("\u014f\u014d\3\2\2\2\u0150\u0151\7$\2\2\u0151V\3\2\2\2")
        buf.write("\u0152\u0153\5Y-\2\u0153X\3\2\2\2\u0154\u015a\7)\2\2\u0155")
        buf.write("\u0156\7^\2\2\u0156\u0159\7)\2\2\u0157\u0159\n\4\2\2\u0158")
        buf.write("\u0155\3\2\2\2\u0158\u0157\3\2\2\2\u0159\u015c\3\2\2\2")
        buf.write("\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u015d\3")
        buf.write("\2\2\2\u015c\u015a\3\2\2\2\u015d\u015e\7)\2\2\u015eZ\3")
        buf.write("\2\2\2\u015f\u0165\7)\2\2\u0160\u0161\7)\2\2\u0161\u0164")
        buf.write("\7)\2\2\u0162\u0164\n\4\2\2\u0163\u0160\3\2\2\2\u0163")
        buf.write("\u0162\3\2\2\2\u0164\u0167\3\2\2\2\u0165\u0163\3\2\2\2")
        buf.write("\u0165\u0166\3\2\2\2\u0166\u0168\3\2\2\2\u0167\u0165\3")
        buf.write("\2\2\2\u0168\u0169\7)\2\2\u0169\\\3\2\2\2\u016a\u016b")
        buf.write("\7/\2\2\u016b\u0170\7/\2\2\u016c\u016d\7\61\2\2\u016d")
        buf.write("\u0170\7\61\2\2\u016e\u0170\7%\2\2\u016f\u016a\3\2\2\2")
        buf.write("\u016f\u016c\3\2\2\2\u016f\u016e\3\2\2\2\u0170\u0174\3")
        buf.write("\2\2\2\u0171\u0173\n\5\2\2\u0172\u0171\3\2\2\2\u0173\u0176")
        buf.write("\3\2\2\2\u0174\u0172\3\2\2\2\u0174\u0175\3\2\2\2\u0175")
        buf.write("\u0177\3\2\2\2\u0176\u0174\3\2\2\2\u0177\u0178\b/\2\2")
        buf.write("\u0178^\3\2\2\2\u0179\u017a\7\61\2\2\u017a\u017b\7,\2")
        buf.write("\2\u017b\u017f\3\2\2\2\u017c\u017e\13\2\2\2\u017d\u017c")
        buf.write("\3\2\2\2\u017e\u0181\3\2\2\2\u017f\u0180\3\2\2\2\u017f")
        buf.write("\u017d\3\2\2\2\u0180\u0185\3\2\2\2\u0181\u017f\3\2\2\2")
        buf.write("\u0182\u0183\7,\2\2\u0183\u0186\7\61\2\2\u0184\u0186\7")
        buf.write("\2\2\3\u0185\u0182\3\2\2\2\u0185\u0184\3\2\2\2\u0186\u0187")
        buf.write("\3\2\2\2\u0187\u0188\b\60\2\2\u0188`\3\2\2\2\u0189\u018a")
        buf.write("\t\6\2\2\u018a\u018b\3\2\2\2\u018b\u018c\b\61\2\2\u018c")
        buf.write("b\3\2\2\2\u018d\u0191\t\7\2\2\u018e\u0190\t\b\2\2\u018f")
        buf.write("\u018e\3\2\2\2\u0190\u0193\3\2\2\2\u0191\u018f\3\2\2\2")
        buf.write("\u0191\u0192\3\2\2\2\u0192d\3\2\2\2\u0193\u0191\3\2\2")
        buf.write("\2\u0194\u0195\t\t\2\2\u0195f\3\2\2\2\u0196\u0197\t\n")
        buf.write("\2\2\u0197h\3\2\2\2\u0198\u0199\t\13\2\2\u0199j\3\2\2")
        buf.write("\2\u019a\u019b\t\f\2\2\u019bl\3\2\2\2\u019c\u019d\t\r")
        buf.write("\2\2\u019dn\3\2\2\2\u019e\u019f\t\16\2\2\u019fp\3\2\2")
        buf.write("\2\u01a0\u01a1\t\17\2\2\u01a1r\3\2\2\2\u01a2\u01a3\t\20")
        buf.write("\2\2\u01a3t\3\2\2\2\u01a4\u01a5\t\21\2\2\u01a5v\3\2\2")
        buf.write("\2\u01a6\u01a7\t\22\2\2\u01a7x\3\2\2\2\u01a8\u01a9\t\23")
        buf.write("\2\2\u01a9z\3\2\2\2\u01aa\u01ab\t\24\2\2\u01ab|\3\2\2")
        buf.write("\2\u01ac\u01ad\t\25\2\2\u01ad~\3\2\2\2\u01ae\u01af\t\26")
        buf.write("\2\2\u01af\u0080\3\2\2\2\u01b0\u01b1\t\27\2\2\u01b1\u0082")
        buf.write("\3\2\2\2\u01b2\u01b3\t\30\2\2\u01b3\u0084\3\2\2\2\u01b4")
        buf.write("\u01b5\t\31\2\2\u01b5\u0086\3\2\2\2\u01b6\u01b7\t\32\2")
        buf.write("\2\u01b7\u0088\3\2\2\2\u01b8\u01b9\t\33\2\2\u01b9\u008a")
        buf.write("\3\2\2\2\u01ba\u01bb\t\34\2\2\u01bb\u008c\3\2\2\2\u01bc")
        buf.write("\u01bd\t\35\2\2\u01bd\u008e\3\2\2\2\u01be\u01bf\t\36\2")
        buf.write("\2\u01bf\u0090\3\2\2\2\u01c0\u01c1\t\37\2\2\u01c1\u0092")
        buf.write("\3\2\2\2\u01c2\u01c3\t \2\2\u01c3\u0094\3\2\2\2\u01c4")
        buf.write("\u01c5\t!\2\2\u01c5\u0096\3\2\2\2\u01c6\u01c7\t\"\2\2")
        buf.write("\u01c7\u0098\3\2\2\2\u01c8\u01c9\t#\2\2\u01c9\u009a\3")
        buf.write("\2\2\2\33\2\u0111\u0117\u011a\u011e\u0123\u0125\u012b")
        buf.write("\u012f\u0134\u0136\u0138\u0140\u0142\u014b\u014d\u0158")
        buf.write("\u015a\u0163\u0165\u016f\u0174\u017f\u0185\u0191\3\2\3")
        buf.write("\2")
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
    K_FALSE = 30
    K_IS = 31
    K_ISNULL = 32
    K_LIKE = 33
    K_NOT = 34
    K_NOTNULL = 35
    K_NULL = 36
    K_OR = 37
    K_TRUE = 38
    NUMERIC_LITERAL = 39
    DOUBLE_QUOTED_STRING = 40
    DOUBLE_QUOTED_STRING_TEL = 41
    DOUBLE_QUOTED_STRING_SQL = 42
    SINGLE_QUOTED_STRING = 43
    SINGLE_QUOTED_STRING_TEL = 44
    SINGLE_QUOTED_STRING_SQL = 45
    SINGLE_LINE_COMMENT = 46
    MULTILINE_COMMENT = 47
    SPACES = 48
    WORD = 49

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
            "K_AND", "K_FALSE", "K_IS", "K_ISNULL", "K_LIKE", "K_NOT", "K_NOTNULL", 
            "K_NULL", "K_OR", "K_TRUE", "NUMERIC_LITERAL", "DOUBLE_QUOTED_STRING", 
            "DOUBLE_QUOTED_STRING_TEL", "DOUBLE_QUOTED_STRING_SQL", "SINGLE_QUOTED_STRING", 
            "SINGLE_QUOTED_STRING_TEL", "SINGLE_QUOTED_STRING_SQL", "SINGLE_LINE_COMMENT", 
            "MULTILINE_COMMENT", "SPACES", "WORD" ]

    ruleNames = [ "AND", "EQ", "GT_EQ", "LT_EQ", "NOT_EQ1", "NOT_EQ2", "OR", 
                  "SHIFT_LEFT", "SHIFT_RIGHT", "AMP", "ASSIGN", "CLOSE_PAREN", 
                  "COLON", "COMMA", "DOT", "FORWARD_SLASH", "GT", "LT", 
                  "MINUS", "MOD", "OPEN_PAREN", "PIPE", "PLUS", "QUESTION_MARK", 
                  "SCOL", "STAR", "TILDE", "UNDER", "K_AND", "K_FALSE", 
                  "K_IS", "K_ISNULL", "K_LIKE", "K_NOT", "K_NOTNULL", "K_NULL", 
                  "K_OR", "K_TRUE", "NUMERIC_LITERAL", "DOUBLE_QUOTED_STRING", 
                  "DOUBLE_QUOTED_STRING_TEL", "DOUBLE_QUOTED_STRING_SQL", 
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



# Generated from grammar/PqlLexer.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2:")
        buf.write("\u01fd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20")
        buf.write("\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3")
        buf.write("&\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3)")
        buf.write("\3)\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3")
        buf.write(",\3,\3,\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3/\6/\u0143\n")
        buf.write("/\r/\16/\u0144\3/\3/\7/\u0149\n/\f/\16/\u014c\13/\5/\u014e")
        buf.write("\n/\3/\3/\5/\u0152\n/\3/\6/\u0155\n/\r/\16/\u0156\5/\u0159")
        buf.write("\n/\3/\3/\6/\u015d\n/\r/\16/\u015e\3/\3/\5/\u0163\n/\3")
        buf.write("/\6/\u0166\n/\r/\16/\u0167\5/\u016a\n/\5/\u016c\n/\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\61\7\61\u0174\n\61\f\61\16\61\u0177")
        buf.write("\13\61\3\61\3\61\3\62\3\62\3\62\3\62\7\62\u017f\n\62\f")
        buf.write("\62\16\62\u0182\13\62\3\62\3\62\3\63\3\63\3\64\3\64\3")
        buf.write("\64\3\64\7\64\u018c\n\64\f\64\16\64\u018f\13\64\3\64\3")
        buf.write("\64\3\65\3\65\3\65\3\65\7\65\u0197\n\65\f\65\16\65\u019a")
        buf.write("\13\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\5\66\u01a3\n")
        buf.write("\66\3\66\7\66\u01a6\n\66\f\66\16\66\u01a9\13\66\3\66\3")
        buf.write("\66\3\67\3\67\3\67\3\67\7\67\u01b1\n\67\f\67\16\67\u01b4")
        buf.write("\13\67\3\67\3\67\3\67\5\67\u01b9\n\67\3\67\3\67\38\38")
        buf.write("\38\38\39\39\79\u01c3\n9\f9\169\u01c6\139\3:\3:\3;\3;")
        buf.write("\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3")
        buf.write("D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3L\3M\3")
        buf.write("M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\3R\3S\3S\3T\3T\3\u01b2\2")
        buf.write("U\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s\2")
        buf.write("u\2w\2y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2")
        buf.write("\u0089\2\u008b\2\u008d\2\u008f\2\u0091\2\u0093\2\u0095")
        buf.write("\2\u0097\2\u0099\2\u009b\2\u009d\2\u009f\2\u00a1\2\u00a3")
        buf.write("\2\u00a5\2\u00a7\2\3\2$\4\2--//\3\2$$\3\2))\4\2\f\f\17")
        buf.write("\17\5\2\13\r\17\17\"\"\5\2C\\aac|\6\2\62;C\\aac|\3\2\62")
        buf.write(";\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHhh\4\2")
        buf.write("IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4")
        buf.write("\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVv")
        buf.write("v\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\2")
        buf.write("\u01fa\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2")
        buf.write("\2\2q\3\2\2\2\3\u00a9\3\2\2\2\5\u00ab\3\2\2\2\7\u00ad")
        buf.write("\3\2\2\2\t\u00b0\3\2\2\2\13\u00b3\3\2\2\2\r\u00b6\3\2")
        buf.write("\2\2\17\u00b9\3\2\2\2\21\u00bc\3\2\2\2\23\u00bf\3\2\2")
        buf.write("\2\25\u00c2\3\2\2\2\27\u00c5\3\2\2\2\31\u00c8\3\2\2\2")
        buf.write("\33\u00ca\3\2\2\2\35\u00cc\3\2\2\2\37\u00ce\3\2\2\2!\u00d0")
        buf.write("\3\2\2\2#\u00d2\3\2\2\2%\u00d4\3\2\2\2\'\u00d6\3\2\2\2")
        buf.write(")\u00d8\3\2\2\2+\u00da\3\2\2\2-\u00dc\3\2\2\2/\u00de\3")
        buf.write("\2\2\2\61\u00e0\3\2\2\2\63\u00e2\3\2\2\2\65\u00e4\3\2")
        buf.write("\2\2\67\u00e6\3\2\2\29\u00e8\3\2\2\2;\u00ea\3\2\2\2=\u00ee")
        buf.write("\3\2\2\2?\u00f2\3\2\2\2A\u00f5\3\2\2\2C\u00fa\3\2\2\2")
        buf.write("E\u0100\3\2\2\2G\u0103\3\2\2\2I\u010a\3\2\2\2K\u010f\3")
        buf.write("\2\2\2M\u0115\3\2\2\2O\u0119\3\2\2\2Q\u0121\3\2\2\2S\u0126")
        buf.write("\3\2\2\2U\u0129\3\2\2\2W\u012f\3\2\2\2Y\u0136\3\2\2\2")
        buf.write("[\u013b\3\2\2\2]\u016b\3\2\2\2_\u016d\3\2\2\2a\u016f\3")
        buf.write("\2\2\2c\u017a\3\2\2\2e\u0185\3\2\2\2g\u0187\3\2\2\2i\u0192")
        buf.write("\3\2\2\2k\u01a2\3\2\2\2m\u01ac\3\2\2\2o\u01bc\3\2\2\2")
        buf.write("q\u01c0\3\2\2\2s\u01c7\3\2\2\2u\u01c9\3\2\2\2w\u01cb\3")
        buf.write("\2\2\2y\u01cd\3\2\2\2{\u01cf\3\2\2\2}\u01d1\3\2\2\2\177")
        buf.write("\u01d3\3\2\2\2\u0081\u01d5\3\2\2\2\u0083\u01d7\3\2\2\2")
        buf.write("\u0085\u01d9\3\2\2\2\u0087\u01db\3\2\2\2\u0089\u01dd\3")
        buf.write("\2\2\2\u008b\u01df\3\2\2\2\u008d\u01e1\3\2\2\2\u008f\u01e3")
        buf.write("\3\2\2\2\u0091\u01e5\3\2\2\2\u0093\u01e7\3\2\2\2\u0095")
        buf.write("\u01e9\3\2\2\2\u0097\u01eb\3\2\2\2\u0099\u01ed\3\2\2\2")
        buf.write("\u009b\u01ef\3\2\2\2\u009d\u01f1\3\2\2\2\u009f\u01f3\3")
        buf.write("\2\2\2\u00a1\u01f5\3\2\2\2\u00a3\u01f7\3\2\2\2\u00a5\u01f9")
        buf.write("\3\2\2\2\u00a7\u01fb\3\2\2\2\u00a9\u00aa\7<\2\2\u00aa")
        buf.write("\4\3\2\2\2\u00ab\u00ac\7A\2\2\u00ac\6\3\2\2\2\u00ad\u00ae")
        buf.write("\7(\2\2\u00ae\u00af\7(\2\2\u00af\b\3\2\2\2\u00b0\u00b1")
        buf.write("\7?\2\2\u00b1\u00b2\7?\2\2\u00b2\n\3\2\2\2\u00b3\u00b4")
        buf.write("\7@\2\2\u00b4\u00b5\7?\2\2\u00b5\f\3\2\2\2\u00b6\u00b7")
        buf.write("\7>\2\2\u00b7\u00b8\7?\2\2\u00b8\16\3\2\2\2\u00b9\u00ba")
        buf.write("\7#\2\2\u00ba\u00bb\7?\2\2\u00bb\20\3\2\2\2\u00bc\u00bd")
        buf.write("\7>\2\2\u00bd\u00be\7@\2\2\u00be\22\3\2\2\2\u00bf\u00c0")
        buf.write("\7~\2\2\u00c0\u00c1\7~\2\2\u00c1\24\3\2\2\2\u00c2\u00c3")
        buf.write("\7>\2\2\u00c3\u00c4\7>\2\2\u00c4\26\3\2\2\2\u00c5\u00c6")
        buf.write("\7@\2\2\u00c6\u00c7\7@\2\2\u00c7\30\3\2\2\2\u00c8\u00c9")
        buf.write("\7(\2\2\u00c9\32\3\2\2\2\u00ca\u00cb\7?\2\2\u00cb\34\3")
        buf.write("\2\2\2\u00cc\u00cd\7+\2\2\u00cd\36\3\2\2\2\u00ce\u00cf")
        buf.write("\7.\2\2\u00cf \3\2\2\2\u00d0\u00d1\7\60\2\2\u00d1\"\3")
        buf.write("\2\2\2\u00d2\u00d3\7\61\2\2\u00d3$\3\2\2\2\u00d4\u00d5")
        buf.write("\7@\2\2\u00d5&\3\2\2\2\u00d6\u00d7\7>\2\2\u00d7(\3\2\2")
        buf.write("\2\u00d8\u00d9\7/\2\2\u00d9*\3\2\2\2\u00da\u00db\7\'\2")
        buf.write("\2\u00db,\3\2\2\2\u00dc\u00dd\7*\2\2\u00dd.\3\2\2\2\u00de")
        buf.write("\u00df\7~\2\2\u00df\60\3\2\2\2\u00e0\u00e1\7-\2\2\u00e1")
        buf.write("\62\3\2\2\2\u00e2\u00e3\7=\2\2\u00e3\64\3\2\2\2\u00e4")
        buf.write("\u00e5\7,\2\2\u00e5\66\3\2\2\2\u00e6\u00e7\7\u0080\2\2")
        buf.write("\u00e78\3\2\2\2\u00e8\u00e9\7a\2\2\u00e9:\3\2\2\2\u00ea")
        buf.write("\u00eb\5u;\2\u00eb\u00ec\5\u008fH\2\u00ec\u00ed\5{>\2")
        buf.write("\u00ed<\3\2\2\2\u00ee\u00ef\5u;\2\u00ef\u00f0\5\u0099")
        buf.write("M\2\u00f0\u00f1\5y=\2\u00f1>\3\2\2\2\u00f2\u00f3\5w<\2")
        buf.write("\u00f3\u00f4\5\u00a5S\2\u00f4@\3\2\2\2\u00f5\u00f6\5{")
        buf.write(">\2\u00f6\u00f7\5}?\2\u00f7\u00f8\5\u0099M\2\u00f8\u00f9")
        buf.write("\5y=\2\u00f9B\3\2\2\2\u00fa\u00fb\5\177@\2\u00fb\u00fc")
        buf.write("\5u;\2\u00fc\u00fd\5\u008bF\2\u00fd\u00fe\5\u0099M\2\u00fe")
        buf.write("\u00ff\5}?\2\u00ffD\3\2\2\2\u0100\u0101\5\u0085C\2\u0101")
        buf.write("\u0102\5\u0099M\2\u0102F\3\2\2\2\u0103\u0104\5\u0085C")
        buf.write("\2\u0104\u0105\5\u0099M\2\u0105\u0106\5\u008fH\2\u0106")
        buf.write("\u0107\5\u009dO\2\u0107\u0108\5\u008bF\2\u0108\u0109\5")
        buf.write("\u008bF\2\u0109H\3\2\2\2\u010a\u010b\5\u008bF\2\u010b")
        buf.write("\u010c\5\u0085C\2\u010c\u010d\5\u0089E\2\u010d\u010e\5")
        buf.write("}?\2\u010eJ\3\2\2\2\u010f\u0110\5\u008bF\2\u0110\u0111")
        buf.write("\5\u0085C\2\u0111\u0112\5\u008dG\2\u0112\u0113\5\u0085")
        buf.write("C\2\u0113\u0114\5\u009bN\2\u0114L\3\2\2\2\u0115\u0116")
        buf.write("\5\u008fH\2\u0116\u0117\5\u0091I\2\u0117\u0118\5\u009b")
        buf.write("N\2\u0118N\3\2\2\2\u0119\u011a\5\u008fH\2\u011a\u011b")
        buf.write("\5\u0091I\2\u011b\u011c\5\u009bN\2\u011c\u011d\5\u008f")
        buf.write("H\2\u011d\u011e\5\u009dO\2\u011e\u011f\5\u008bF\2\u011f")
        buf.write("\u0120\5\u008bF\2\u0120P\3\2\2\2\u0121\u0122\5\u008fH")
        buf.write("\2\u0122\u0123\5\u009dO\2\u0123\u0124\5\u008bF\2\u0124")
        buf.write("\u0125\5\u008bF\2\u0125R\3\2\2\2\u0126\u0127\5\u0091I")
        buf.write("\2\u0127\u0128\5\u0097L\2\u0128T\3\2\2\2\u0129\u012a\5")
        buf.write("\u0091I\2\u012a\u012b\5\u0097L\2\u012b\u012c\5{>\2\u012c")
        buf.write("\u012d\5}?\2\u012d\u012e\5\u0097L\2\u012eV\3\2\2\2\u012f")
        buf.write("\u0130\5\u0099M\2\u0130\u0131\5}?\2\u0131\u0132\5\u008b")
        buf.write("F\2\u0132\u0133\5}?\2\u0133\u0134\5y=\2\u0134\u0135\5")
        buf.write("\u009bN\2\u0135X\3\2\2\2\u0136\u0137\5\u009bN\2\u0137")
        buf.write("\u0138\5\u0097L\2\u0138\u0139\5\u009dO\2\u0139\u013a\5")
        buf.write("}?\2\u013aZ\3\2\2\2\u013b\u013c\5\u00a1Q\2\u013c\u013d")
        buf.write("\5\u0083B\2\u013d\u013e\5}?\2\u013e\u013f\5\u0097L\2\u013f")
        buf.write("\u0140\5}?\2\u0140\\\3\2\2\2\u0141\u0143\5s:\2\u0142\u0141")
        buf.write("\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0142\3\2\2\2\u0144")
        buf.write("\u0145\3\2\2\2\u0145\u014d\3\2\2\2\u0146\u014a\7\60\2")
        buf.write("\2\u0147\u0149\5s:\2\u0148\u0147\3\2\2\2\u0149\u014c\3")
        buf.write("\2\2\2\u014a\u0148\3\2\2\2\u014a\u014b\3\2\2\2\u014b\u014e")
        buf.write("\3\2\2\2\u014c\u014a\3\2\2\2\u014d\u0146\3\2\2\2\u014d")
        buf.write("\u014e\3\2\2\2\u014e\u0158\3\2\2\2\u014f\u0151\5}?\2\u0150")
        buf.write("\u0152\t\2\2\2\u0151\u0150\3\2\2\2\u0151\u0152\3\2\2\2")
        buf.write("\u0152\u0154\3\2\2\2\u0153\u0155\5s:\2\u0154\u0153\3\2")
        buf.write("\2\2\u0155\u0156\3\2\2\2\u0156\u0154\3\2\2\2\u0156\u0157")
        buf.write("\3\2\2\2\u0157\u0159\3\2\2\2\u0158\u014f\3\2\2\2\u0158")
        buf.write("\u0159\3\2\2\2\u0159\u016c\3\2\2\2\u015a\u015c\7\60\2")
        buf.write("\2\u015b\u015d\5s:\2\u015c\u015b\3\2\2\2\u015d\u015e\3")
        buf.write("\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2\u015f\u0169")
        buf.write("\3\2\2\2\u0160\u0162\5}?\2\u0161\u0163\t\2\2\2\u0162\u0161")
        buf.write("\3\2\2\2\u0162\u0163\3\2\2\2\u0163\u0165\3\2\2\2\u0164")
        buf.write("\u0166\5s:\2\u0165\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167")
        buf.write("\u0165\3\2\2\2\u0167\u0168\3\2\2\2\u0168\u016a\3\2\2\2")
        buf.write("\u0169\u0160\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016c\3")
        buf.write("\2\2\2\u016b\u0142\3\2\2\2\u016b\u015a\3\2\2\2\u016c^")
        buf.write("\3\2\2\2\u016d\u016e\5a\61\2\u016e`\3\2\2\2\u016f\u0175")
        buf.write("\7$\2\2\u0170\u0171\7^\2\2\u0171\u0174\7$\2\2\u0172\u0174")
        buf.write("\n\3\2\2\u0173\u0170\3\2\2\2\u0173\u0172\3\2\2\2\u0174")
        buf.write("\u0177\3\2\2\2\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2")
        buf.write("\u0176\u0178\3\2\2\2\u0177\u0175\3\2\2\2\u0178\u0179\7")
        buf.write("$\2\2\u0179b\3\2\2\2\u017a\u0180\7$\2\2\u017b\u017c\7")
        buf.write("$\2\2\u017c\u017f\7$\2\2\u017d\u017f\n\3\2\2\u017e\u017b")
        buf.write("\3\2\2\2\u017e\u017d\3\2\2\2\u017f\u0182\3\2\2\2\u0180")
        buf.write("\u017e\3\2\2\2\u0180\u0181\3\2\2\2\u0181\u0183\3\2\2\2")
        buf.write("\u0182\u0180\3\2\2\2\u0183\u0184\7$\2\2\u0184d\3\2\2\2")
        buf.write("\u0185\u0186\5g\64\2\u0186f\3\2\2\2\u0187\u018d\7)\2\2")
        buf.write("\u0188\u0189\7^\2\2\u0189\u018c\7)\2\2\u018a\u018c\n\4")
        buf.write("\2\2\u018b\u0188\3\2\2\2\u018b\u018a\3\2\2\2\u018c\u018f")
        buf.write("\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e")
        buf.write("\u0190\3\2\2\2\u018f\u018d\3\2\2\2\u0190\u0191\7)\2\2")
        buf.write("\u0191h\3\2\2\2\u0192\u0198\7)\2\2\u0193\u0194\7)\2\2")
        buf.write("\u0194\u0197\7)\2\2\u0195\u0197\n\4\2\2\u0196\u0193\3")
        buf.write("\2\2\2\u0196\u0195\3\2\2\2\u0197\u019a\3\2\2\2\u0198\u0196")
        buf.write("\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u019b\3\2\2\2\u019a")
        buf.write("\u0198\3\2\2\2\u019b\u019c\7)\2\2\u019cj\3\2\2\2\u019d")
        buf.write("\u019e\7/\2\2\u019e\u01a3\7/\2\2\u019f\u01a0\7\61\2\2")
        buf.write("\u01a0\u01a3\7\61\2\2\u01a1\u01a3\7%\2\2\u01a2\u019d\3")
        buf.write("\2\2\2\u01a2\u019f\3\2\2\2\u01a2\u01a1\3\2\2\2\u01a3\u01a7")
        buf.write("\3\2\2\2\u01a4\u01a6\n\5\2\2\u01a5\u01a4\3\2\2\2\u01a6")
        buf.write("\u01a9\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2")
        buf.write("\u01a8\u01aa\3\2\2\2\u01a9\u01a7\3\2\2\2\u01aa\u01ab\b")
        buf.write("\66\2\2\u01abl\3\2\2\2\u01ac\u01ad\7\61\2\2\u01ad\u01ae")
        buf.write("\7,\2\2\u01ae\u01b2\3\2\2\2\u01af\u01b1\13\2\2\2\u01b0")
        buf.write("\u01af\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b3\3\2\2\2")
        buf.write("\u01b2\u01b0\3\2\2\2\u01b3\u01b8\3\2\2\2\u01b4\u01b2\3")
        buf.write("\2\2\2\u01b5\u01b6\7,\2\2\u01b6\u01b9\7\61\2\2\u01b7\u01b9")
        buf.write("\7\2\2\3\u01b8\u01b5\3\2\2\2\u01b8\u01b7\3\2\2\2\u01b9")
        buf.write("\u01ba\3\2\2\2\u01ba\u01bb\b\67\2\2\u01bbn\3\2\2\2\u01bc")
        buf.write("\u01bd\t\6\2\2\u01bd\u01be\3\2\2\2\u01be\u01bf\b8\2\2")
        buf.write("\u01bfp\3\2\2\2\u01c0\u01c4\t\7\2\2\u01c1\u01c3\t\b\2")
        buf.write("\2\u01c2\u01c1\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4\u01c2")
        buf.write("\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5r\3\2\2\2\u01c6\u01c4")
        buf.write("\3\2\2\2\u01c7\u01c8\t\t\2\2\u01c8t\3\2\2\2\u01c9\u01ca")
        buf.write("\t\n\2\2\u01cav\3\2\2\2\u01cb\u01cc\t\13\2\2\u01ccx\3")
        buf.write("\2\2\2\u01cd\u01ce\t\f\2\2\u01cez\3\2\2\2\u01cf\u01d0")
        buf.write("\t\r\2\2\u01d0|\3\2\2\2\u01d1\u01d2\t\16\2\2\u01d2~\3")
        buf.write("\2\2\2\u01d3\u01d4\t\17\2\2\u01d4\u0080\3\2\2\2\u01d5")
        buf.write("\u01d6\t\20\2\2\u01d6\u0082\3\2\2\2\u01d7\u01d8\t\21\2")
        buf.write("\2\u01d8\u0084\3\2\2\2\u01d9\u01da\t\22\2\2\u01da\u0086")
        buf.write("\3\2\2\2\u01db\u01dc\t\23\2\2\u01dc\u0088\3\2\2\2\u01dd")
        buf.write("\u01de\t\24\2\2\u01de\u008a\3\2\2\2\u01df\u01e0\t\25\2")
        buf.write("\2\u01e0\u008c\3\2\2\2\u01e1\u01e2\t\26\2\2\u01e2\u008e")
        buf.write("\3\2\2\2\u01e3\u01e4\t\27\2\2\u01e4\u0090\3\2\2\2\u01e5")
        buf.write("\u01e6\t\30\2\2\u01e6\u0092\3\2\2\2\u01e7\u01e8\t\31\2")
        buf.write("\2\u01e8\u0094\3\2\2\2\u01e9\u01ea\t\32\2\2\u01ea\u0096")
        buf.write("\3\2\2\2\u01eb\u01ec\t\33\2\2\u01ec\u0098\3\2\2\2\u01ed")
        buf.write("\u01ee\t\34\2\2\u01ee\u009a\3\2\2\2\u01ef\u01f0\t\35\2")
        buf.write("\2\u01f0\u009c\3\2\2\2\u01f1\u01f2\t\36\2\2\u01f2\u009e")
        buf.write("\3\2\2\2\u01f3\u01f4\t\37\2\2\u01f4\u00a0\3\2\2\2\u01f5")
        buf.write("\u01f6\t \2\2\u01f6\u00a2\3\2\2\2\u01f7\u01f8\t!\2\2\u01f8")
        buf.write("\u00a4\3\2\2\2\u01f9\u01fa\t\"\2\2\u01fa\u00a6\3\2\2\2")
        buf.write("\u01fb\u01fc\t#\2\2\u01fc\u00a8\3\2\2\2\33\2\u0144\u014a")
        buf.write("\u014d\u0151\u0156\u0158\u015e\u0162\u0167\u0169\u016b")
        buf.write("\u0173\u0175\u017e\u0180\u018b\u018d\u0196\u0198\u01a2")
        buf.write("\u01a7\u01b2\u01b8\u01c4\3\2\3\2")
        return buf.getvalue()


class PqlLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TAXON_TAG_DELIMITER = 1
    TAXON_OPTIONAL_OPERATOR = 2
    AND = 3
    EQ = 4
    GT_EQ = 5
    LT_EQ = 6
    NOT_EQ1 = 7
    NOT_EQ2 = 8
    OR = 9
    SHIFT_LEFT = 10
    SHIFT_RIGHT = 11
    AMP = 12
    ASSIGN = 13
    CLOSE_PAREN = 14
    COMMA = 15
    DOT = 16
    FORWARD_SLASH = 17
    GT = 18
    LT = 19
    MINUS = 20
    MOD = 21
    OPEN_PAREN = 22
    PIPE = 23
    PLUS = 24
    SCOL = 25
    STAR = 26
    TILDE = 27
    UNDER = 28
    K_AND = 29
    K_ASC = 30
    K_BY = 31
    K_DESC = 32
    K_FALSE = 33
    K_IS = 34
    K_ISNULL = 35
    K_LIKE = 36
    K_LIMIT = 37
    K_NOT = 38
    K_NOTNULL = 39
    K_NULL = 40
    K_OR = 41
    K_ORDER = 42
    K_SELECT = 43
    K_TRUE = 44
    K_WHERE = 45
    NUMERIC_LITERAL = 46
    DOUBLE_QUOTED_STRING = 47
    DOUBLE_QUOTED_STRING_TEL = 48
    DOUBLE_QUOTED_STRING_SQL = 49
    SINGLE_QUOTED_STRING = 50
    SINGLE_QUOTED_STRING_TEL = 51
    SINGLE_QUOTED_STRING_SQL = 52
    SINGLE_LINE_COMMENT = 53
    MULTILINE_COMMENT = 54
    SPACES = 55
    WORD = 56

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':'", "'?'", "'&&'", "'=='", "'>='", "'<='", "'!='", "'<>'", 
            "'||'", "'<<'", "'>>'", "'&'", "'='", "')'", "','", "'.'", "'/'", 
            "'>'", "'<'", "'-'", "'%'", "'('", "'|'", "'+'", "';'", "'*'", 
            "'~'", "'_'" ]

    symbolicNames = [ "<INVALID>",
            "TAXON_TAG_DELIMITER", "TAXON_OPTIONAL_OPERATOR", "AND", "EQ", 
            "GT_EQ", "LT_EQ", "NOT_EQ1", "NOT_EQ2", "OR", "SHIFT_LEFT", 
            "SHIFT_RIGHT", "AMP", "ASSIGN", "CLOSE_PAREN", "COMMA", "DOT", 
            "FORWARD_SLASH", "GT", "LT", "MINUS", "MOD", "OPEN_PAREN", "PIPE", 
            "PLUS", "SCOL", "STAR", "TILDE", "UNDER", "K_AND", "K_ASC", 
            "K_BY", "K_DESC", "K_FALSE", "K_IS", "K_ISNULL", "K_LIKE", "K_LIMIT", 
            "K_NOT", "K_NOTNULL", "K_NULL", "K_OR", "K_ORDER", "K_SELECT", 
            "K_TRUE", "K_WHERE", "NUMERIC_LITERAL", "DOUBLE_QUOTED_STRING", 
            "DOUBLE_QUOTED_STRING_TEL", "DOUBLE_QUOTED_STRING_SQL", "SINGLE_QUOTED_STRING", 
            "SINGLE_QUOTED_STRING_TEL", "SINGLE_QUOTED_STRING_SQL", "SINGLE_LINE_COMMENT", 
            "MULTILINE_COMMENT", "SPACES", "WORD" ]

    ruleNames = [ "TAXON_TAG_DELIMITER", "TAXON_OPTIONAL_OPERATOR", "AND", 
                  "EQ", "GT_EQ", "LT_EQ", "NOT_EQ1", "NOT_EQ2", "OR", "SHIFT_LEFT", 
                  "SHIFT_RIGHT", "AMP", "ASSIGN", "CLOSE_PAREN", "COMMA", 
                  "DOT", "FORWARD_SLASH", "GT", "LT", "MINUS", "MOD", "OPEN_PAREN", 
                  "PIPE", "PLUS", "SCOL", "STAR", "TILDE", "UNDER", "K_AND", 
                  "K_ASC", "K_BY", "K_DESC", "K_FALSE", "K_IS", "K_ISNULL", 
                  "K_LIKE", "K_LIMIT", "K_NOT", "K_NOTNULL", "K_NULL", "K_OR", 
                  "K_ORDER", "K_SELECT", "K_TRUE", "K_WHERE", "NUMERIC_LITERAL", 
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



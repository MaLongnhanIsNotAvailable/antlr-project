# Generated from /home/long/Documents/PPL/ass1.1/assignment1/initial/src/main/csel/parser/CSEL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2?")
        buf.write("\u01d5\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\2\3\2\5\2\u0096")
        buf.write("\n\2\3\3\3\3\7\3\u009a\n\3\f\3\16\3\u009d\13\3\3\4\3\4")
        buf.write("\7\4\u00a1\n\4\f\4\16\4\u00a4\13\4\3\5\3\5\7\5\u00a8\n")
        buf.write("\5\f\5\16\5\u00ab\13\5\3\6\3\6\5\6\u00af\n\6\3\7\3\7\5")
        buf.write("\7\u00b3\n\7\3\b\3\b\7\b\u00b7\n\b\f\b\16\b\u00ba\13\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\7\t\u00c1\n\t\f\t\16\t\u00c4\13\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\7\n\u00cc\n\n\f\n\16\n\u00cf")
        buf.write("\13\n\3\13\3\13\3\13\3\13\5\13\u00d5\n\13\3\f\3\f\3\f")
        buf.write("\3\r\3\r\7\r\u00dc\n\r\f\r\16\r\u00df\13\r\3\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\7\16\u00e7\n\16\f\16\16\16\u00ea\13\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\20\3\20\5\20\u00f3\n\20\3")
        buf.write("\21\3\21\5\21\u00f7\n\21\3\21\3\21\3\22\6\22\u00fc\n\22")
        buf.write("\r\22\16\22\u00fd\3\23\3\23\7\23\u0102\n\23\f\23\16\23")
        buf.write("\u0105\13\23\3\24\3\24\5\24\u0109\n\24\3\24\6\24\u010c")
        buf.write("\n\24\r\24\16\24\u010d\3\25\3\25\3\26\3\26\3\27\3\27\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#")
        buf.write("\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3")
        buf.write("&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(")
        buf.write("\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3")
        buf.write("+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3")
        buf.write("\60\3\61\3\61\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\38\39\39\39\3:\3")
        buf.write(":\3:\3;\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3")
        buf.write("B\3C\3C\3D\3D\3E\3E\3E\3F\3F\3F\3F\3G\6G\u01ce\nG\rG\16")
        buf.write("G\u01cf\3G\3G\3H\3H\3\u00c2\2I\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\2\27\2\31\f\33\r\35\2\37\2!\2#\2")
        buf.write("%\2\'\2)\2+\2-\16/\17\61\20\63\21\65\22\67\239\24;\25")
        buf.write("=\26?\27A\30C\31E\32G\33I\34K\35M\36O\37Q S!U\"W#Y$[%")
        buf.write("]&_\'a(c)e*g+i,k-m.o/q\60s\61u\62w\63y\64{\65}\66\177")
        buf.write("\67\u00818\u00839\u0085:\u0087;\u0089<\u008b=\u008d>\u008f")
        buf.write("?\3\2\f\3\2c|\6\2\62;C\\aac|\4\2&&c|\6\2%%\64\64}}\177")
        buf.write("\177\6\2\f\f\17\17$$^^\t\2))^^ddhhppttvv\4\2GGgg\4\2-")
        buf.write("-//\3\2\62;\5\2\13\f\17\17\"\"\2\u01e0\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2")
        buf.write("\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\3\u0095\3\2\2\2\5\u0097\3\2\2")
        buf.write("\2\7\u009e\3\2\2\2\t\u00a5\3\2\2\2\13\u00ae\3\2\2\2\r")
        buf.write("\u00b2\3\2\2\2\17\u00b4\3\2\2\2\21\u00be\3\2\2\2\23\u00c9")
        buf.write("\3\2\2\2\25\u00d4\3\2\2\2\27\u00d6\3\2\2\2\31\u00d9\3")
        buf.write("\2\2\2\33\u00e4\3\2\2\2\35\u00ed\3\2\2\2\37\u00f0\3\2")
        buf.write("\2\2!\u00f6\3\2\2\2#\u00fb\3\2\2\2%\u00ff\3\2\2\2\'\u0106")
        buf.write("\3\2\2\2)\u010f\3\2\2\2+\u0111\3\2\2\2-\u0113\3\2\2\2")
        buf.write("/\u0115\3\2\2\2\61\u011b\3\2\2\2\63\u0124\3\2\2\2\65\u0127")
        buf.write("\3\2\2\2\67\u012c\3\2\2\29\u0131\3\2\2\2;\u0137\3\2\2")
        buf.write("\2=\u013b\3\2\2\2?\u013e\3\2\2\2A\u0141\3\2\2\2C\u014a")
        buf.write("\3\2\2\2E\u014e\3\2\2\2G\u0153\3\2\2\2I\u0159\3\2\2\2")
        buf.write("K\u015e\3\2\2\2M\u0165\3\2\2\2O\u016c\3\2\2\2Q\u0174\3")
        buf.write("\2\2\2S\u017b\3\2\2\2U\u0180\3\2\2\2W\u0186\3\2\2\2Y\u018f")
        buf.write("\3\2\2\2[\u0191\3\2\2\2]\u0193\3\2\2\2_\u0195\3\2\2\2")
        buf.write("a\u0197\3\2\2\2c\u0199\3\2\2\2e\u019b\3\2\2\2g\u019e\3")
        buf.write("\2\2\2i\u01a1\3\2\2\2k\u01a3\3\2\2\2m\u01a5\3\2\2\2o\u01a7")
        buf.write("\3\2\2\2q\u01aa\3\2\2\2s\u01ad\3\2\2\2u\u01b0\3\2\2\2")
        buf.write("w\u01b3\3\2\2\2y\u01b5\3\2\2\2{\u01b7\3\2\2\2}\u01b9\3")
        buf.write("\2\2\2\177\u01bb\3\2\2\2\u0081\u01bd\3\2\2\2\u0083\u01bf")
        buf.write("\3\2\2\2\u0085\u01c1\3\2\2\2\u0087\u01c3\3\2\2\2\u0089")
        buf.write("\u01c5\3\2\2\2\u008b\u01c8\3\2\2\2\u008d\u01cd\3\2\2\2")
        buf.write("\u008f\u01d3\3\2\2\2\u0091\u0096\5Q)\2\u0092\u0096\5M")
        buf.write("\'\2\u0093\u0096\5O(\2\u0094\u0096\5S*\2\u0095\u0091\3")
        buf.write("\2\2\2\u0095\u0092\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0094")
        buf.write("\3\2\2\2\u0096\4\3\2\2\2\u0097\u009b\t\2\2\2\u0098\u009a")
        buf.write("\t\3\2\2\u0099\u0098\3\2\2\2\u009a\u009d\3\2\2\2\u009b")
        buf.write("\u0099\3\2\2\2\u009b\u009c\3\2\2\2\u009c\6\3\2\2\2\u009d")
        buf.write("\u009b\3\2\2\2\u009e\u00a2\7&\2\2\u009f\u00a1\t\3\2\2")
        buf.write("\u00a0\u009f\3\2\2\2\u00a1\u00a4\3\2\2\2\u00a2\u00a0\3")
        buf.write("\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\b\3\2\2\2\u00a4\u00a2")
        buf.write("\3\2\2\2\u00a5\u00a9\t\4\2\2\u00a6\u00a8\t\3\2\2\u00a7")
        buf.write("\u00a6\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3\2\2\2")
        buf.write("\u00a9\u00aa\3\2\2\2\u00aa\n\3\2\2\2\u00ab\u00a9\3\2\2")
        buf.write("\2\u00ac\u00af\5\37\20\2\u00ad\u00af\5!\21\2\u00ae\u00ac")
        buf.write("\3\2\2\2\u00ae\u00ad\3\2\2\2\u00af\f\3\2\2\2\u00b0\u00b3")
        buf.write("\5E#\2\u00b1\u00b3\5G$\2\u00b2\u00b0\3\2\2\2\u00b2\u00b1")
        buf.write("\3\2\2\2\u00b3\16\3\2\2\2\u00b4\u00b8\7$\2\2\u00b5\u00b7")
        buf.write("\5\25\13\2\u00b6\u00b5\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8")
        buf.write("\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00bb\3\2\2\2")
        buf.write("\u00ba\u00b8\3\2\2\2\u00bb\u00bc\7$\2\2\u00bc\u00bd\b")
        buf.write("\b\2\2\u00bd\20\3\2\2\2\u00be\u00c2\5\35\17\2\u00bf\u00c1")
        buf.write("\13\2\2\2\u00c0\u00bf\3\2\2\2\u00c1\u00c4\3\2\2\2\u00c2")
        buf.write("\u00c3\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c3\u00c5\3\2\2\2")
        buf.write("\u00c4\u00c2\3\2\2\2\u00c5\u00c6\5\35\17\2\u00c6\u00c7")
        buf.write("\3\2\2\2\u00c7\u00c8\b\t\3\2\u00c8\22\3\2\2\2\u00c9\u00cd")
        buf.write("\5\35\17\2\u00ca\u00cc\n\5\2\2\u00cb\u00ca\3\2\2\2\u00cc")
        buf.write("\u00cf\3\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2")
        buf.write("\u00ce\24\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d5\n\6")
        buf.write("\2\2\u00d1\u00d5\5\27\f\2\u00d2\u00d3\7)\2\2\u00d3\u00d5")
        buf.write("\7$\2\2\u00d4\u00d0\3\2\2\2\u00d4\u00d1\3\2\2\2\u00d4")
        buf.write("\u00d2\3\2\2\2\u00d5\26\3\2\2\2\u00d6\u00d7\7^\2\2\u00d7")
        buf.write("\u00d8\t\7\2\2\u00d8\30\3\2\2\2\u00d9\u00dd\7$\2\2\u00da")
        buf.write("\u00dc\5\25\13\2\u00db\u00da\3\2\2\2\u00dc\u00df\3\2\2")
        buf.write("\2\u00dd\u00db\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00e0")
        buf.write("\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0\u00e1\7^\2\2\u00e1")
        buf.write("\u00e2\n\7\2\2\u00e2\u00e3\b\r\4\2\u00e3\32\3\2\2\2\u00e4")
        buf.write("\u00e8\7$\2\2\u00e5\u00e7\5\25\13\2\u00e6\u00e5\3\2\2")
        buf.write("\2\u00e7\u00ea\3\2\2\2\u00e8\u00e6\3\2\2\2\u00e8\u00e9")
        buf.write("\3\2\2\2\u00e9\u00eb\3\2\2\2\u00ea\u00e8\3\2\2\2\u00eb")
        buf.write("\u00ec\b\16\5\2\u00ec\34\3\2\2\2\u00ed\u00ee\7%\2\2\u00ee")
        buf.write("\u00ef\7%\2\2\u00ef\36\3\2\2\2\u00f0\u00f2\5#\22\2\u00f1")
        buf.write("\u00f3\5%\23\2\u00f2\u00f1\3\2\2\2\u00f2\u00f3\3\2\2\2")
        buf.write("\u00f3 \3\2\2\2\u00f4\u00f7\5#\22\2\u00f5\u00f7\5\37\20")
        buf.write("\2\u00f6\u00f4\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7\u00f8")
        buf.write("\3\2\2\2\u00f8\u00f9\5\'\24\2\u00f9\"\3\2\2\2\u00fa\u00fc")
        buf.write("\5)\25\2\u00fb\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd")
        buf.write("\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe$\3\2\2\2\u00ff")
        buf.write("\u0103\7\60\2\2\u0100\u0102\5)\25\2\u0101\u0100\3\2\2")
        buf.write("\2\u0102\u0105\3\2\2\2\u0103\u0101\3\2\2\2\u0103\u0104")
        buf.write("\3\2\2\2\u0104&\3\2\2\2\u0105\u0103\3\2\2\2\u0106\u0108")
        buf.write("\t\b\2\2\u0107\u0109\t\t\2\2\u0108\u0107\3\2\2\2\u0108")
        buf.write("\u0109\3\2\2\2\u0109\u010b\3\2\2\2\u010a\u010c\5)\25\2")
        buf.write("\u010b\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u010b\3")
        buf.write("\2\2\2\u010d\u010e\3\2\2\2\u010e(\3\2\2\2\u010f\u0110")
        buf.write("\t\n\2\2\u0110*\3\2\2\2\u0111\u0112\7/\2\2\u0112,\3\2")
        buf.write("\2\2\u0113\u0114\7=\2\2\u0114.\3\2\2\2\u0115\u0116\7D")
        buf.write("\2\2\u0116\u0117\7t\2\2\u0117\u0118\7g\2\2\u0118\u0119")
        buf.write("\7c\2\2\u0119\u011a\7m\2\2\u011a\60\3\2\2\2\u011b\u011c")
        buf.write("\7E\2\2\u011c\u011d\7q\2\2\u011d\u011e\7p\2\2\u011e\u011f")
        buf.write("\7v\2\2\u011f\u0120\7k\2\2\u0120\u0121\7p\2\2\u0121\u0122")
        buf.write("\7w\2\2\u0122\u0123\7g\2\2\u0123\62\3\2\2\2\u0124\u0125")
        buf.write("\7K\2\2\u0125\u0126\7h\2\2\u0126\64\3\2\2\2\u0127\u0128")
        buf.write("\7G\2\2\u0128\u0129\7n\2\2\u0129\u012a\7k\2\2\u012a\u012b")
        buf.write("\7h\2\2\u012b\66\3\2\2\2\u012c\u012d\7G\2\2\u012d\u012e")
        buf.write("\7n\2\2\u012e\u012f\7u\2\2\u012f\u0130\7g\2\2\u01308\3")
        buf.write("\2\2\2\u0131\u0132\7Y\2\2\u0132\u0133\7j\2\2\u0133\u0134")
        buf.write("\7k\2\2\u0134\u0135\7n\2\2\u0135\u0136\7g\2\2\u0136:\3")
        buf.write("\2\2\2\u0137\u0138\7H\2\2\u0138\u0139\7q\2\2\u0139\u013a")
        buf.write("\7t\2\2\u013a<\3\2\2\2\u013b\u013c\7Q\2\2\u013c\u013d")
        buf.write("\7h\2\2\u013d>\3\2\2\2\u013e\u013f\7K\2\2\u013f\u0140")
        buf.write("\7p\2\2\u0140@\3\2\2\2\u0141\u0142\7H\2\2\u0142\u0143")
        buf.write("\7w\2\2\u0143\u0144\7p\2\2\u0144\u0145\7e\2\2\u0145\u0146")
        buf.write("\7v\2\2\u0146\u0147\7k\2\2\u0147\u0148\7q\2\2\u0148\u0149")
        buf.write("\7p\2\2\u0149B\3\2\2\2\u014a\u014b\7N\2\2\u014b\u014c")
        buf.write("\7g\2\2\u014c\u014d\7v\2\2\u014dD\3\2\2\2\u014e\u014f")
        buf.write("\7V\2\2\u014f\u0150\7t\2\2\u0150\u0151\7w\2\2\u0151\u0152")
        buf.write("\7g\2\2\u0152F\3\2\2\2\u0153\u0154\7H\2\2\u0154\u0155")
        buf.write("\7c\2\2\u0155\u0156\7n\2\2\u0156\u0157\7u\2\2\u0157\u0158")
        buf.write("\7g\2\2\u0158H\3\2\2\2\u0159\u015a\7E\2\2\u015a\u015b")
        buf.write("\7c\2\2\u015b\u015c\7n\2\2\u015c\u015d\7n\2\2\u015dJ\3")
        buf.write("\2\2\2\u015e\u015f\7T\2\2\u015f\u0160\7g\2\2\u0160\u0161")
        buf.write("\7v\2\2\u0161\u0162\7w\2\2\u0162\u0163\7t\2\2\u0163\u0164")
        buf.write("\7p\2\2\u0164L\3\2\2\2\u0165\u0166\7P\2\2\u0166\u0167")
        buf.write("\7w\2\2\u0167\u0168\7o\2\2\u0168\u0169\7d\2\2\u0169\u016a")
        buf.write("\7g\2\2\u016a\u016b\7t\2\2\u016bN\3\2\2\2\u016c\u016d")
        buf.write("\7D\2\2\u016d\u016e\7q\2\2\u016e\u016f\7q\2\2\u016f\u0170")
        buf.write("\7n\2\2\u0170\u0171\7g\2\2\u0171\u0172\7c\2\2\u0172\u0173")
        buf.write("\7p\2\2\u0173P\3\2\2\2\u0174\u0175\7U\2\2\u0175\u0176")
        buf.write("\7v\2\2\u0176\u0177\7t\2\2\u0177\u0178\7k\2\2\u0178\u0179")
        buf.write("\7p\2\2\u0179\u017a\7i\2\2\u017aR\3\2\2\2\u017b\u017c")
        buf.write("\7L\2\2\u017c\u017d\7U\2\2\u017d\u017e\7Q\2\2\u017e\u017f")
        buf.write("\7P\2\2\u017fT\3\2\2\2\u0180\u0181\7C\2\2\u0181\u0182")
        buf.write("\7t\2\2\u0182\u0183\7t\2\2\u0183\u0184\7c\2\2\u0184\u0185")
        buf.write("\7{\2\2\u0185V\3\2\2\2\u0186\u0187\7E\2\2\u0187\u0188")
        buf.write("\7q\2\2\u0188\u0189\7p\2\2\u0189\u018a\7u\2\2\u018a\u018b")
        buf.write("\7v\2\2\u018b\u018c\7c\2\2\u018c\u018d\7p\2\2\u018d\u018e")
        buf.write("\7v\2\2\u018eX\3\2\2\2\u018f\u0190\7-\2\2\u0190Z\3\2\2")
        buf.write("\2\u0191\u0192\7/\2\2\u0192\\\3\2\2\2\u0193\u0194\7,\2")
        buf.write("\2\u0194^\3\2\2\2\u0195\u0196\7\61\2\2\u0196`\3\2\2\2")
        buf.write("\u0197\u0198\7\'\2\2\u0198b\3\2\2\2\u0199\u019a\7#\2\2")
        buf.write("\u019ad\3\2\2\2\u019b\u019c\7(\2\2\u019c\u019d\7(\2\2")
        buf.write("\u019df\3\2\2\2\u019e\u019f\7~\2\2\u019f\u01a0\7~\2\2")
        buf.write("\u01a0h\3\2\2\2\u01a1\u01a2\7>\2\2\u01a2j\3\2\2\2\u01a3")
        buf.write("\u01a4\7@\2\2\u01a4l\3\2\2\2\u01a5\u01a6\7?\2\2\u01a6")
        buf.write("n\3\2\2\2\u01a7\u01a8\7?\2\2\u01a8\u01a9\7?\2\2\u01a9")
        buf.write("p\3\2\2\2\u01aa\u01ab\7@\2\2\u01ab\u01ac\7?\2\2\u01ac")
        buf.write("r\3\2\2\2\u01ad\u01ae\7>\2\2\u01ae\u01af\7?\2\2\u01af")
        buf.write("t\3\2\2\2\u01b0\u01b1\7#\2\2\u01b1\u01b2\7?\2\2\u01b2")
        buf.write("v\3\2\2\2\u01b3\u01b4\7*\2\2\u01b4x\3\2\2\2\u01b5\u01b6")
        buf.write("\7+\2\2\u01b6z\3\2\2\2\u01b7\u01b8\7]\2\2\u01b8|\3\2\2")
        buf.write("\2\u01b9\u01ba\7_\2\2\u01ba~\3\2\2\2\u01bb\u01bc\7<\2")
        buf.write("\2\u01bc\u0080\3\2\2\2\u01bd\u01be\7\60\2\2\u01be\u0082")
        buf.write("\3\2\2\2\u01bf\u01c0\7.\2\2\u01c0\u0084\3\2\2\2\u01c1")
        buf.write("\u01c2\7}\2\2\u01c2\u0086\3\2\2\2\u01c3\u01c4\7\177\2")
        buf.write("\2\u01c4\u0088\3\2\2\2\u01c5\u01c6\7-\2\2\u01c6\u01c7")
        buf.write("\7\60\2\2\u01c7\u008a\3\2\2\2\u01c8\u01c9\7?\2\2\u01c9")
        buf.write("\u01ca\7?\2\2\u01ca\u01cb\7\60\2\2\u01cb\u008c\3\2\2\2")
        buf.write("\u01cc\u01ce\t\13\2\2\u01cd\u01cc\3\2\2\2\u01ce\u01cf")
        buf.write("\3\2\2\2\u01cf\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0")
        buf.write("\u01d1\3\2\2\2\u01d1\u01d2\bG\3\2\u01d2\u008e\3\2\2\2")
        buf.write("\u01d3\u01d4\13\2\2\2\u01d4\u0090\3\2\2\2\26\2\u0095\u009b")
        buf.write("\u00a2\u00a9\u00ae\u00b2\u00b8\u00c2\u00cd\u00d4\u00dd")
        buf.write("\u00e8\u00f2\u00f6\u00fd\u0103\u0108\u010d\u01cf\6\3\b")
        buf.write("\2\b\2\2\3\r\3\3\16\4")
        return buf.getvalue()


class CSELLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DATA_TYPE = 1
    ID_VARIABLE = 2
    ID_CONSTANT = 3
    ID = 4
    NUM_LIT = 5
    BOOLEAN_LIT = 6
    STRING_LIT = 7
    COMMENT = 8
    UNTERMINATED_COMMENT = 9
    ILLEGAL_ESCAPE = 10
    UNCLOSE_STRING = 11
    SEMICOLON = 12
    BREAK = 13
    CONTINUE = 14
    IF = 15
    ELIF = 16
    ELSE = 17
    WHILE = 18
    FOR = 19
    OF = 20
    IN = 21
    FUNCTION = 22
    LET = 23
    TRUE = 24
    FALSE = 25
    CALL = 26
    RETURN = 27
    NUMBER = 28
    BOOLEAN = 29
    STRING = 30
    JSON = 31
    ARRAY = 32
    CONSTANT = 33
    ADD = 34
    MINUS = 35
    MUL = 36
    DIV = 37
    MOD = 38
    NOT = 39
    AND = 40
    OR = 41
    LESS_THAN = 42
    GREATER_THAN = 43
    ASSIGN = 44
    EQUALS = 45
    GTE = 46
    LTE = 47
    NOT_EQ = 48
    LP = 49
    RP = 50
    LSB = 51
    RSB = 52
    COLON = 53
    DOT = 54
    COMMA = 55
    LCB = 56
    RCB = 57
    ADD_DOT = 58
    DEQUAL_DOT = 59
    WS = 60
    ERROR_CHAR = 61

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'Break'", "'Continue'", "'If'", "'Elif'", "'Else'", 
            "'While'", "'For'", "'Of'", "'In'", "'Function'", "'Let'", "'True'", 
            "'False'", "'Call'", "'Return'", "'Number'", "'Boolean'", "'String'", 
            "'JSON'", "'Array'", "'Constant'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'<'", "'>'", "'='", "'=='", "'>='", 
            "'<='", "'!='", "'('", "')'", "'['", "']'", "':'", "'.'", "','", 
            "'{'", "'}'", "'+.'", "'==.'" ]

    symbolicNames = [ "<INVALID>",
            "DATA_TYPE", "ID_VARIABLE", "ID_CONSTANT", "ID", "NUM_LIT", 
            "BOOLEAN_LIT", "STRING_LIT", "COMMENT", "UNTERMINATED_COMMENT", 
            "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "SEMICOLON", "BREAK", "CONTINUE", 
            "IF", "ELIF", "ELSE", "WHILE", "FOR", "OF", "IN", "FUNCTION", 
            "LET", "TRUE", "FALSE", "CALL", "RETURN", "NUMBER", "BOOLEAN", 
            "STRING", "JSON", "ARRAY", "CONSTANT", "ADD", "MINUS", "MUL", 
            "DIV", "MOD", "NOT", "AND", "OR", "LESS_THAN", "GREATER_THAN", 
            "ASSIGN", "EQUALS", "GTE", "LTE", "NOT_EQ", "LP", "RP", "LSB", 
            "RSB", "COLON", "DOT", "COMMA", "LCB", "RCB", "ADD_DOT", "DEQUAL_DOT", 
            "WS", "ERROR_CHAR" ]

    ruleNames = [ "DATA_TYPE", "ID_VARIABLE", "ID_CONSTANT", "ID", "NUM_LIT", 
                  "BOOLEAN_LIT", "STRING_LIT", "COMMENT", "UNTERMINATED_COMMENT", 
                  "STRINGCHAR", "EscapeSequence", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                  "HASHTAGS", "POINT_FLOAT", "EXPONENT_FLOAT", "INT_PART", 
                  "FRACTION", "EXPONENT", "DIGIT", "NEGATIVE", "SEMICOLON", 
                  "BREAK", "CONTINUE", "IF", "ELIF", "ELSE", "WHILE", "FOR", 
                  "OF", "IN", "FUNCTION", "LET", "TRUE", "FALSE", "CALL", 
                  "RETURN", "NUMBER", "BOOLEAN", "STRING", "JSON", "ARRAY", 
                  "CONSTANT", "ADD", "MINUS", "MUL", "DIV", "MOD", "NOT", 
                  "AND", "OR", "LESS_THAN", "GREATER_THAN", "ASSIGN", "EQUALS", 
                  "GTE", "LTE", "NOT_EQ", "LP", "RP", "LSB", "RSB", "COLON", 
                  "DOT", "COMMA", "LCB", "RCB", "ADD_DOT", "DEQUAL_DOT", 
                  "WS", "ERROR_CHAR" ]

    grammarFileName = "CSEL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[6] = self.STRING_LIT_action 
            actions[11] = self.ILLEGAL_ESCAPE_action 
            actions[12] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            self.text=self.text[1:-1]

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                raise IllegalEscape(self.text[1:])

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                raise UncloseString(self.text[1:])

     



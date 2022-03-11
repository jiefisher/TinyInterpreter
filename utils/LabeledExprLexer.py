# Generated from LabeledExpr.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\23")
        buf.write("f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\fH\n\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\5\rQ\n\r\3\16\6\16T\n\16\r\16\16\16U\3\17")
        buf.write("\3\17\7\17Z\n\17\f\17\16\17]\13\17\3\20\3\20\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\2\2\23\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("\3\2\6\3\2\62;\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\16\17")
        buf.write("\"\"\2i\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\3%\3\2\2\2\5\'\3\2\2\2\7)\3\2\2\2\t+\3\2\2\2\13")
        buf.write("-\3\2\2\2\r/\3\2\2\2\17\61\3\2\2\2\21\65\3\2\2\2\23\67")
        buf.write("\3\2\2\2\259\3\2\2\2\27G\3\2\2\2\31P\3\2\2\2\33S\3\2\2")
        buf.write("\2\35W\3\2\2\2\37^\3\2\2\2!`\3\2\2\2#b\3\2\2\2%&\7*\2")
        buf.write("\2&\4\3\2\2\2\'(\7+\2\2(\6\3\2\2\2)*\7,\2\2*\b\3\2\2\2")
        buf.write("+,\7\61\2\2,\n\3\2\2\2-.\7-\2\2.\f\3\2\2\2/\60\7/\2\2")
        buf.write("\60\16\3\2\2\2\61\62\7f\2\2\62\63\7g\2\2\63\64\7h\2\2")
        buf.write("\64\20\3\2\2\2\65\66\7}\2\2\66\22\3\2\2\2\678\7\177\2")
        buf.write("\28\24\3\2\2\29:\7t\2\2:;\7g\2\2;<\7v\2\2<=\7w\2\2=>\7")
        buf.write("t\2\2>?\7p\2\2?\26\3\2\2\2@A\7j\2\2AB\7g\2\2BC\7n\2\2")
        buf.write("CD\7n\2\2DH\7q\2\2EF\7j\2\2FH\7k\2\2G@\3\2\2\2GE\3\2\2")
        buf.write("\2H\30\3\2\2\2IJ\7d\2\2JK\7{\2\2KQ\7g\2\2LM\7v\2\2MN\7")
        buf.write("c\2\2NO\7v\2\2OQ\7c\2\2PI\3\2\2\2PL\3\2\2\2Q\32\3\2\2")
        buf.write("\2RT\t\2\2\2SR\3\2\2\2TU\3\2\2\2US\3\2\2\2UV\3\2\2\2V")
        buf.write("\34\3\2\2\2W[\t\3\2\2XZ\t\4\2\2YX\3\2\2\2Z]\3\2\2\2[Y")
        buf.write("\3\2\2\2[\\\3\2\2\2\\\36\3\2\2\2][\3\2\2\2^_\7?\2\2_ ")
        buf.write("\3\2\2\2`a\7=\2\2a\"\3\2\2\2bc\t\5\2\2cd\3\2\2\2de\b\22")
        buf.write("\2\2e$\3\2\2\2\7\2GPU[\3\b\2\2")
        return buf.getvalue()


class LabeledExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    DEF = 7
    START = 8
    END = 9
    Return = 10
    HELLO = 11
    BYE = 12
    INT = 13
    ID = 14
    EQUAL = 15
    SCOL = 16
    Space = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'*'", "'/'", "'+'", "'-'", "'def'", "'{'", "'}'", 
            "'return'", "'='", "';'" ]

    symbolicNames = [ "<INVALID>",
            "DEF", "START", "END", "Return", "HELLO", "BYE", "INT", "ID", 
            "EQUAL", "SCOL", "Space" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "DEF", 
                  "START", "END", "Return", "HELLO", "BYE", "INT", "ID", 
                  "EQUAL", "SCOL", "Space" ]

    grammarFileName = "LabeledExpr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



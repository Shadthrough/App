# Generated from .\static\antlr\fsm.g4 by ANTLR 4.10.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,7,29,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,0,
        0,7,1,1,3,2,5,3,7,4,9,5,11,6,13,7,1,0,0,28,0,1,1,0,0,0,0,3,1,0,0,
        0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,
        1,15,1,0,0,0,3,17,1,0,0,0,5,19,1,0,0,0,7,21,1,0,0,0,9,23,1,0,0,0,
        11,25,1,0,0,0,13,27,1,0,0,0,15,16,5,35,0,0,16,2,1,0,0,0,17,18,5,
        51,0,0,18,4,1,0,0,0,19,20,5,120,0,0,20,6,1,0,0,0,21,22,5,65,0,0,
        22,8,1,0,0,0,23,24,5,108,0,0,24,10,1,0,0,0,25,26,5,114,0,0,26,12,
        1,0,0,0,27,28,5,66,0,0,28,14,1,0,0,0,1,0,0
    ]

class fsmLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'#'", "'3'", "'x'", "'A'", "'l'", "'r'", "'B'" ]

    symbolicNames = [ "<INVALID>",
 ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6" ]

    grammarFileName = "fsm.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



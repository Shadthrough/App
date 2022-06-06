# Generated from .\static\antlr\fsm.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,123,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,3,1,47,8,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,55,8,2,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,67,8,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,
        75,8,4,1,5,1,5,1,5,1,5,1,5,1,5,3,5,83,8,5,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,3,6,92,8,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,100,8,7,1,8,1,8,1,8,
        1,8,1,8,1,8,3,8,108,8,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,116,8,9,1,10,
        1,10,1,10,3,10,121,8,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,
        0,0,141,0,22,1,0,0,0,2,46,1,0,0,0,4,54,1,0,0,0,6,66,1,0,0,0,8,74,
        1,0,0,0,10,82,1,0,0,0,12,91,1,0,0,0,14,99,1,0,0,0,16,107,1,0,0,0,
        18,115,1,0,0,0,20,120,1,0,0,0,22,23,3,2,1,0,23,1,1,0,0,0,24,25,5,
        1,0,0,25,47,3,2,1,0,26,27,5,1,0,0,27,47,3,16,8,0,28,29,5,2,0,0,29,
        47,3,16,8,0,30,31,5,1,0,0,31,47,3,4,2,0,32,33,5,3,0,0,33,47,3,4,
        2,0,34,35,5,1,0,0,35,47,3,10,5,0,36,37,5,4,0,0,37,47,3,10,5,0,38,
        39,5,1,0,0,39,47,3,14,7,0,40,41,5,5,0,0,41,47,3,14,7,0,42,43,5,1,
        0,0,43,47,3,12,6,0,44,45,5,6,0,0,45,47,3,12,6,0,46,24,1,0,0,0,46,
        26,1,0,0,0,46,28,1,0,0,0,46,30,1,0,0,0,46,32,1,0,0,0,46,34,1,0,0,
        0,46,36,1,0,0,0,46,38,1,0,0,0,46,40,1,0,0,0,46,42,1,0,0,0,46,44,
        1,0,0,0,47,3,1,0,0,0,48,49,5,1,0,0,49,55,3,4,2,0,50,51,5,1,0,0,51,
        55,3,6,3,0,52,53,5,7,0,0,53,55,3,6,3,0,54,48,1,0,0,0,54,50,1,0,0,
        0,54,52,1,0,0,0,55,5,1,0,0,0,56,57,5,1,0,0,57,67,3,6,3,0,58,59,5,
        1,0,0,59,67,3,20,10,0,60,61,5,2,0,0,61,67,3,20,10,0,62,63,5,1,0,
        0,63,67,3,8,4,0,64,65,5,4,0,0,65,67,3,8,4,0,66,56,1,0,0,0,66,58,
        1,0,0,0,66,60,1,0,0,0,66,62,1,0,0,0,66,64,1,0,0,0,67,7,1,0,0,0,68,
        69,5,1,0,0,69,75,3,8,4,0,70,71,5,1,0,0,71,75,3,6,3,0,72,73,5,7,0,
        0,73,75,3,6,3,0,74,68,1,0,0,0,74,70,1,0,0,0,74,72,1,0,0,0,75,9,1,
        0,0,0,76,77,5,1,0,0,77,83,3,10,5,0,78,79,5,1,0,0,79,83,3,4,2,0,80,
        81,5,3,0,0,81,83,3,4,2,0,82,76,1,0,0,0,82,78,1,0,0,0,82,80,1,0,0,
        0,83,11,1,0,0,0,84,85,5,1,0,0,85,92,3,12,6,0,86,87,5,1,0,0,87,92,
        3,14,7,0,88,92,5,0,0,1,89,90,5,5,0,0,90,92,3,14,7,0,91,84,1,0,0,
        0,91,86,1,0,0,0,91,88,1,0,0,0,91,89,1,0,0,0,92,13,1,0,0,0,93,94,
        5,1,0,0,94,100,3,14,7,0,95,96,5,1,0,0,96,100,3,14,7,0,97,98,5,6,
        0,0,98,100,3,14,7,0,99,93,1,0,0,0,99,95,1,0,0,0,99,97,1,0,0,0,100,
        15,1,0,0,0,101,102,5,1,0,0,102,108,3,16,8,0,103,104,5,1,0,0,104,
        108,3,4,2,0,105,106,5,2,0,0,106,108,3,4,2,0,107,101,1,0,0,0,107,
        103,1,0,0,0,107,105,1,0,0,0,108,17,1,0,0,0,109,110,5,1,0,0,110,116,
        3,18,9,0,111,112,5,1,0,0,112,116,3,4,2,0,113,114,5,2,0,0,114,116,
        3,4,2,0,115,109,1,0,0,0,115,111,1,0,0,0,115,113,1,0,0,0,116,19,1,
        0,0,0,117,118,5,1,0,0,118,121,3,20,10,0,119,121,5,0,0,1,120,117,
        1,0,0,0,120,119,1,0,0,0,121,21,1,0,0,0,10,46,54,66,74,82,91,99,107,
        115,120
    ]

class fsmParser ( Parser ):

    grammarFileName = "fsm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'#'", "'3'", "'x'", "'A'", "'l'", "'r'", 
                     "'B'" ]

    symbolicNames = [  ]

    RULE_expr = 0
    RULE_start = 1
    RULE_s0 = 2
    RULE_s1 = 3
    RULE_s2 = 4
    RULE_s3 = 5
    RULE_s4 = 6
    RULE_s5 = 7
    RULE_s6 = 8
    RULE_s7 = 9
    RULE_s8 = 10

    ruleNames =  [ "expr", "start", "s0", "s1", "s2", "s3", "s4", "s5", 
                   "s6", "s7", "s8" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def start(self):
            return self.getTypedRuleContext(fsmParser.StartContext,0)


        def getRuleIndex(self):
            return fsmParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = fsmParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.start()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def start(self):
            return self.getTypedRuleContext(fsmParser.StartContext,0)


        def s6(self):
            return self.getTypedRuleContext(fsmParser.S6Context,0)


        def s0(self):
            return self.getTypedRuleContext(fsmParser.S0Context,0)


        def s3(self):
            return self.getTypedRuleContext(fsmParser.S3Context,0)


        def s5(self):
            return self.getTypedRuleContext(fsmParser.S5Context,0)


        def s4(self):
            return self.getTypedRuleContext(fsmParser.S4Context,0)


        def getRuleIndex(self):
            return fsmParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = fsmParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_start)
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.match(fsmParser.T__0)
                self.state = 25
                self.start()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.match(fsmParser.T__0)
                self.state = 27
                self.s6()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.match(fsmParser.T__1)
                self.state = 29
                self.s6()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.match(fsmParser.T__0)
                self.state = 31
                self.s0()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 32
                self.match(fsmParser.T__2)
                self.state = 33
                self.s0()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 34
                self.match(fsmParser.T__0)
                self.state = 35
                self.s3()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 36
                self.match(fsmParser.T__3)
                self.state = 37
                self.s3()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 38
                self.match(fsmParser.T__0)
                self.state = 39
                self.s5()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 40
                self.match(fsmParser.T__4)
                self.state = 41
                self.s5()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 42
                self.match(fsmParser.T__0)
                self.state = 43
                self.s4()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 44
                self.match(fsmParser.T__5)
                self.state = 45
                self.s4()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class S0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s0(self):
            return self.getTypedRuleContext(fsmParser.S0Context,0)


        def s1(self):
            return self.getTypedRuleContext(fsmParser.S1Context,0)


        def getRuleIndex(self):
            return fsmParser.RULE_s0

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS0" ):
                listener.enterS0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS0" ):
                listener.exitS0(self)




    def s0(self):

        localctx = fsmParser.S0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_s0)
        try:
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.match(fsmParser.T__0)
                self.state = 49
                self.s0()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.match(fsmParser.T__0)
                self.state = 51
                self.s1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.match(fsmParser.T__6)
                self.state = 53
                self.s1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class S1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s1(self):
            return self.getTypedRuleContext(fsmParser.S1Context,0)


        def s8(self):
            return self.getTypedRuleContext(fsmParser.S8Context,0)


        def s2(self):
            return self.getTypedRuleContext(fsmParser.S2Context,0)


        def getRuleIndex(self):
            return fsmParser.RULE_s1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS1" ):
                listener.enterS1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS1" ):
                listener.exitS1(self)




    def s1(self):

        localctx = fsmParser.S1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_s1)
        try:
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(fsmParser.T__0)
                self.state = 57
                self.s1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.match(fsmParser.T__0)
                self.state = 59
                self.s8()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 60
                self.match(fsmParser.T__1)
                self.state = 61
                self.s8()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 62
                self.match(fsmParser.T__0)
                self.state = 63
                self.s2()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 64
                self.match(fsmParser.T__3)
                self.state = 65
                self.s2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class S2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s2(self):
            return self.getTypedRuleContext(fsmParser.S2Context,0)


        def s1(self):
            return self.getTypedRuleContext(fsmParser.S1Context,0)


        def getRuleIndex(self):
            return fsmParser.RULE_s2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS2" ):
                listener.enterS2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS2" ):
                listener.exitS2(self)




    def s2(self):

        localctx = fsmParser.S2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_s2)
        try:
            self.state = 74
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.match(fsmParser.T__0)
                self.state = 69
                self.s2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.match(fsmParser.T__0)
                self.state = 71
                self.s1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.match(fsmParser.T__6)
                self.state = 73
                self.s1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class S3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s3(self):
            return self.getTypedRuleContext(fsmParser.S3Context,0)


        def s0(self):
            return self.getTypedRuleContext(fsmParser.S0Context,0)


        def getRuleIndex(self):
            return fsmParser.RULE_s3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS3" ):
                listener.enterS3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS3" ):
                listener.exitS3(self)




    def s3(self):

        localctx = fsmParser.S3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_s3)
        try:
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(fsmParser.T__0)
                self.state = 77
                self.s3()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.match(fsmParser.T__0)
                self.state = 79
                self.s0()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 80
                self.match(fsmParser.T__2)
                self.state = 81
                self.s0()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class S4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s4(self):
            return self.getTypedRuleContext(fsmParser.S4Context,0)


        def s5(self):
            return self.getTypedRuleContext(fsmParser.S5Context,0)


        def EOF(self):
            return self.getToken(fsmParser.EOF, 0)

        def getRuleIndex(self):
            return fsmParser.RULE_s4

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS4" ):
                listener.enterS4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS4" ):
                listener.exitS4(self)




    def s4(self):

        localctx = fsmParser.S4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_s4)
        try:
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.match(fsmParser.T__0)
                self.state = 85
                self.s4()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.match(fsmParser.T__0)
                self.state = 87
                self.s5()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.match(fsmParser.EOF)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 89
                self.match(fsmParser.T__4)
                self.state = 90
                self.s5()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class S5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s5(self):
            return self.getTypedRuleContext(fsmParser.S5Context,0)


        def getRuleIndex(self):
            return fsmParser.RULE_s5

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS5" ):
                listener.enterS5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS5" ):
                listener.exitS5(self)




    def s5(self):

        localctx = fsmParser.S5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_s5)
        try:
            self.state = 99
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.match(fsmParser.T__0)
                self.state = 94
                self.s5()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.match(fsmParser.T__0)
                self.state = 96
                self.s5()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 97
                self.match(fsmParser.T__5)
                self.state = 98
                self.s5()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class S6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s6(self):
            return self.getTypedRuleContext(fsmParser.S6Context,0)


        def s0(self):
            return self.getTypedRuleContext(fsmParser.S0Context,0)


        def getRuleIndex(self):
            return fsmParser.RULE_s6

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS6" ):
                listener.enterS6(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS6" ):
                listener.exitS6(self)




    def s6(self):

        localctx = fsmParser.S6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_s6)
        try:
            self.state = 107
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.match(fsmParser.T__0)
                self.state = 102
                self.s6()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.match(fsmParser.T__0)
                self.state = 104
                self.s0()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 105
                self.match(fsmParser.T__1)
                self.state = 106
                self.s0()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class S7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s7(self):
            return self.getTypedRuleContext(fsmParser.S7Context,0)


        def s0(self):
            return self.getTypedRuleContext(fsmParser.S0Context,0)


        def getRuleIndex(self):
            return fsmParser.RULE_s7

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS7" ):
                listener.enterS7(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS7" ):
                listener.exitS7(self)




    def s7(self):

        localctx = fsmParser.S7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_s7)
        try:
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 109
                self.match(fsmParser.T__0)
                self.state = 110
                self.s7()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.match(fsmParser.T__0)
                self.state = 112
                self.s0()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 113
                self.match(fsmParser.T__1)
                self.state = 114
                self.s0()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class S8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def s8(self):
            return self.getTypedRuleContext(fsmParser.S8Context,0)


        def EOF(self):
            return self.getToken(fsmParser.EOF, 0)

        def getRuleIndex(self):
            return fsmParser.RULE_s8

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterS8" ):
                listener.enterS8(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitS8" ):
                listener.exitS8(self)




    def s8(self):

        localctx = fsmParser.S8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_s8)
        try:
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [fsmParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.match(fsmParser.T__0)
                self.state = 118
                self.s8()
                pass
            elif token in [fsmParser.EOF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.match(fsmParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






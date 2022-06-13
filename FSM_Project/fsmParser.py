# Generated from .\fsm.g4 by ANTLR 4.10.1
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
        4,1,4,48,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,3,1,21,8,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,29,
        8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,38,8,3,1,4,1,4,1,4,1,4,1,4,1,
        4,3,4,46,8,4,1,4,0,0,5,0,2,4,6,8,0,0,52,0,10,1,0,0,0,2,20,1,0,0,
        0,4,28,1,0,0,0,6,37,1,0,0,0,8,45,1,0,0,0,10,11,3,2,1,0,11,1,1,0,
        0,0,12,13,5,1,0,0,13,21,3,2,1,0,14,15,5,1,0,0,15,21,3,4,2,0,16,17,
        5,2,0,0,17,21,3,4,2,0,18,19,5,3,0,0,19,21,3,4,2,0,20,12,1,0,0,0,
        20,14,1,0,0,0,20,16,1,0,0,0,20,18,1,0,0,0,21,3,1,0,0,0,22,23,5,1,
        0,0,23,29,3,4,2,0,24,25,5,1,0,0,25,29,3,6,3,0,26,27,5,4,0,0,27,29,
        3,6,3,0,28,22,1,0,0,0,28,24,1,0,0,0,28,26,1,0,0,0,29,5,1,0,0,0,30,
        31,5,1,0,0,31,38,3,6,3,0,32,33,5,1,0,0,33,38,3,8,4,0,34,38,5,0,0,
        1,35,36,5,2,0,0,36,38,3,8,4,0,37,30,1,0,0,0,37,32,1,0,0,0,37,34,
        1,0,0,0,37,35,1,0,0,0,38,7,1,0,0,0,39,40,5,1,0,0,40,46,3,8,4,0,41,
        42,5,1,0,0,42,46,3,6,3,0,43,44,5,4,0,0,44,46,3,6,3,0,45,39,1,0,0,
        0,45,41,1,0,0,0,45,43,1,0,0,0,46,9,1,0,0,0,4,20,28,37,45
    ]

class fsmParser ( Parser ):

    grammarFileName = "fsm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'#'", "'A'", "'x'", "'B'" ]

    symbolicNames = [  ]

    RULE_expr = 0
    RULE_start = 1
    RULE_s0 = 2
    RULE_s1 = 3
    RULE_s2 = 4

    ruleNames =  [ "expr", "start", "s0", "s1", "s2" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4

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
            self.state = 10
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


        def s0(self):
            return self.getTypedRuleContext(fsmParser.S0Context,0)


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
            self.state = 20
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.match(fsmParser.T__0)
                self.state = 13
                self.start()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(fsmParser.T__0)
                self.state = 15
                self.s0()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 16
                self.match(fsmParser.T__1)
                self.state = 17
                self.s0()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 18
                self.match(fsmParser.T__2)
                self.state = 19
                self.s0()
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
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.match(fsmParser.T__0)
                self.state = 23
                self.s0()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.match(fsmParser.T__0)
                self.state = 25
                self.s1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.match(fsmParser.T__3)
                self.state = 27
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


        def s2(self):
            return self.getTypedRuleContext(fsmParser.S2Context,0)


        def EOF(self):
            return self.getToken(fsmParser.EOF, 0)

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
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.match(fsmParser.T__0)
                self.state = 31
                self.s1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.match(fsmParser.T__0)
                self.state = 33
                self.s2()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.match(fsmParser.EOF)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 35
                self.match(fsmParser.T__1)
                self.state = 36
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
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(fsmParser.T__0)
                self.state = 40
                self.s2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.match(fsmParser.T__0)
                self.state = 42
                self.s1()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.match(fsmParser.T__3)
                self.state = 44
                self.s1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






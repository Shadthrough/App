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
        4,1,4,66,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,27,8,1,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,39,8,2,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,3,3,52,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,3,4,64,8,4,1,4,0,0,5,0,2,4,6,8,0,0,70,0,10,1,0,0,0,2,26,
        1,0,0,0,4,38,1,0,0,0,6,51,1,0,0,0,8,63,1,0,0,0,10,11,3,2,1,0,11,
        1,1,0,0,0,12,13,5,1,0,0,13,27,3,2,1,0,14,15,5,1,0,0,15,16,3,4,2,
        0,16,17,6,1,-1,0,17,27,1,0,0,0,18,19,5,2,0,0,19,20,3,4,2,0,20,21,
        6,1,-1,0,21,27,1,0,0,0,22,23,5,3,0,0,23,24,3,4,2,0,24,25,6,1,-1,
        0,25,27,1,0,0,0,26,12,1,0,0,0,26,14,1,0,0,0,26,18,1,0,0,0,26,22,
        1,0,0,0,27,3,1,0,0,0,28,29,5,1,0,0,29,39,3,4,2,0,30,31,5,1,0,0,31,
        32,3,6,3,0,32,33,6,2,-1,0,33,39,1,0,0,0,34,35,5,4,0,0,35,36,3,6,
        3,0,36,37,6,2,-1,0,37,39,1,0,0,0,38,28,1,0,0,0,38,30,1,0,0,0,38,
        34,1,0,0,0,39,5,1,0,0,0,40,41,5,1,0,0,41,52,3,6,3,0,42,43,5,1,0,
        0,43,44,3,8,4,0,44,45,6,3,-1,0,45,52,1,0,0,0,46,52,5,0,0,1,47,48,
        5,2,0,0,48,49,3,8,4,0,49,50,6,3,-1,0,50,52,1,0,0,0,51,40,1,0,0,0,
        51,42,1,0,0,0,51,46,1,0,0,0,51,47,1,0,0,0,52,7,1,0,0,0,53,54,5,1,
        0,0,54,64,3,8,4,0,55,56,5,1,0,0,56,57,3,6,3,0,57,58,6,4,-1,0,58,
        64,1,0,0,0,59,60,5,4,0,0,60,61,3,6,3,0,61,62,6,4,-1,0,62,64,1,0,
        0,0,63,53,1,0,0,0,63,55,1,0,0,0,63,59,1,0,0,0,64,9,1,0,0,0,4,26,
        38,51,63
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



    paths = []



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
            self.state = 26
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
                self.paths.append('-A>s0')
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 18
                self.match(fsmParser.T__1)
                self.state = 19
                self.s0()
                self.paths.append('-A>s0')
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 22
                self.match(fsmParser.T__2)
                self.state = 23
                self.s0()
                self.paths.append('-x>s0')
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
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.match(fsmParser.T__0)
                self.state = 29
                self.s0()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.match(fsmParser.T__0)
                self.state = 31
                self.s1()
                self.paths.append('-B>s1')
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.match(fsmParser.T__3)
                self.state = 35
                self.s1()
                self.paths.append('-B>s1')
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
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.match(fsmParser.T__0)
                self.state = 41
                self.s1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(fsmParser.T__0)
                self.state = 43
                self.s2()
                self.paths.append('-A>s2')
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.match(fsmParser.EOF)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 47
                self.match(fsmParser.T__1)
                self.state = 48
                self.s2()
                self.paths.append('-A>s2')
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
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(fsmParser.T__0)
                self.state = 54
                self.s2()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(fsmParser.T__0)
                self.state = 56
                self.s1()
                self.paths.append('-B>s1')
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 59
                self.match(fsmParser.T__3)
                self.state = 60
                self.s1()
                self.paths.append('-B>s1')
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






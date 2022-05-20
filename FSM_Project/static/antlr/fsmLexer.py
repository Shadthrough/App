# $ANTLR 3.3 Nov 30, 2010 12:50:56 fsm__.g 2022-05-20 13:49:20

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
EOF=-1
T__4=4
T__5=5
T__6=6
T__7=7
T__8=8


class fsmLexer(Lexer):

    grammarFileName = "fsm__.g"
    antlr_version = version_str_to_tuple("3.3 Nov 30, 2010 12:50:56")
    antlr_version_str = "3.3 Nov 30, 2010 12:50:56"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(fsmLexer, self).__init__(input, state)







    # $ANTLR start "T__4"
    def mT__4(self, ):

        try:
            _type = T__4
            _channel = DEFAULT_CHANNEL

            # fsm__.g:7:6: ( '#' )
            # fsm__.g:7:8: '#'
            pass 
            self.match(35)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__4"



    # $ANTLR start "T__5"
    def mT__5(self, ):

        try:
            _type = T__5
            _channel = DEFAULT_CHANNEL

            # fsm__.g:8:6: ( '2' )
            # fsm__.g:8:8: '2'
            pass 
            self.match(50)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__5"



    # $ANTLR start "T__6"
    def mT__6(self, ):

        try:
            _type = T__6
            _channel = DEFAULT_CHANNEL

            # fsm__.g:9:6: ( 'A' )
            # fsm__.g:9:8: 'A'
            pass 
            self.match(65)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__6"



    # $ANTLR start "T__7"
    def mT__7(self, ):

        try:
            _type = T__7
            _channel = DEFAULT_CHANNEL

            # fsm__.g:10:6: ( 'x' )
            # fsm__.g:10:8: 'x'
            pass 
            self.match(120)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__7"



    # $ANTLR start "T__8"
    def mT__8(self, ):

        try:
            _type = T__8
            _channel = DEFAULT_CHANNEL

            # fsm__.g:11:6: ( 'B' )
            # fsm__.g:11:8: 'B'
            pass 
            self.match(66)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__8"



    def mTokens(self):
        # fsm__.g:1:8: ( T__4 | T__5 | T__6 | T__7 | T__8 )
        alt1 = 5
        LA1 = self.input.LA(1)
        if LA1 == 35:
            alt1 = 1
        elif LA1 == 50:
            alt1 = 2
        elif LA1 == 65:
            alt1 = 3
        elif LA1 == 120:
            alt1 = 4
        elif LA1 == 66:
            alt1 = 5
        else:
            nvae = NoViableAltException("", 1, 0, self.input)

            raise nvae

        if alt1 == 1:
            # fsm__.g:1:10: T__4
            pass 
            self.mT__4()


        elif alt1 == 2:
            # fsm__.g:1:15: T__5
            pass 
            self.mT__5()


        elif alt1 == 3:
            # fsm__.g:1:20: T__6
            pass 
            self.mT__6()


        elif alt1 == 4:
            # fsm__.g:1:25: T__7
            pass 
            self.mT__7()


        elif alt1 == 5:
            # fsm__.g:1:30: T__8
            pass 
            self.mT__8()







 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(fsmLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)

# $ANTLR 3.3 Nov 30, 2010 12:50:56 .\\static\\antlr\\fsm.g 2022-05-20 13:49:20

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

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "'#'", "'2'", "'A'", "'x'", "'B'"
]




class fsmParser(Parser):
    grammarFileName = ".\\static\\antlr\\fsm.g"
    antlr_version = version_str_to_tuple("3.3 Nov 30, 2010 12:50:56")
    antlr_version_str = "3.3 Nov 30, 2010 12:50:56"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(fsmParser, self).__init__(input, state, *args, **kwargs)






                


        



    # $ANTLR start "start"
    # .\\static\\antlr\\fsm.g:3:1: start : ( '#' s1 | '2' s1 | '#' s0 | 'A' s0 | 'x' s0 );
    def start(self, ):

        try:
            try:
                # .\\static\\antlr\\fsm.g:3:7: ( '#' s1 | '2' s1 | '#' s0 | 'A' s0 | 'x' s0 )
                alt1 = 5
                LA1 = self.input.LA(1)
                if LA1 == 4:
                    LA1_1 = self.input.LA(2)

                    if (self.synpred1_fsm()) :
                        alt1 = 1
                    elif (self.synpred3_fsm()) :
                        alt1 = 3
                    else:
                        if self._state.backtracking > 0:
                            raise BacktrackingFailed

                        nvae = NoViableAltException("", 1, 1, self.input)

                        raise nvae

                elif LA1 == 5:
                    alt1 = 2
                elif LA1 == 6:
                    alt1 = 4
                elif LA1 == 7:
                    alt1 = 5
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 1, 0, self.input)

                    raise nvae

                if alt1 == 1:
                    # .\\static\\antlr\\fsm.g:3:9: '#' s1
                    pass 
                    self.match(self.input, 4, self.FOLLOW_4_in_start20)
                    self._state.following.append(self.FOLLOW_s1_in_start22)
                    self.s1()

                    self._state.following.pop()


                elif alt1 == 2:
                    # .\\static\\antlr\\fsm.g:4:3: '2' s1
                    pass 
                    self.match(self.input, 5, self.FOLLOW_5_in_start26)
                    self._state.following.append(self.FOLLOW_s1_in_start28)
                    self.s1()

                    self._state.following.pop()


                elif alt1 == 3:
                    # .\\static\\antlr\\fsm.g:5:3: '#' s0
                    pass 
                    self.match(self.input, 4, self.FOLLOW_4_in_start32)
                    self._state.following.append(self.FOLLOW_s0_in_start34)
                    self.s0()

                    self._state.following.pop()


                elif alt1 == 4:
                    # .\\static\\antlr\\fsm.g:6:3: 'A' s0
                    pass 
                    self.match(self.input, 6, self.FOLLOW_6_in_start38)
                    self._state.following.append(self.FOLLOW_s0_in_start40)
                    self.s0()

                    self._state.following.pop()


                elif alt1 == 5:
                    # .\\static\\antlr\\fsm.g:7:3: 'x' s0
                    pass 
                    self.match(self.input, 7, self.FOLLOW_7_in_start44)
                    self._state.following.append(self.FOLLOW_s0_in_start46)
                    self.s0()

                    self._state.following.pop()



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "start"


    # $ANTLR start "s0"
    # .\\static\\antlr\\fsm.g:9:1: s0 : ( '#' s1 | 'B' s1 );
    def s0(self, ):

        try:
            try:
                # .\\static\\antlr\\fsm.g:9:4: ( '#' s1 | 'B' s1 )
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == 4) :
                    alt2 = 1
                elif (LA2_0 == 8) :
                    alt2 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 2, 0, self.input)

                    raise nvae

                if alt2 == 1:
                    # .\\static\\antlr\\fsm.g:9:6: '#' s1
                    pass 
                    self.match(self.input, 4, self.FOLLOW_4_in_s054)
                    self._state.following.append(self.FOLLOW_s1_in_s056)
                    self.s1()

                    self._state.following.pop()


                elif alt2 == 2:
                    # .\\static\\antlr\\fsm.g:10:3: 'B' s1
                    pass 
                    self.match(self.input, 8, self.FOLLOW_8_in_s060)
                    self._state.following.append(self.FOLLOW_s1_in_s062)
                    self.s1()

                    self._state.following.pop()



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "s0"


    # $ANTLR start "s1"
    # .\\static\\antlr\\fsm.g:12:1: s1 : ( '#' s2 | 'A' s2 );
    def s1(self, ):

        try:
            try:
                # .\\static\\antlr\\fsm.g:12:4: ( '#' s2 | 'A' s2 )
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == 4) :
                    alt3 = 1
                elif (LA3_0 == 6) :
                    alt3 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 3, 0, self.input)

                    raise nvae

                if alt3 == 1:
                    # .\\static\\antlr\\fsm.g:12:6: '#' s2
                    pass 
                    self.match(self.input, 4, self.FOLLOW_4_in_s170)
                    self._state.following.append(self.FOLLOW_s2_in_s172)
                    self.s2()

                    self._state.following.pop()


                elif alt3 == 2:
                    # .\\static\\antlr\\fsm.g:13:3: 'A' s2
                    pass 
                    self.match(self.input, 6, self.FOLLOW_6_in_s176)
                    self._state.following.append(self.FOLLOW_s2_in_s178)
                    self.s2()

                    self._state.following.pop()



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "s1"


    # $ANTLR start "s2"
    # .\\static\\antlr\\fsm.g:15:1: s2 : ( '#' s1 | 'B' s1 );
    def s2(self, ):

        try:
            try:
                # .\\static\\antlr\\fsm.g:15:4: ( '#' s1 | 'B' s1 )
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 4) :
                    alt4 = 1
                elif (LA4_0 == 8) :
                    alt4 = 2
                else:
                    if self._state.backtracking > 0:
                        raise BacktrackingFailed

                    nvae = NoViableAltException("", 4, 0, self.input)

                    raise nvae

                if alt4 == 1:
                    # .\\static\\antlr\\fsm.g:15:6: '#' s1
                    pass 
                    self.match(self.input, 4, self.FOLLOW_4_in_s286)
                    self._state.following.append(self.FOLLOW_s1_in_s288)
                    self.s1()

                    self._state.following.pop()


                elif alt4 == 2:
                    # .\\static\\antlr\\fsm.g:16:3: 'B' s1
                    pass 
                    self.match(self.input, 8, self.FOLLOW_8_in_s292)
                    self._state.following.append(self.FOLLOW_s1_in_s294)
                    self.s1()

                    self._state.following.pop()



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return 

    # $ANTLR end "s2"

    # $ANTLR start "synpred1_fsm"
    def synpred1_fsm_fragment(self, ):
        # .\\static\\antlr\\fsm.g:3:9: ( '#' s1 )
        # .\\static\\antlr\\fsm.g:3:9: '#' s1
        pass 
        self.match(self.input, 4, self.FOLLOW_4_in_synpred1_fsm20)
        self._state.following.append(self.FOLLOW_s1_in_synpred1_fsm22)
        self.s1()

        self._state.following.pop()


    # $ANTLR end "synpred1_fsm"



    # $ANTLR start "synpred3_fsm"
    def synpred3_fsm_fragment(self, ):
        # .\\static\\antlr\\fsm.g:5:3: ( '#' s0 )
        # .\\static\\antlr\\fsm.g:5:3: '#' s0
        pass 
        self.match(self.input, 4, self.FOLLOW_4_in_synpred3_fsm32)
        self._state.following.append(self.FOLLOW_s0_in_synpred3_fsm34)
        self.s0()

        self._state.following.pop()


    # $ANTLR end "synpred3_fsm"




    # Delegated rules

    def synpred3_fsm(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred3_fsm_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success

    def synpred1_fsm(self):
        self._state.backtracking += 1
        start = self.input.mark()
        try:
            self.synpred1_fsm_fragment()
        except BacktrackingFailed:
            success = False
        else:
            success = True
        self.input.rewind(start)
        self._state.backtracking -= 1
        return success



 

    FOLLOW_4_in_start20 = frozenset([4, 6])
    FOLLOW_s1_in_start22 = frozenset([1])
    FOLLOW_5_in_start26 = frozenset([4, 6])
    FOLLOW_s1_in_start28 = frozenset([1])
    FOLLOW_4_in_start32 = frozenset([4, 8])
    FOLLOW_s0_in_start34 = frozenset([1])
    FOLLOW_6_in_start38 = frozenset([4, 8])
    FOLLOW_s0_in_start40 = frozenset([1])
    FOLLOW_7_in_start44 = frozenset([4, 8])
    FOLLOW_s0_in_start46 = frozenset([1])
    FOLLOW_4_in_s054 = frozenset([4, 6])
    FOLLOW_s1_in_s056 = frozenset([1])
    FOLLOW_8_in_s060 = frozenset([4, 6])
    FOLLOW_s1_in_s062 = frozenset([1])
    FOLLOW_4_in_s170 = frozenset([4, 8])
    FOLLOW_s2_in_s172 = frozenset([1])
    FOLLOW_6_in_s176 = frozenset([4, 8])
    FOLLOW_s2_in_s178 = frozenset([1])
    FOLLOW_4_in_s286 = frozenset([4, 6])
    FOLLOW_s1_in_s288 = frozenset([1])
    FOLLOW_8_in_s292 = frozenset([4, 6])
    FOLLOW_s1_in_s294 = frozenset([1])
    FOLLOW_4_in_synpred1_fsm20 = frozenset([4, 6])
    FOLLOW_s1_in_synpred1_fsm22 = frozenset([1])
    FOLLOW_4_in_synpred3_fsm32 = frozenset([4, 8])
    FOLLOW_s0_in_synpred3_fsm34 = frozenset([1])



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import ParserMain
    main = ParserMain("fsmLexer", fsmParser)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)

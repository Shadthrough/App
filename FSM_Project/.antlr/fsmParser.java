// Generated from c:\Users\maxim\Desktop\Subj\Diplom\App\FSM_Project\fsm.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class fsmParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11;
	public static final int
		RULE_expr = 0, RULE_start = 1, RULE_s0 = 2, RULE_s4 = 3, RULE_s2 = 4, 
		RULE_s1 = 5, RULE_s3 = 6, RULE_s5 = 7, RULE_s8 = 8, RULE_s7 = 9, RULE_s6 = 10, 
		RULE_s9 = 11, RULE_s10 = 12;
	private static String[] makeRuleNames() {
		return new String[] {
			"expr", "start", "s0", "s4", "s2", "s1", "s3", "s5", "s8", "s7", "s6", 
			"s9", "s10"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'#'", "'L'", "'S'", "'C'", "'K'", "'D'", "'R'", "'A'", "'U'", 
			"'T'", "'t'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "fsm.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }


	paths = []

	public fsmParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ExprContext extends ParserRuleContext {
		public StartContext start() {
			return getRuleContext(StartContext.class,0);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(26);
			start();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StartContext extends ParserRuleContext {
		public StartContext start() {
			return getRuleContext(StartContext.class,0);
		}
		public S0Context s0() {
			return getRuleContext(S0Context.class,0);
		}
		public TerminalNode EOF() { return getToken(fsmParser.EOF, 0); }
		public S4Context s4() {
			return getRuleContext(S4Context.class,0);
		}
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_start);
		try {
			setState(48);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(28);
				match(T__0);
				setState(29);
				start();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(30);
				match(T__0);
				setState(31);
				s0();
				self.paths.append('-L>s0')
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(34);
				match(EOF);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(35);
				match(T__1);
				setState(36);
				s0();
				self.paths.append('-L>s0')
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(39);
				match(T__0);
				setState(40);
				s4();
				self.paths.append('-S>s4')
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(43);
				match(EOF);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(44);
				match(T__2);
				setState(45);
				s4();
				self.paths.append('-S>s4')
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class S0Context extends ParserRuleContext {
		public S0Context s0() {
			return getRuleContext(S0Context.class,0);
		}
		public StartContext start() {
			return getRuleContext(StartContext.class,0);
		}
		public S2Context s2() {
			return getRuleContext(S2Context.class,0);
		}
		public S4Context s4() {
			return getRuleContext(S4Context.class,0);
		}
		public S0Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_s0; }
	}

	public final S0Context s0() throws RecognitionException {
		S0Context _localctx = new S0Context(_ctx, getState());
		enterRule(_localctx, 4, RULE_s0);
		try {
			setState(76);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(50);
				match(T__0);
				setState(51);
				s0();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(52);
				match(T__0);
				setState(53);
				start();
				self.paths.append('-C>start')
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(56);
				match(T__3);
				setState(57);
				start();
				self.paths.append('-C>start')
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(60);
				match(T__0);
				setState(61);
				s2();
				self.paths.append('-K>s2')
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(64);
				match(T__4);
				setState(65);
				s2();
				self.paths.append('-K>s2')
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(68);
				match(T__0);
				setState(69);
				s4();
				self.paths.append('-S>s4')
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(72);
				match(T__2);
				setState(73);
				s4();
				self.paths.append('-S>s4')
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class S4Context extends ParserRuleContext {
		public S4Context s4() {
			return getRuleContext(S4Context.class,0);
		}
		public StartContext start() {
			return getRuleContext(StartContext.class,0);
		}
		public S2Context s2() {
			return getRuleContext(S2Context.class,0);
		}
		public S1Context s1() {
			return getRuleContext(S1Context.class,0);
		}
		public S4Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_s4; }
	}

	public final S4Context s4() throws RecognitionException {
		S4Context _localctx = new S4Context(_ctx, getState());
		enterRule(_localctx, 6, RULE_s4);
		try {
			setState(104);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(78);
				match(T__0);
				setState(79);
				s4();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(80);
				match(T__0);
				setState(81);
				start();
				self.paths.append('-C>start')
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(84);
				match(T__3);
				setState(85);
				start();
				self.paths.append('-C>start')
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(88);
				match(T__0);
				setState(89);
				s2();
				self.paths.append('-K>s2')
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(92);
				match(T__4);
				setState(93);
				s2();
				self.paths.append('-K>s2')
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(96);
				match(T__0);
				setState(97);
				s1();
				self.paths.append('-D>s1')
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(100);
				match(T__5);
				setState(101);
				s1();
				self.paths.append('-D>s1')
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class S2Context extends ParserRuleContext {
		public S2Context s2() {
			return getRuleContext(S2Context.class,0);
		}
		public S0Context s0() {
			return getRuleContext(S0Context.class,0);
		}
		public S1Context s1() {
			return getRuleContext(S1Context.class,0);
		}
		public S5Context s5() {
			return getRuleContext(S5Context.class,0);
		}
		public S2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_s2; }
	}

	public final S2Context s2() throws RecognitionException {
		S2Context _localctx = new S2Context(_ctx, getState());
		enterRule(_localctx, 8, RULE_s2);
		try {
			setState(132);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(106);
				match(T__0);
				setState(107);
				s2();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(108);
				match(T__0);
				setState(109);
				s0();
				self.paths.append('-R>s0')
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(112);
				match(T__6);
				setState(113);
				s0();
				self.paths.append('-R>s0')
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(116);
				match(T__0);
				setState(117);
				s1();
				self.paths.append('-A>s1')
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(120);
				match(T__7);
				setState(121);
				s1();
				self.paths.append('-A>s1')
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(124);
				match(T__0);
				setState(125);
				s5();
				self.paths.append('-L>s5')
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(128);
				match(T__1);
				setState(129);
				s5();
				self.paths.append('-L>s5')
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class S1Context extends ParserRuleContext {
		public S1Context s1() {
			return getRuleContext(S1Context.class,0);
		}
		public S5Context s5() {
			return getRuleContext(S5Context.class,0);
		}
		public TerminalNode EOF() { return getToken(fsmParser.EOF, 0); }
		public S3Context s3() {
			return getRuleContext(S3Context.class,0);
		}
		public S1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_s1; }
	}

	public final S1Context s1() throws RecognitionException {
		S1Context _localctx = new S1Context(_ctx, getState());
		enterRule(_localctx, 10, RULE_s1);
		try {
			setState(154);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(134);
				match(T__0);
				setState(135);
				s1();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(136);
				match(T__0);
				setState(137);
				s5();
				self.paths.append('-L>s5')
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(140);
				match(EOF);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(141);
				match(T__1);
				setState(142);
				s5();
				self.paths.append('-L>s5')
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(145);
				match(T__0);
				setState(146);
				s3();
				self.paths.append('-U>s3')
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(149);
				match(EOF);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(150);
				match(T__8);
				setState(151);
				s3();
				self.paths.append('-U>s3')
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class S3Context extends ParserRuleContext {
		public S3Context s3() {
			return getRuleContext(S3Context.class,0);
		}
		public S6Context s6() {
			return getRuleContext(S6Context.class,0);
		}
		public S3Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_s3; }
	}

	public final S3Context s3() throws RecognitionException {
		S3Context _localctx = new S3Context(_ctx, getState());
		enterRule(_localctx, 12, RULE_s3);
		try {
			setState(166);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(156);
				match(T__0);
				setState(157);
				s3();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(158);
				match(T__0);
				setState(159);
				s6();
				self.paths.append('-L>s6')
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(162);
				match(T__1);
				setState(163);
				s6();
				self.paths.append('-L>s6')
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class S5Context extends ParserRuleContext {
		public S5Context s5() {
			return getRuleContext(S5Context.class,0);
		}
		public S8Context s8() {
			return getRuleContext(S8Context.class,0);
		}
		public S9Context s9() {
			return getRuleContext(S9Context.class,0);
		}
		public S7Context s7() {
			return getRuleContext(S7Context.class,0);
		}
		public S5Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_s5; }
	}

	public final S5Context s5() throws RecognitionException {
		S5Context _localctx = new S5Context(_ctx, getState());
		enterRule(_localctx, 14, RULE_s5);
		try {
			setState(194);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(168);
				match(T__0);
				setState(169);
				s5();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(170);
				match(T__0);
				setState(171);
				s8();
				self.paths.append('-L>s8')
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(174);
				match(T__1);
				setState(175);
				s8();
				self.paths.append('-L>s8')
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(178);
				match(T__0);
				setState(179);
				s9();
				self.paths.append('-T>s9')
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(182);
				match(T__9);
				setState(183);
				s9();
				self.paths.append('-T>s9')
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(186);
				match(T__0);
				setState(187);
				s7();
				self.paths.append('-A>s7')
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(190);
				match(T__7);
				setState(191);
				s7();
				self.paths.append('-A>s7')
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class S8Context extends ParserRuleContext {
		public S8Context s8() {
			return getRuleContext(S8Context.class,0);
		}
		public S9Context s9() {
			return getRuleContext(S9Context.class,0);
		}
		public S8Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_s8; }
	}

	public final S8Context s8() throws RecognitionException {
		S8Context _localctx = new S8Context(_ctx, getState());
		enterRule(_localctx, 16, RULE_s8);
		try {
			setState(206);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(196);
				match(T__0);
				setState(197);
				s8();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(198);
				match(T__0);
				setState(199);
				s9();
				self.paths.append('-A>s9')
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(202);
				match(T__7);
				setState(203);
				s9();
				self.paths.append('-A>s9')
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class S7Context extends ParserRuleContext {
		public S7Context s7() {
			return getRuleContext(S7Context.class,0);
		}
		public S9Context s9() {
			return getRuleContext(S9Context.class,0);
		}
		public S7Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_s7; }
	}

	public final S7Context s7() throws RecognitionException {
		S7Context _localctx = new S7Context(_ctx, getState());
		enterRule(_localctx, 18, RULE_s7);
		try {
			setState(218);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(208);
				match(T__0);
				setState(209);
				s7();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(210);
				match(T__0);
				setState(211);
				s9();
				self.paths.append('-U>s9')
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(214);
				match(T__8);
				setState(215);
				s9();
				self.paths.append('-U>s9')
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class S6Context extends ParserRuleContext {
		public S6Context s6() {
			return getRuleContext(S6Context.class,0);
		}
		public S10Context s10() {
			return getRuleContext(S10Context.class,0);
		}
		public S6Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_s6; }
	}

	public final S6Context s6() throws RecognitionException {
		S6Context _localctx = new S6Context(_ctx, getState());
		enterRule(_localctx, 20, RULE_s6);
		try {
			setState(230);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(220);
				match(T__0);
				setState(221);
				s6();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(222);
				match(T__0);
				setState(223);
				s10();
				self.paths.append('-A>s10')
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(226);
				match(T__7);
				setState(227);
				s10();
				self.paths.append('-A>s10')
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class S9Context extends ParserRuleContext {
		public S9Context s9() {
			return getRuleContext(S9Context.class,0);
		}
		public S10Context s10() {
			return getRuleContext(S10Context.class,0);
		}
		public S9Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_s9; }
	}

	public final S9Context s9() throws RecognitionException {
		S9Context _localctx = new S9Context(_ctx, getState());
		enterRule(_localctx, 22, RULE_s9);
		try {
			setState(242);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(232);
				match(T__0);
				setState(233);
				s9();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(234);
				match(T__0);
				setState(235);
				s10();
				self.paths.append('-t>s10')
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(238);
				match(T__10);
				setState(239);
				s10();
				self.paths.append('-t>s10')
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class S10Context extends ParserRuleContext {
		public S10Context s10() {
			return getRuleContext(S10Context.class,0);
		}
		public TerminalNode EOF() { return getToken(fsmParser.EOF, 0); }
		public S10Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_s10; }
	}

	public final S10Context s10() throws RecognitionException {
		S10Context _localctx = new S10Context(_ctx, getState());
		enterRule(_localctx, 24, RULE_s10);
		try {
			setState(247);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				enterOuterAlt(_localctx, 1);
				{
				setState(244);
				match(T__0);
				setState(245);
				s10();
				}
				break;
			case EOF:
				enterOuterAlt(_localctx, 2);
				{
				setState(246);
				match(EOF);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r\u00fc\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\63\n\3\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4"+
		"\3\4\3\4\3\4\3\4\3\4\3\4\5\4O\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5"+
		"\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5"+
		"\5k\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0087\n\6\3\7\3\7\3\7\3"+
		"\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7"+
		"\u009d\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00a9\n\b\3\t\3"+
		"\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00c5\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n"+
		"\3\n\3\n\3\n\5\n\u00d1\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13"+
		"\3\13\5\13\u00dd\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00e9"+
		"\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00f5\n\r\3\16\3\16\3"+
		"\16\5\16\u00fa\n\16\3\16\2\2\17\2\4\6\b\n\f\16\20\22\24\26\30\32\2\2\2"+
		"\u011d\2\34\3\2\2\2\4\62\3\2\2\2\6N\3\2\2\2\bj\3\2\2\2\n\u0086\3\2\2\2"+
		"\f\u009c\3\2\2\2\16\u00a8\3\2\2\2\20\u00c4\3\2\2\2\22\u00d0\3\2\2\2\24"+
		"\u00dc\3\2\2\2\26\u00e8\3\2\2\2\30\u00f4\3\2\2\2\32\u00f9\3\2\2\2\34\35"+
		"\5\4\3\2\35\3\3\2\2\2\36\37\7\3\2\2\37\63\5\4\3\2 !\7\3\2\2!\"\5\6\4\2"+
		"\"#\b\3\1\2#\63\3\2\2\2$\63\7\2\2\3%&\7\4\2\2&\'\5\6\4\2\'(\b\3\1\2(\63"+
		"\3\2\2\2)*\7\3\2\2*+\5\b\5\2+,\b\3\1\2,\63\3\2\2\2-\63\7\2\2\3./\7\5\2"+
		"\2/\60\5\b\5\2\60\61\b\3\1\2\61\63\3\2\2\2\62\36\3\2\2\2\62 \3\2\2\2\62"+
		"$\3\2\2\2\62%\3\2\2\2\62)\3\2\2\2\62-\3\2\2\2\62.\3\2\2\2\63\5\3\2\2\2"+
		"\64\65\7\3\2\2\65O\5\6\4\2\66\67\7\3\2\2\678\5\4\3\289\b\4\1\29O\3\2\2"+
		"\2:;\7\6\2\2;<\5\4\3\2<=\b\4\1\2=O\3\2\2\2>?\7\3\2\2?@\5\n\6\2@A\b\4\1"+
		"\2AO\3\2\2\2BC\7\7\2\2CD\5\n\6\2DE\b\4\1\2EO\3\2\2\2FG\7\3\2\2GH\5\b\5"+
		"\2HI\b\4\1\2IO\3\2\2\2JK\7\5\2\2KL\5\b\5\2LM\b\4\1\2MO\3\2\2\2N\64\3\2"+
		"\2\2N\66\3\2\2\2N:\3\2\2\2N>\3\2\2\2NB\3\2\2\2NF\3\2\2\2NJ\3\2\2\2O\7"+
		"\3\2\2\2PQ\7\3\2\2Qk\5\b\5\2RS\7\3\2\2ST\5\4\3\2TU\b\5\1\2Uk\3\2\2\2V"+
		"W\7\6\2\2WX\5\4\3\2XY\b\5\1\2Yk\3\2\2\2Z[\7\3\2\2[\\\5\n\6\2\\]\b\5\1"+
		"\2]k\3\2\2\2^_\7\7\2\2_`\5\n\6\2`a\b\5\1\2ak\3\2\2\2bc\7\3\2\2cd\5\f\7"+
		"\2de\b\5\1\2ek\3\2\2\2fg\7\b\2\2gh\5\f\7\2hi\b\5\1\2ik\3\2\2\2jP\3\2\2"+
		"\2jR\3\2\2\2jV\3\2\2\2jZ\3\2\2\2j^\3\2\2\2jb\3\2\2\2jf\3\2\2\2k\t\3\2"+
		"\2\2lm\7\3\2\2m\u0087\5\n\6\2no\7\3\2\2op\5\6\4\2pq\b\6\1\2q\u0087\3\2"+
		"\2\2rs\7\t\2\2st\5\6\4\2tu\b\6\1\2u\u0087\3\2\2\2vw\7\3\2\2wx\5\f\7\2"+
		"xy\b\6\1\2y\u0087\3\2\2\2z{\7\n\2\2{|\5\f\7\2|}\b\6\1\2}\u0087\3\2\2\2"+
		"~\177\7\3\2\2\177\u0080\5\20\t\2\u0080\u0081\b\6\1\2\u0081\u0087\3\2\2"+
		"\2\u0082\u0083\7\4\2\2\u0083\u0084\5\20\t\2\u0084\u0085\b\6\1\2\u0085"+
		"\u0087\3\2\2\2\u0086l\3\2\2\2\u0086n\3\2\2\2\u0086r\3\2\2\2\u0086v\3\2"+
		"\2\2\u0086z\3\2\2\2\u0086~\3\2\2\2\u0086\u0082\3\2\2\2\u0087\13\3\2\2"+
		"\2\u0088\u0089\7\3\2\2\u0089\u009d\5\f\7\2\u008a\u008b\7\3\2\2\u008b\u008c"+
		"\5\20\t\2\u008c\u008d\b\7\1\2\u008d\u009d\3\2\2\2\u008e\u009d\7\2\2\3"+
		"\u008f\u0090\7\4\2\2\u0090\u0091\5\20\t\2\u0091\u0092\b\7\1\2\u0092\u009d"+
		"\3\2\2\2\u0093\u0094\7\3\2\2\u0094\u0095\5\16\b\2\u0095\u0096\b\7\1\2"+
		"\u0096\u009d\3\2\2\2\u0097\u009d\7\2\2\3\u0098\u0099\7\13\2\2\u0099\u009a"+
		"\5\16\b\2\u009a\u009b\b\7\1\2\u009b\u009d\3\2\2\2\u009c\u0088\3\2\2\2"+
		"\u009c\u008a\3\2\2\2\u009c\u008e\3\2\2\2\u009c\u008f\3\2\2\2\u009c\u0093"+
		"\3\2\2\2\u009c\u0097\3\2\2\2\u009c\u0098\3\2\2\2\u009d\r\3\2\2\2\u009e"+
		"\u009f\7\3\2\2\u009f\u00a9\5\16\b\2\u00a0\u00a1\7\3\2\2\u00a1\u00a2\5"+
		"\26\f\2\u00a2\u00a3\b\b\1\2\u00a3\u00a9\3\2\2\2\u00a4\u00a5\7\4\2\2\u00a5"+
		"\u00a6\5\26\f\2\u00a6\u00a7\b\b\1\2\u00a7\u00a9\3\2\2\2\u00a8\u009e\3"+
		"\2\2\2\u00a8\u00a0\3\2\2\2\u00a8\u00a4\3\2\2\2\u00a9\17\3\2\2\2\u00aa"+
		"\u00ab\7\3\2\2\u00ab\u00c5\5\20\t\2\u00ac\u00ad\7\3\2\2\u00ad\u00ae\5"+
		"\22\n\2\u00ae\u00af\b\t\1\2\u00af\u00c5\3\2\2\2\u00b0\u00b1\7\4\2\2\u00b1"+
		"\u00b2\5\22\n\2\u00b2\u00b3\b\t\1\2\u00b3\u00c5\3\2\2\2\u00b4\u00b5\7"+
		"\3\2\2\u00b5\u00b6\5\30\r\2\u00b6\u00b7\b\t\1\2\u00b7\u00c5\3\2\2\2\u00b8"+
		"\u00b9\7\f\2\2\u00b9\u00ba\5\30\r\2\u00ba\u00bb\b\t\1\2\u00bb\u00c5\3"+
		"\2\2\2\u00bc\u00bd\7\3\2\2\u00bd\u00be\5\24\13\2\u00be\u00bf\b\t\1\2\u00bf"+
		"\u00c5\3\2\2\2\u00c0\u00c1\7\n\2\2\u00c1\u00c2\5\24\13\2\u00c2\u00c3\b"+
		"\t\1\2\u00c3\u00c5\3\2\2\2\u00c4\u00aa\3\2\2\2\u00c4\u00ac\3\2\2\2\u00c4"+
		"\u00b0\3\2\2\2\u00c4\u00b4\3\2\2\2\u00c4\u00b8\3\2\2\2\u00c4\u00bc\3\2"+
		"\2\2\u00c4\u00c0\3\2\2\2\u00c5\21\3\2\2\2\u00c6\u00c7\7\3\2\2\u00c7\u00d1"+
		"\5\22\n\2\u00c8\u00c9\7\3\2\2\u00c9\u00ca\5\30\r\2\u00ca\u00cb\b\n\1\2"+
		"\u00cb\u00d1\3\2\2\2\u00cc\u00cd\7\n\2\2\u00cd\u00ce\5\30\r\2\u00ce\u00cf"+
		"\b\n\1\2\u00cf\u00d1\3\2\2\2\u00d0\u00c6\3\2\2\2\u00d0\u00c8\3\2\2\2\u00d0"+
		"\u00cc\3\2\2\2\u00d1\23\3\2\2\2\u00d2\u00d3\7\3\2\2\u00d3\u00dd\5\24\13"+
		"\2\u00d4\u00d5\7\3\2\2\u00d5\u00d6\5\30\r\2\u00d6\u00d7\b\13\1\2\u00d7"+
		"\u00dd\3\2\2\2\u00d8\u00d9\7\13\2\2\u00d9\u00da\5\30\r\2\u00da\u00db\b"+
		"\13\1\2\u00db\u00dd\3\2\2\2\u00dc\u00d2\3\2\2\2\u00dc\u00d4\3\2\2\2\u00dc"+
		"\u00d8\3\2\2\2\u00dd\25\3\2\2\2\u00de\u00df\7\3\2\2\u00df\u00e9\5\26\f"+
		"\2\u00e0\u00e1\7\3\2\2\u00e1\u00e2\5\32\16\2\u00e2\u00e3\b\f\1\2\u00e3"+
		"\u00e9\3\2\2\2\u00e4\u00e5\7\n\2\2\u00e5\u00e6\5\32\16\2\u00e6\u00e7\b"+
		"\f\1\2\u00e7\u00e9\3\2\2\2\u00e8\u00de\3\2\2\2\u00e8\u00e0\3\2\2\2\u00e8"+
		"\u00e4\3\2\2\2\u00e9\27\3\2\2\2\u00ea\u00eb\7\3\2\2\u00eb\u00f5\5\30\r"+
		"\2\u00ec\u00ed\7\3\2\2\u00ed\u00ee\5\32\16\2\u00ee\u00ef\b\r\1\2\u00ef"+
		"\u00f5\3\2\2\2\u00f0\u00f1\7\r\2\2\u00f1\u00f2\5\32\16\2\u00f2\u00f3\b"+
		"\r\1\2\u00f3\u00f5\3\2\2\2\u00f4\u00ea\3\2\2\2\u00f4\u00ec\3\2\2\2\u00f4"+
		"\u00f0\3\2\2\2\u00f5\31\3\2\2\2\u00f6\u00f7\7\3\2\2\u00f7\u00fa\5\32\16"+
		"\2\u00f8\u00fa\7\2\2\3\u00f9\u00f6\3\2\2\2\u00f9\u00f8\3\2\2\2\u00fa\33"+
		"\3\2\2\2\16\62Nj\u0086\u009c\u00a8\u00c4\u00d0\u00dc\u00e8\u00f4\u00f9";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
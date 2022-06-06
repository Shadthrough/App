// Generated from .\static\antlr\fsm.g4 by ANTLR 4.10.1
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
	static { RuntimeMetaData.checkVersion("4.10.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4;
	public static final int
		RULE_expr = 0, RULE_start = 1, RULE_s0 = 2, RULE_s1 = 3, RULE_s2 = 4;
	private static String[] makeRuleNames() {
		return new String[] {
			"expr", "start", "s0", "s1", "s2"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'#'", "'A'", "'x'", "'B'"
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof fsmListener ) ((fsmListener)listener).enterExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof fsmListener ) ((fsmListener)listener).exitExpr(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_expr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(10);
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
		public S0Context s0() {
			return getRuleContext(S0Context.class,0);
		}
		public StartContext start() {
			return getRuleContext(StartContext.class,0);
		}
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof fsmListener ) ((fsmListener)listener).enterStart(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof fsmListener ) ((fsmListener)listener).exitStart(this);
		}
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_start);
		try {
			setState(20);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(12);
				match(T__0);
				setState(13);
				s0();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(14);
				match(T__0);
				setState(15);
				start();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(16);
				match(T__1);
				setState(17);
				s0();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(18);
				match(T__2);
				setState(19);
				s0();
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
		public S1Context s1() {
			return getRuleContext(S1Context.class,0);
		}
		public S0Context s0() {
			return getRuleContext(S0Context.class,0);
		}
		public S0Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_s0; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof fsmListener ) ((fsmListener)listener).enterS0(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof fsmListener ) ((fsmListener)listener).exitS0(this);
		}
	}

	public final S0Context s0() throws RecognitionException {
		S0Context _localctx = new S0Context(_ctx, getState());
		enterRule(_localctx, 4, RULE_s0);
		try {
			setState(28);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(22);
				match(T__0);
				setState(23);
				s1();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(24);
				match(T__0);
				setState(25);
				s0();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(26);
				match(T__3);
				setState(27);
				s1();
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
		public S2Context s2() {
			return getRuleContext(S2Context.class,0);
		}
		public S1Context s1() {
			return getRuleContext(S1Context.class,0);
		}
		public TerminalNode EOF() { return getToken(fsmParser.EOF, 0); }
		public S1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_s1; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof fsmListener ) ((fsmListener)listener).enterS1(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof fsmListener ) ((fsmListener)listener).exitS1(this);
		}
	}

	public final S1Context s1() throws RecognitionException {
		S1Context _localctx = new S1Context(_ctx, getState());
		enterRule(_localctx, 6, RULE_s1);
		try {
			setState(37);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(30);
				match(T__0);
				setState(31);
				s2();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(32);
				match(T__0);
				setState(33);
				s1();
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
				s2();
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
		public S1Context s1() {
			return getRuleContext(S1Context.class,0);
		}
		public S2Context s2() {
			return getRuleContext(S2Context.class,0);
		}
		public S2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_s2; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof fsmListener ) ((fsmListener)listener).enterS2(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof fsmListener ) ((fsmListener)listener).exitS2(this);
		}
	}

	public final S2Context s2() throws RecognitionException {
		S2Context _localctx = new S2Context(_ctx, getState());
		enterRule(_localctx, 8, RULE_s2);
		try {
			setState(45);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(39);
				match(T__0);
				setState(40);
				s1();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(41);
				match(T__0);
				setState(42);
				s2();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(43);
				match(T__3);
				setState(44);
				s1();
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

	public static final String _serializedATN =
		"\u0004\u0001\u00040\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0001"+
		"\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001\u0015\b\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003"+
		"\u0002\u001d\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0003\u0003&\b\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004.\b"+
		"\u0004\u0001\u0004\u0000\u0000\u0005\u0000\u0002\u0004\u0006\b\u0000\u0000"+
		"4\u0000\n\u0001\u0000\u0000\u0000\u0002\u0014\u0001\u0000\u0000\u0000"+
		"\u0004\u001c\u0001\u0000\u0000\u0000\u0006%\u0001\u0000\u0000\u0000\b"+
		"-\u0001\u0000\u0000\u0000\n\u000b\u0003\u0002\u0001\u0000\u000b\u0001"+
		"\u0001\u0000\u0000\u0000\f\r\u0005\u0001\u0000\u0000\r\u0015\u0003\u0004"+
		"\u0002\u0000\u000e\u000f\u0005\u0001\u0000\u0000\u000f\u0015\u0003\u0002"+
		"\u0001\u0000\u0010\u0011\u0005\u0002\u0000\u0000\u0011\u0015\u0003\u0004"+
		"\u0002\u0000\u0012\u0013\u0005\u0003\u0000\u0000\u0013\u0015\u0003\u0004"+
		"\u0002\u0000\u0014\f\u0001\u0000\u0000\u0000\u0014\u000e\u0001\u0000\u0000"+
		"\u0000\u0014\u0010\u0001\u0000\u0000\u0000\u0014\u0012\u0001\u0000\u0000"+
		"\u0000\u0015\u0003\u0001\u0000\u0000\u0000\u0016\u0017\u0005\u0001\u0000"+
		"\u0000\u0017\u001d\u0003\u0006\u0003\u0000\u0018\u0019\u0005\u0001\u0000"+
		"\u0000\u0019\u001d\u0003\u0004\u0002\u0000\u001a\u001b\u0005\u0004\u0000"+
		"\u0000\u001b\u001d\u0003\u0006\u0003\u0000\u001c\u0016\u0001\u0000\u0000"+
		"\u0000\u001c\u0018\u0001\u0000\u0000\u0000\u001c\u001a\u0001\u0000\u0000"+
		"\u0000\u001d\u0005\u0001\u0000\u0000\u0000\u001e\u001f\u0005\u0001\u0000"+
		"\u0000\u001f&\u0003\b\u0004\u0000 !\u0005\u0001\u0000\u0000!&\u0003\u0006"+
		"\u0003\u0000\"&\u0005\u0000\u0000\u0001#$\u0005\u0002\u0000\u0000$&\u0003"+
		"\b\u0004\u0000%\u001e\u0001\u0000\u0000\u0000% \u0001\u0000\u0000\u0000"+
		"%\"\u0001\u0000\u0000\u0000%#\u0001\u0000\u0000\u0000&\u0007\u0001\u0000"+
		"\u0000\u0000\'(\u0005\u0001\u0000\u0000(.\u0003\u0006\u0003\u0000)*\u0005"+
		"\u0001\u0000\u0000*.\u0003\b\u0004\u0000+,\u0005\u0004\u0000\u0000,.\u0003"+
		"\u0006\u0003\u0000-\'\u0001\u0000\u0000\u0000-)\u0001\u0000\u0000\u0000"+
		"-+\u0001\u0000\u0000\u0000.\t\u0001\u0000\u0000\u0000\u0004\u0014\u001c"+
		"%-";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
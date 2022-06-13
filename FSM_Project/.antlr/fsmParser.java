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
		public StartContext start() {
			return getRuleContext(StartContext.class,0);
		}
		public S0Context s0() {
			return getRuleContext(S0Context.class,0);
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
			setState(20);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(12);
				match(T__0);
				setState(13);
				start();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(14);
				match(T__0);
				setState(15);
				s0();
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
		public S0Context s0() {
			return getRuleContext(S0Context.class,0);
		}
		public S1Context s1() {
			return getRuleContext(S1Context.class,0);
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
			setState(28);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(22);
				match(T__0);
				setState(23);
				s0();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(24);
				match(T__0);
				setState(25);
				s1();
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
		public S1Context s1() {
			return getRuleContext(S1Context.class,0);
		}
		public S2Context s2() {
			return getRuleContext(S2Context.class,0);
		}
		public TerminalNode EOF() { return getToken(fsmParser.EOF, 0); }
		public S1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_s1; }
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
				s1();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(32);
				match(T__0);
				setState(33);
				s2();
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
		public S2Context s2() {
			return getRuleContext(S2Context.class,0);
		}
		public S1Context s1() {
			return getRuleContext(S1Context.class,0);
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
			setState(45);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(39);
				match(T__0);
				setState(40);
				s2();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(41);
				match(T__0);
				setState(42);
				s1();
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\6\62\4\2\t\2\4\3"+
		"\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5"+
		"\3\27\n\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4\37\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3"+
		"\5\5\5(\n\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6\60\n\6\3\6\2\2\7\2\4\6\b\n\2\2"+
		"\2\66\2\f\3\2\2\2\4\26\3\2\2\2\6\36\3\2\2\2\b\'\3\2\2\2\n/\3\2\2\2\f\r"+
		"\5\4\3\2\r\3\3\2\2\2\16\17\7\3\2\2\17\27\5\4\3\2\20\21\7\3\2\2\21\27\5"+
		"\6\4\2\22\23\7\4\2\2\23\27\5\6\4\2\24\25\7\5\2\2\25\27\5\6\4\2\26\16\3"+
		"\2\2\2\26\20\3\2\2\2\26\22\3\2\2\2\26\24\3\2\2\2\27\5\3\2\2\2\30\31\7"+
		"\3\2\2\31\37\5\6\4\2\32\33\7\3\2\2\33\37\5\b\5\2\34\35\7\6\2\2\35\37\5"+
		"\b\5\2\36\30\3\2\2\2\36\32\3\2\2\2\36\34\3\2\2\2\37\7\3\2\2\2 !\7\3\2"+
		"\2!(\5\b\5\2\"#\7\3\2\2#(\5\n\6\2$(\7\2\2\3%&\7\4\2\2&(\5\n\6\2\' \3\2"+
		"\2\2\'\"\3\2\2\2\'$\3\2\2\2\'%\3\2\2\2(\t\3\2\2\2)*\7\3\2\2*\60\5\n\6"+
		"\2+,\7\3\2\2,\60\5\b\5\2-.\7\6\2\2.\60\5\b\5\2/)\3\2\2\2/+\3\2\2\2/-\3"+
		"\2\2\2\60\13\3\2\2\2\6\26\36\'/";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
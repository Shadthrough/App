// Generated from .\fsm.g4 by ANTLR 4.10.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link fsmParser}.
 */
public interface fsmListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link fsmParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(fsmParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link fsmParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(fsmParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link fsmParser#start}.
	 * @param ctx the parse tree
	 */
	void enterStart(fsmParser.StartContext ctx);
	/**
	 * Exit a parse tree produced by {@link fsmParser#start}.
	 * @param ctx the parse tree
	 */
	void exitStart(fsmParser.StartContext ctx);
	/**
	 * Enter a parse tree produced by {@link fsmParser#s0}.
	 * @param ctx the parse tree
	 */
	void enterS0(fsmParser.S0Context ctx);
	/**
	 * Exit a parse tree produced by {@link fsmParser#s0}.
	 * @param ctx the parse tree
	 */
	void exitS0(fsmParser.S0Context ctx);
	/**
	 * Enter a parse tree produced by {@link fsmParser#s1}.
	 * @param ctx the parse tree
	 */
	void enterS1(fsmParser.S1Context ctx);
	/**
	 * Exit a parse tree produced by {@link fsmParser#s1}.
	 * @param ctx the parse tree
	 */
	void exitS1(fsmParser.S1Context ctx);
	/**
	 * Enter a parse tree produced by {@link fsmParser#s2}.
	 * @param ctx the parse tree
	 */
	void enterS2(fsmParser.S2Context ctx);
	/**
	 * Exit a parse tree produced by {@link fsmParser#s2}.
	 * @param ctx the parse tree
	 */
	void exitS2(fsmParser.S2Context ctx);
}
# Generated from LabeledExpr.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("V\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\7\2\23\n\2\f\2\16\2\26\13\2\3\2\3\2\3\3\3")
        buf.write("\3\7\3\34\n\3\f\3\16\3\37\13\3\3\3\3\3\3\3\3\3\5\3%\n")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4-\n\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\bI\n\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\7\bQ\n\b\f\b\16\bT\13\b\3\b\2\3\16\t\2\4")
        buf.write("\6\b\n\f\16\2\4\3\2\5\6\3\2\7\b\2Y\2\24\3\2\2\2\4\35\3")
        buf.write("\2\2\2\6,\3\2\2\2\b.\3\2\2\2\n\67\3\2\2\2\f<\3\2\2\2\16")
        buf.write("H\3\2\2\2\20\23\5\b\5\2\21\23\5\6\4\2\22\20\3\2\2\2\22")
        buf.write("\21\3\2\2\2\23\26\3\2\2\2\24\22\3\2\2\2\24\25\3\2\2\2")
        buf.write("\25\27\3\2\2\2\26\24\3\2\2\2\27\30\7\2\2\3\30\3\3\2\2")
        buf.write("\2\31\34\5\6\4\2\32\34\5\b\5\2\33\31\3\2\2\2\33\32\3\2")
        buf.write("\2\2\34\37\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36$\3\2")
        buf.write("\2\2\37\35\3\2\2\2 !\7\f\2\2!\"\5\16\b\2\"#\7\22\2\2#")
        buf.write("%\3\2\2\2$ \3\2\2\2$%\3\2\2\2%\5\3\2\2\2&\'\5\f\7\2\'")
        buf.write("(\7\22\2\2(-\3\2\2\2)*\5\n\6\2*+\7\22\2\2+-\3\2\2\2,&")
        buf.write("\3\2\2\2,)\3\2\2\2-\7\3\2\2\2./\7\t\2\2/\60\7\20\2\2\60")
        buf.write("\61\7\3\2\2\61\62\7\20\2\2\62\63\7\4\2\2\63\64\7\n\2\2")
        buf.write("\64\65\5\4\3\2\65\66\7\13\2\2\66\t\3\2\2\2\678\7\20\2")
        buf.write("\289\7\3\2\29:\5\16\b\2:;\7\4\2\2;\13\3\2\2\2<=\7\20\2")
        buf.write("\2=>\7\21\2\2>?\5\16\b\2?\r\3\2\2\2@A\b\b\1\2AI\5\n\6")
        buf.write("\2BI\7\17\2\2CI\7\20\2\2DE\7\3\2\2EF\5\16\b\2FG\7\4\2")
        buf.write("\2GI\3\2\2\2H@\3\2\2\2HB\3\2\2\2HC\3\2\2\2HD\3\2\2\2I")
        buf.write("R\3\2\2\2JK\f\b\2\2KL\t\2\2\2LQ\5\16\b\tMN\f\7\2\2NO\t")
        buf.write("\3\2\2OQ\5\16\b\bPJ\3\2\2\2PM\3\2\2\2QT\3\2\2\2RP\3\2")
        buf.write("\2\2RS\3\2\2\2S\17\3\2\2\2TR\3\2\2\2\13\22\24\33\35$,")
        buf.write("HPR")
        return buf.getvalue()


class LabeledExprParser ( Parser ):

    grammarFileName = "LabeledExpr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'*'", "'/'", "'+'", "'-'", 
                     "'def'", "'{'", "'}'", "'return'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'='", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "DEF", "START", 
                      "END", "Return", "HELLO", "BYE", "INT", "ID", "EQUAL", 
                      "SCOL", "Space" ]

    RULE_root = 0
    RULE_block = 1
    RULE_statement = 2
    RULE_functionDecl = 3
    RULE_functionCall = 4
    RULE_assignment = 5
    RULE_expr = 6

    ruleNames =  [ "root", "block", "statement", "functionDecl", "functionCall", 
                   "assignment", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    DEF=7
    START=8
    END=9
    Return=10
    HELLO=11
    BYE=12
    INT=13
    ID=14
    EQUAL=15
    SCOL=16
    Space=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(LabeledExprParser.EOF, 0)

        def functionDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LabeledExprParser.FunctionDeclContext)
            else:
                return self.getTypedRuleContext(LabeledExprParser.FunctionDeclContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LabeledExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(LabeledExprParser.StatementContext,i)


        def getRuleIndex(self):
            return LabeledExprParser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = LabeledExprParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LabeledExprParser.DEF or _la==LabeledExprParser.ID:
                self.state = 16
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LabeledExprParser.DEF]:
                    self.state = 14
                    self.functionDecl()
                    pass
                elif token in [LabeledExprParser.ID]:
                    self.state = 15
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 21
            self.match(LabeledExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LabeledExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(LabeledExprParser.StatementContext,i)


        def functionDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LabeledExprParser.FunctionDeclContext)
            else:
                return self.getTypedRuleContext(LabeledExprParser.FunctionDeclContext,i)


        def Return(self):
            return self.getToken(LabeledExprParser.Return, 0)

        def expr(self):
            return self.getTypedRuleContext(LabeledExprParser.ExprContext,0)


        def SCOL(self):
            return self.getToken(LabeledExprParser.SCOL, 0)

        def getRuleIndex(self):
            return LabeledExprParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = LabeledExprParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LabeledExprParser.DEF or _la==LabeledExprParser.ID:
                self.state = 25
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [LabeledExprParser.ID]:
                    self.state = 23
                    self.statement()
                    pass
                elif token in [LabeledExprParser.DEF]:
                    self.state = 24
                    self.functionDecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LabeledExprParser.Return:
                self.state = 30
                self.match(LabeledExprParser.Return)
                self.state = 31
                self.expr(0)
                self.state = 32
                self.match(LabeledExprParser.SCOL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(LabeledExprParser.AssignmentContext,0)


        def SCOL(self):
            return self.getToken(LabeledExprParser.SCOL, 0)

        def functionCall(self):
            return self.getTypedRuleContext(LabeledExprParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return LabeledExprParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = LabeledExprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.assignment()
                self.state = 37
                self.match(LabeledExprParser.SCOL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.functionCall()
                self.state = 40
                self.match(LabeledExprParser.SCOL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionDeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LabeledExprParser.RULE_functionDecl

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FuncdelcExprContext(FunctionDeclContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.FunctionDeclContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DEF(self):
            return self.getToken(LabeledExprParser.DEF, 0)
        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LabeledExprParser.ID)
            else:
                return self.getToken(LabeledExprParser.ID, i)
        def START(self):
            return self.getToken(LabeledExprParser.START, 0)
        def block(self):
            return self.getTypedRuleContext(LabeledExprParser.BlockContext,0)

        def END(self):
            return self.getToken(LabeledExprParser.END, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncdelcExpr" ):
                listener.enterFuncdelcExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncdelcExpr" ):
                listener.exitFuncdelcExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdelcExpr" ):
                return visitor.visitFuncdelcExpr(self)
            else:
                return visitor.visitChildren(self)



    def functionDecl(self):

        localctx = LabeledExprParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_functionDecl)
        try:
            localctx = LabeledExprParser.FuncdelcExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(LabeledExprParser.DEF)
            self.state = 45
            self.match(LabeledExprParser.ID)
            self.state = 46
            self.match(LabeledExprParser.T__0)
            self.state = 47
            self.match(LabeledExprParser.ID)
            self.state = 48
            self.match(LabeledExprParser.T__1)
            self.state = 49
            self.match(LabeledExprParser.START)
            self.state = 50
            self.block()
            self.state = 51
            self.match(LabeledExprParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LabeledExprParser.RULE_functionCall

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IdentifierFunctionCallContext(FunctionCallContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.FunctionCallContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LabeledExprParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(LabeledExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierFunctionCall" ):
                listener.enterIdentifierFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierFunctionCall" ):
                listener.exitIdentifierFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierFunctionCall" ):
                return visitor.visitIdentifierFunctionCall(self)
            else:
                return visitor.visitChildren(self)



    def functionCall(self):

        localctx = LabeledExprParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_functionCall)
        try:
            localctx = LabeledExprParser.IdentifierFunctionCallContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(LabeledExprParser.ID)
            self.state = 54
            self.match(LabeledExprParser.T__0)
            self.state = 55
            self.expr(0)
            self.state = 56
            self.match(LabeledExprParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LabeledExprParser.RULE_assignment

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignExprContext(AssignmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.AssignmentContext
            super().__init__(parser)
            self.rid = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def EQUAL(self):
            return self.getToken(LabeledExprParser.EQUAL, 0)
        def ID(self):
            return self.getToken(LabeledExprParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(LabeledExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignExpr" ):
                listener.enterAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignExpr" ):
                listener.exitAssignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignExpr" ):
                return visitor.visitAssignExpr(self)
            else:
                return visitor.visitChildren(self)



    def assignment(self):

        localctx = LabeledExprParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignment)
        try:
            localctx = LabeledExprParser.AssignExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            localctx.rid = self.match(LabeledExprParser.ID)
            self.state = 59
            self.match(LabeledExprParser.EQUAL)
            self.state = 60
            localctx.right = self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LabeledExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class FunctionCallExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionCall(self):
            return self.getTypedRuleContext(LabeledExprParser.FunctionCallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallExpr" ):
                listener.enterFunctionCallExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallExpr" ):
                listener.exitFunctionCallExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallExpr" ):
                return visitor.visitFunctionCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LabeledExprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(LabeledExprParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LabeledExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class InfixExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LabeledExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(LabeledExprParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInfixExpr" ):
                listener.enterInfixExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInfixExpr" ):
                listener.exitInfixExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfixExpr" ):
                return visitor.visitInfixExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LabeledExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = LabeledExprParser.FunctionCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 63
                self.functionCall()
                pass

            elif la_ == 2:
                localctx = LabeledExprParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 64
                localctx.atom = self.match(LabeledExprParser.INT)
                pass

            elif la_ == 3:
                localctx = LabeledExprParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 65
                localctx.atom = self.match(LabeledExprParser.ID)
                pass

            elif la_ == 4:
                localctx = LabeledExprParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 66
                self.match(LabeledExprParser.T__0)
                self.state = 67
                self.expr(0)
                self.state = 68
                self.match(LabeledExprParser.T__1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 80
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 78
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = LabeledExprParser.InfixExprContext(self, LabeledExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 72
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 73
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==LabeledExprParser.T__2 or _la==LabeledExprParser.T__3):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 74
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = LabeledExprParser.InfixExprContext(self, LabeledExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 75
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 76
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==LabeledExprParser.T__4 or _la==LabeledExprParser.T__5):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 77
                        localctx.right = self.expr(6)
                        pass

             
                self.state = 82
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         





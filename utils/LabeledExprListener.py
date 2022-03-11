# Generated from LabeledExpr.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LabeledExprParser import LabeledExprParser
else:
    from LabeledExprParser import LabeledExprParser

# This class defines a complete listener for a parse tree produced by LabeledExprParser.
class LabeledExprListener(ParseTreeListener):

    # Enter a parse tree produced by LabeledExprParser#root.
    def enterRoot(self, ctx:LabeledExprParser.RootContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#root.
    def exitRoot(self, ctx:LabeledExprParser.RootContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#block.
    def enterBlock(self, ctx:LabeledExprParser.BlockContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#block.
    def exitBlock(self, ctx:LabeledExprParser.BlockContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#statement.
    def enterStatement(self, ctx:LabeledExprParser.StatementContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#statement.
    def exitStatement(self, ctx:LabeledExprParser.StatementContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#FuncdelcExpr.
    def enterFuncdelcExpr(self, ctx:LabeledExprParser.FuncdelcExprContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#FuncdelcExpr.
    def exitFuncdelcExpr(self, ctx:LabeledExprParser.FuncdelcExprContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#identifierFunctionCall.
    def enterIdentifierFunctionCall(self, ctx:LabeledExprParser.IdentifierFunctionCallContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#identifierFunctionCall.
    def exitIdentifierFunctionCall(self, ctx:LabeledExprParser.IdentifierFunctionCallContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#AssignExpr.
    def enterAssignExpr(self, ctx:LabeledExprParser.AssignExprContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#AssignExpr.
    def exitAssignExpr(self, ctx:LabeledExprParser.AssignExprContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#FunctionCallExpr.
    def enterFunctionCallExpr(self, ctx:LabeledExprParser.FunctionCallExprContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#FunctionCallExpr.
    def exitFunctionCallExpr(self, ctx:LabeledExprParser.FunctionCallExprContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#IdExpr.
    def enterIdExpr(self, ctx:LabeledExprParser.IdExprContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#IdExpr.
    def exitIdExpr(self, ctx:LabeledExprParser.IdExprContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#NumberExpr.
    def enterNumberExpr(self, ctx:LabeledExprParser.NumberExprContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#NumberExpr.
    def exitNumberExpr(self, ctx:LabeledExprParser.NumberExprContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#ParenExpr.
    def enterParenExpr(self, ctx:LabeledExprParser.ParenExprContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#ParenExpr.
    def exitParenExpr(self, ctx:LabeledExprParser.ParenExprContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#InfixExpr.
    def enterInfixExpr(self, ctx:LabeledExprParser.InfixExprContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#InfixExpr.
    def exitInfixExpr(self, ctx:LabeledExprParser.InfixExprContext):
        pass



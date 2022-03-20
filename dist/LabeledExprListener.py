# Generated from LabeledExpr.g4 by ANTLR 4.9.3
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


    # Enter a parse tree produced by LabeledExprParser#AssignExpr.
    def enterAssignExpr(self, ctx:LabeledExprParser.AssignExprContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#AssignExpr.
    def exitAssignExpr(self, ctx:LabeledExprParser.AssignExprContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#identifierFunctionCall.
    def enterIdentifierFunctionCall(self, ctx:LabeledExprParser.IdentifierFunctionCallContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#identifierFunctionCall.
    def exitIdentifierFunctionCall(self, ctx:LabeledExprParser.IdentifierFunctionCallContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#IfStatementExpr.
    def enterIfStatementExpr(self, ctx:LabeledExprParser.IfStatementExprContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#IfStatementExpr.
    def exitIfStatementExpr(self, ctx:LabeledExprParser.IfStatementExprContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#IfExpr.
    def enterIfExpr(self, ctx:LabeledExprParser.IfExprContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#IfExpr.
    def exitIfExpr(self, ctx:LabeledExprParser.IfExprContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#ElseIfExpr.
    def enterElseIfExpr(self, ctx:LabeledExprParser.ElseIfExprContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#ElseIfExpr.
    def exitElseIfExpr(self, ctx:LabeledExprParser.ElseIfExprContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#ElseExpr.
    def enterElseExpr(self, ctx:LabeledExprParser.ElseExprContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#ElseExpr.
    def exitElseExpr(self, ctx:LabeledExprParser.ElseExprContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#ForExpr.
    def enterForExpr(self, ctx:LabeledExprParser.ForExprContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#ForExpr.
    def exitForExpr(self, ctx:LabeledExprParser.ForExprContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#FuncdelcExpr.
    def enterFuncdelcExpr(self, ctx:LabeledExprParser.FuncdelcExprContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#FuncdelcExpr.
    def exitFuncdelcExpr(self, ctx:LabeledExprParser.FuncdelcExprContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#IdListExpr.
    def enterIdListExpr(self, ctx:LabeledExprParser.IdListExprContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#IdListExpr.
    def exitIdListExpr(self, ctx:LabeledExprParser.IdListExprContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#ExprlistExpr.
    def enterExprlistExpr(self, ctx:LabeledExprParser.ExprlistExprContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#ExprlistExpr.
    def exitExprlistExpr(self, ctx:LabeledExprParser.ExprlistExprContext):
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


    # Enter a parse tree produced by LabeledExprParser#listExpression.
    def enterListExpression(self, ctx:LabeledExprParser.ListExpressionContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#listExpression.
    def exitListExpression(self, ctx:LabeledExprParser.ListExpressionContext):
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


    # Enter a parse tree produced by LabeledExprParser#ArrayExpr.
    def enterArrayExpr(self, ctx:LabeledExprParser.ArrayExprContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#ArrayExpr.
    def exitArrayExpr(self, ctx:LabeledExprParser.ArrayExprContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#IndexExpr.
    def enterIndexExpr(self, ctx:LabeledExprParser.IndexExprContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#IndexExpr.
    def exitIndexExpr(self, ctx:LabeledExprParser.IndexExprContext):
        pass



del LabeledExprParser
# Generated from LabeledExpr.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LabeledExprParser import LabeledExprParser
else:
    from LabeledExprParser import LabeledExprParser

# This class defines a complete generic visitor for a parse tree produced by LabeledExprParser.

class LabeledExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LabeledExprParser#root.
    def visitRoot(self, ctx:LabeledExprParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#block.
    def visitBlock(self, ctx:LabeledExprParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#statement.
    def visitStatement(self, ctx:LabeledExprParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#AssignExpr.
    def visitAssignExpr(self, ctx:LabeledExprParser.AssignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#identifierFunctionCall.
    def visitIdentifierFunctionCall(self, ctx:LabeledExprParser.IdentifierFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#IfStatementExpr.
    def visitIfStatementExpr(self, ctx:LabeledExprParser.IfStatementExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#IfExpr.
    def visitIfExpr(self, ctx:LabeledExprParser.IfExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#ElseIfExpr.
    def visitElseIfExpr(self, ctx:LabeledExprParser.ElseIfExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#ElseExpr.
    def visitElseExpr(self, ctx:LabeledExprParser.ElseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#ForExpr.
    def visitForExpr(self, ctx:LabeledExprParser.ForExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#FuncdelcExpr.
    def visitFuncdelcExpr(self, ctx:LabeledExprParser.FuncdelcExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#IdListExpr.
    def visitIdListExpr(self, ctx:LabeledExprParser.IdListExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#ExprlistExpr.
    def visitExprlistExpr(self, ctx:LabeledExprParser.ExprlistExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#FunctionCallExpr.
    def visitFunctionCallExpr(self, ctx:LabeledExprParser.FunctionCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#IdExpr.
    def visitIdExpr(self, ctx:LabeledExprParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#NumberExpr.
    def visitNumberExpr(self, ctx:LabeledExprParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#listExpression.
    def visitListExpression(self, ctx:LabeledExprParser.ListExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#ParenExpr.
    def visitParenExpr(self, ctx:LabeledExprParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#InfixExpr.
    def visitInfixExpr(self, ctx:LabeledExprParser.InfixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#ArrayExpr.
    def visitArrayExpr(self, ctx:LabeledExprParser.ArrayExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#IndexExpr.
    def visitIndexExpr(self, ctx:LabeledExprParser.IndexExprContext):
        return self.visitChildren(ctx)



del LabeledExprParser
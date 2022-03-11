# Generated from LabeledExpr.g4 by ANTLR 4.7.2
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


    # Visit a parse tree produced by LabeledExprParser#FuncdelcExpr.
    def visitFuncdelcExpr(self, ctx:LabeledExprParser.FuncdelcExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#identifierFunctionCall.
    def visitIdentifierFunctionCall(self, ctx:LabeledExprParser.IdentifierFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#AssignExpr.
    def visitAssignExpr(self, ctx:LabeledExprParser.AssignExprContext):
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


    # Visit a parse tree produced by LabeledExprParser#ParenExpr.
    def visitParenExpr(self, ctx:LabeledExprParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#InfixExpr.
    def visitInfixExpr(self, ctx:LabeledExprParser.InfixExprContext):
        return self.visitChildren(ctx)



del LabeledExprParser
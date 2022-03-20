from antlr4 import *
import sys
from dist.LabeledExprLexer import LabeledExprLexer
from dist.LabeledExprParser import LabeledExprParser
from dist.LabeledExprVisitor import LabeledExprVisitor
import copy
def get_username():
    from pwd import getpwuid
    from os import getuid
    return getpwuid(getuid())[ 0 ]

class Scope:
    def __init__(self):
        self.prev = None
        self.post = None
        self.param = {}
        self.tag = 0


class MyVisitor(LabeledExprVisitor):

    scope = Scope()
    output_var_name = None
    func_dic = {}
    func_param_table = []
    def visitIdExpr(self, ctx):
        key = ctx.getText()
        # if key in self.dic["main"]:
        #     value = self.dic["main"][key]
        #     return value
        if key in self.scope.param:
            value = self.scope.param[key]
            return value
        elif len(self.func_param_table)>0:
            self.scope.tag = 1
            value = self.func_param_table.pop()
            block_scope = self.scope
            while block_scope:
                if key in block_scope.param:
                    block_scope.param[key] = value
                    break
                else:
                    if block_scope.prev:
                        block_scope = block_scope.prev
                    else:
                        break
            self.scope = block_scope
            while self.scope:
                if self.scope.post.tag == 1:
                    self.scope = self.scope.post
                    break
                else:
                    self.scope = self.scope.post
            return value
        
        return 0

    def visitFuncdelcExpr(self, ctx):
        func_name = ctx.ID().getText()
        self.func_dic[func_name] = ctx 
        
        
        return 0
    def visitIdentifierFunctionCall(self,ctx):
        func_id = str(ctx.ID().getText())
        print(ctx.getText())
        func_ctx = self.func_dic[func_id]
        self.scope.post = Scope()
        self.scope.post.prev = self.scope
        self.scope = self.scope.post
        # self.block_index += 1
        if ctx.exprList():
            for x in ctx.exprList().expr():
                value = self.visit(x)
                self.func_param_table.append(value)
        
        value = self.visit(func_ctx.block())
        
        
        self.scope.param = {}
        if self.scope.prev != None:
            self.scope = self.scope.prev
        
        # self.func_dic.pop(func_id)
        return value
    def visitFunctionCallExpr(self, ctx):
        value = self.visit(ctx.functionCall())
        print(ctx.getText())
        if ctx.indexes():
            ind = self.visit(ctx.indexes().expr()[0])
            return value[ind]
        return value
    def visitBlock(self,ctx):
        for state in ctx.statement():
            self.visit(state)
        if ctx.expr():
            value = self.visit(ctx.expr())
            return value
        return 0
    def visitAssignExpr(self, ctx):
        
        l = ctx.ID().getText()
        r = self.visit(ctx.expr())
        if ctx.indexes():
            ind = self.visit(ctx.indexes().expr()[0])
            
            self.scope.param[l][ind] = r
        else:
            self.scope.param[l] = r
        self.output_var_name = l
        return r
    def visitNumberExpr(self, ctx):
        value = int(ctx.getText())
        return value

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitInfixExpr(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        op = ctx.op.text
        operation =  {
        '+': lambda: l + r,
        '-': lambda: l - r,
        '*': lambda: l * r,
        '/': lambda: l / r,
        '^': lambda: l ^ r,
        '==': lambda: l == r,
        '!=': lambda: l != r,
        '>': lambda: l > r,
        '<': lambda: l < r,
        '>=': lambda: l >= r,
        '<=': lambda: l <= r,
        '&&': lambda: l and r,
        '||': lambda: l or r,
        }
        return operation.get(op, lambda: None)()
    
    def visitIfStatementExpr(self, ctx):
        if bool(self.visit(ctx.ifStat().expr())):
            self.visit(ctx.ifStat().block())
        for x in ctx.elseIfStat():
            if bool(self.visit(x.expr())):
                self.visit(x.block())
        if ctx.elseStat():
            self.visit(ctx.elseStat().block())
        return 0
    def visitForExpr(self,ctx):
        self.visit(ctx.assignment()[0])
        while(bool(self.visit(ctx.expr()))):
            self.visit(ctx.block())
            self.visit(ctx.assignment()[1])
        return 0
    def visitlistExpression(self,ctx):
        value = self.visit(ctx.array())
        if ctx.indexes():
            ind = self.visit(self.indexes().expr()[0])
            return value[ind]
        return value
    
    def visitArrayExpr(self, ctx):
        
        value = self.visit(ctx.exprList())
        return value
    
    def visitIdListExpr(self,ctx):
        id_table = []
        for x in ctx.ID():
            value = x.getText()
            id_table.append(value)
        return id_table

    def visitExprlistExpr(self,ctx):
        val_table = []
        for x in ctx.expr():
            value = self.visit(x)
            val_table.append(value)
        return val_table

    def visitIndexExpr(self, ctx):
        return ctx.expr()


    def visitByeExpr(self, ctx):
        print(f"goodbye {get_username()}")
        sys.exit(0)

    def visitHelloExpr(self, ctx):
        return (f"{ctx.getText()} {get_username()}")


if __name__ == "__main__":
    file = open("test.gl","r")

    data =  InputStream(file.read())
    # lexer
    lexer = LabeledExprLexer(data)
    
    stream = CommonTokenStream(lexer)
    # parser
    parser = LabeledExprParser(stream)
    tree = parser.root()
    # print(tree)
    
    
    # evaluator
    visitor = MyVisitor()
    output = visitor.visit(tree)

    print(visitor.scope.param[visitor.output_var_name])
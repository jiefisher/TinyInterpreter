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
        func_name = ctx.ID()[0].getText()
        self.func_dic[func_name] = ctx 
        
        
        return 0
    def visitIdentifierFunctionCall(self,ctx):
        func_id = str(ctx.ID().getText())
        func_ctx = self.func_dic[func_id]
        self.scope.post = Scope()
        self.scope.post.prev = self.scope
        self.scope = self.scope.post
        # self.block_index += 1
        value = self.visit(ctx.expr())
        self.func_param_table.append(value)
        
        value = self.visit(func_ctx.block())
        
        self.scope.param = {}
        if self.scope.prev != None:
            self.scope = self.scope.prev
        # self.func_dic.pop(func_id)
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
        self.scope.param[l] = int(r)
        self.output_var_name = l
        return int(r)
    def visitNumberExpr(self, ctx):
        value = ctx.getText()
        return int(value)

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
        print(self.visit(ctx.assignment()[1]))
        self.visit(ctx.assignment()[0])
        while(bool(self.visit(ctx.expr()))):
            self.visit(ctx.block())
            self.visit(ctx.assignment()[1])
        return 0

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
from antlr4 import *
import sys
from utils.LabeledExprLexer import LabeledExprLexer
from utils.LabeledExprParser import LabeledExprParser
from utils.LabeledExprVisitor import LabeledExprVisitor
import copy
def get_username():
    from pwd import getpwuid
    from os import getuid
    return getpwuid(getuid())[ 0 ]

  
class MyVisitor(LabeledExprVisitor):
    block_name ="main"
    output_var_name = None
    dic = {}
    dic[block_name]={}
    func_dic = {}
    func_param_table = []
    def visitIdExpr(self, ctx):
        key = ctx.getText()
        # if key in self.dic["main"]:
        #     value = self.dic["main"][key]
        #     return value
        if key in self.dic.get(self.block_name,{}):
            value = self.dic[self.block_name][key]
            return value
        elif len(self.func_param_table)>0:
            value = self.func_param_table.pop()
            self.dic[self.block_name][key] = value
            return value
        
        return 0
    def visitFuncdelcExpr(self, ctx):
        func_name = ctx.ID()[0].getText()
        self.func_dic[func_name] = ctx 
        
        
        return 0
    def visitIdentifierFunctionCall(self,ctx):
        func_id = str(ctx.ID().getText())
        func_ctx = self.func_dic[func_id]
        his_block_name = copy.deepcopy(self.block_name)
        self.block_name = copy.deepcopy(func_id)
        value = self.visit(ctx.expr())
        self.func_param_table.append(value)
        
        self.dic[self.block_name]={}
        value = self.visit(func_ctx.block())
        self.dic[self.block_name] = {}
        self.block_name = copy.deepcopy(his_block_name)
        # self.func_dic.pop(func_id)
        return value
    def visitBlock(self,ctx):
        for state in ctx.statement():
            self.visit(state)
        value = self.visit(ctx.expr())
        return value
    def visitAssignExpr(self, ctx):
        
        l = ctx.ID().getText()
        r = self.visit(ctx.expr())
        self.dic[self.block_name][l] = int(r)
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
        }
        return operation.get(op, lambda: None)()

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

    print(visitor.dic['main'][visitor.output_var_name])
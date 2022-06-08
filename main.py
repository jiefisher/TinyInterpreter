from antlr4 import *
import sys
from dist.LabeledExprLexer import LabeledExprLexer
from dist.LabeledExprParser import LabeledExprParser
from dist.LabeledExprVisitor import LabeledExprVisitor


from collections import namedtuple
from ctypes import CFUNCTYPE, c_double
from enum import Enum

import llvmlite.ir as ir
import llvmlite.binding as llvm

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
    module = ir.Module()
    # bb_entry = func.append_basic_block('entry')
    double = ir.DoubleType()
    fnty = ir.FunctionType(ir.DoubleType(), ())

    # Create an empty module...
    
    
    scope = Scope()
    scope.module = ir.Module(name=__file__)
    # and declare a function named "fpadd" inside it
    scope.func = ir.Function(module, fnty, name="main")

    # Now implement the function
    scope.block = scope.func.append_basic_block(name="entry")
    scope.builder = ir.IRBuilder(scope.block)
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
            print(value,"param")
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
        
        return (0,ir.Constant(ir.DoubleType(), 0))

    def visitFuncdelcExpr(self, ctx):
        func_name = ctx.ID().getText()
        self.func_dic[func_name] = ctx 
        
        self.scope.post = Scope()
        self.scope.post.prev = self.scope
        self.scope = self.scope.post
        
        param_li = []
        if ctx.idList():
            for x in ctx.idList().ID():
                param_li.append(ir.DoubleType())
        self.scope.fnty = ir.FunctionType(ir.DoubleType(), param_li)
        self.scope.func = ir.Function(self.module, self.scope.fnty, name=func_name)
        for i in range(len(param_li)):
            self.func_param_table.append((0,self.scope.func.args[i]))
        # Now implement the function
        self.scope.block = self.scope.func.append_basic_block(name="entry")
        self.scope.builder = ir.IRBuilder(self.scope.block)
        # self.block_index += 1
        
        
        
        
        self.visit(ctx.block())
        
        
        self.scope.param = {}
        if self.scope.prev != None:
            self.scope = self.scope.prev
            
        
        
        return 0
    
    def visitIdentifierFunctionCall(self,ctx):
        func_id = str(ctx.ID().getText())
        print(ctx.getText())
        func_ctx = self.func_dic[func_id]
        func_params = []
        if ctx.exprList():
            for x in ctx.exprList().expr():
                value = self.visit(x)
                print(value,x.getText())
                self.func_param_table.append(value)
                func_params.append(value)
        
        
        
        # return self.builder.call(callee_func, call_args, 'calltmp')
        
        
        print(self.func_param_table)
        
        self.scope.param = {}
        if self.scope.prev != None:
            self.scope = self.scope.prev
        
        callee_func = self.module.get_global(func_id)
        call_args = [x[1] for x in func_params]
        # self.func_dic.pop(func_id)
        return (0,self.scope.builder.call(callee_func, call_args, 'calltmp'))
    
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
            print(value)
            self.scope.builder.ret(value[1])
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
        
        rhs_val = self.scope.builder.alloca(ir.DoubleType())
        self.scope.builder.store(r[1], rhs_val)
        return (int(r[0]),rhs_val)
    
    def visitNumberExpr(self, ctx):
        value = int(ctx.getText())
        val = ir.Constant(ir.DoubleType(), float(value))
        return (value,val)

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitInfixExpr(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)

        op = ctx.op.text
        operation =  {
        '+': lambda: (l[0] + r[0],self.scope.builder.fadd(l[1], r[1], 'addtmp')),
        '-': lambda: (l[0] - r[0],self.scope.builder.fsub(l[1], r[1], 'subtmp')),
        '*': lambda: (l[0] * r[0],self.scope.builder.fmul(l[1], r[1], 'multmp')),
        '/': lambda: (l[0] / r[0],self.scope.builder.fdiv(l[1], r[1], 'divtmp')),
        '^': lambda: (l[0] ^ r[0],self.scope.builder.xor(l[1], r[1], 'xortmp')),
        '==': lambda: (l[0] == r[0],self.scope.builder.icmp_signed('==',l[1], r[1], 'equaltmp')),
        '!=': lambda: (l[0] != r[0],self.scope.builder.icmp_signed('!=',l[1], r[1], 'notequaltmp')),
        '>': lambda: (l[0] > r[0],self.scope.builder.icmp_signed('>',l[1], r[1], 'bigtmp')),
        '<': lambda: (l[0] < r[0],self.scope.builder.icmp_signed('<',l[1], r[1], 'smalltmp')),
        '>=': lambda: (l[0] >= r[0],self.buildericmp_signed('>=',l[1], r[1], 'bigequqaltmp')),
        '<=': lambda: (l[0] <= r[0],self.scope.builder.icmp_signed('<=',l[1], r[1], 'smallequaltmp')),
        '&&': lambda: (l[0] and r[0],self.scope.builder.and_(l[1], r[1], 'andtmp')),
        '||': lambda: (l[0] or r[0],self.scope.builder.or_(l[1], r[1], 'ortmp')),
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
    file = open("newtest.gl","r")

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
    print(visitor.module)
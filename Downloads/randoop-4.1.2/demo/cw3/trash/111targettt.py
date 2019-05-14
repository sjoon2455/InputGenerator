# -*- coding: utf-8 -*-
#target.py
import astor
import ast
from tree_walk import *     #class TreeWalk
#from trace.py import Trace  #class Trace

def func(a, b):
    if a >= 3:
        a += 3
        func(4, 2)
        if a <= 7:
            b -= 3
            func(4, 2)
            if b != 0:
                func(4, 2)                                                           
    return False


#_ast = astor.code_to_ast(func)
#_ast.body[0].body.comparators[0].n = 100000
#exec(astor.to_source(_ast))
#print(func(4, 2)) #needs to be false, originally true


_ast = astor.code_to_ast(func)

class PrintBeforeCall(TreeWalk):
    def pre_body_name(self):
        body = self.cur_node #current node
        print(body)
        print_func = ast.Name("print", ast.Load())
        for i, child in enumerate(body[:]):
            #print(i, child)
            self.__name = None
            self.walk(child)
            #print(self.__name)
            if self.__name is not None:
                
                message = ast.Str("Calling {}".format(self.__name))
                print_statement = ast.Expr(ast.Call(print_func, [message], []))
                print(self.__name)
                body.insert(i, print_statement)
                print("a")
        self.__name = None
        return True

    def pre_Call(self):
        self.__name = self.cur_node.func.id
        return True
#펑션 콜이 있으면 그 노드는 __네임을 갖는다. 그리고 그 펑션 콜 직전에다가 인써트 해주는 방식임.
#이프문이 있으면 

'''
class ChangeIf(TreeWalk):
    def pre_IfExp(self):
        self.__left = self.cur_node.test #Compare
        return True
    
    def pre_Compare_name(self):
        #a = []
        body = self.cur_node
        #body = [body]
        #print(body)
        #a.append(body)
        #print(a)
        
        for i, child in enumerate(body[:]):
            self.__left = None
            self.walk(child)
            if self.__left is not None: #얘가 compare가 맞으면
                body.insert(i, ast.Expr(ast.Call(ast.Name("print", ast.Load()), [ast.Str("Calling If")], [])))
                
        child = body
        print(child)
        self.__left = None
        self.walk(child) # compare 가 나오겠지
        print(self.__left)
        if self.__left is not None:
            print("aaa")
            #body.insert(1, ast.Str("aaa"))
        #self.cur_node = ast.Str("aaa")
        return True
        
        #self.__name = None
        #self.walk(body)
        #print(self.cur_node)
        #if self.__name is not None:
        #print(self.__name)
        print(body)
        body.insert(ast.str("a"))
        #self.cur_node = ast.Str("aaa")
        print(body)
        #self.__name = None
        return True
    '''

walker1 = PrintBeforeCall()   # create an instance of the TreeWalk subclass

#walker = ChangeIf()
walker1.walk(_ast)   # modify the tree in place


#trace = trace()

print(astor.to_source(_ast))

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

'''
def func(a, b):
    a += 3
        #func(4, 2)
    if a <= 7:
        b -= 3
        func(4, 2)
        if b != 0:
            return True                                                           
    return False
'''


_ast = astor.code_to_ast(func)

class PrintBeforeCall(TreeWalk):
    def pre_body_name(self): #body 밑에 
        body = self.cur_node #current node, 바디 안에 있는 것들
        print(body)
        '''
        print_func = ast.Name("print", ast.Load())
        for i, child in enumerate(body[:]):
            self.__name = None
            self.walk(child)
            if self.__name is not None:
                message = ast.Str("Calling {}".format(self.__name))
                print_statement = ast.Expr(ast.Call(print_func, [message], []))
                #print(self.__name)
                body.insert(i, print_statement)
        self.__name = None'''
        return True

    def pre_Call(self):
        self.__name = self.cur_node.func.id
        return True


#바디의 차일드가 콜
#테스트의 차일드가 컴페어
class ChangeIf(TreeWalk):
    def pre_body_name(self):
        body = self.cur_node
        #print(body)
        for i, child in enumerate(body[:]): # child는 If, Return
            #print(i, child)
            self.__name__ = None
            
            self.walk(child)
            print(self.cur_node)
            for a in self.cur_node:
                print(a)
                if hasattr(self, __name__):
                    print("a")
        '''
            print(self.__name__)
            if self.__name__ is not None:
                #body.insert(i, ast.Str("a"))
                print("a")
        '''
        #self.__name__ = None
        return True
    
    
    def pre_If(self):
        self.__name__ = None #if 아래에 compare 있다
        #print(self.__name__)
        #return True




    '''
    def pre_left_name(self):
        body = self.cur_node
        self.__left = None
        child = body
        self.walk(child) # compare 가 나오겠지
        print(self.__left)
        if self.__left is not None:
            print("aaa")
            #body.insert(1, ast.Str("aaa"))
        return True
       ''' 

walker1 = PrintBeforeCall()       
walker = ChangeIf()
walker.walk(_ast)   # modify the tree in place

print(astor.to_source(_ast))

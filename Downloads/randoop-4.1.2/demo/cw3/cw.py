import astor
import ast
from tree_walk import * 

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



_ast = astor.code_to_ast(func)
'''
for node in ast.walk(_ast):
    #print(node)
    if isinstance(node, ast.If):
        print(node.test.left.id)
        #node.test.left
'''

class ChangeIf(TreeWalk):
    def pre_body_name(self):
        body = self.cur_node #current node
        #print(body)
        #print_func = ast.Name("print", ast.Load())
        for i, child in enumerate(body[:]):
            #print(i, child)
            #self.__name = None
            self.walk(child)
            #print(ast.dump(child))
            #print(self.__name)
            if isinstance(child, ast.If):
            #if self.__name is not None:
                #self.walk(child)
                #message = ast.Str("Calling {}".format(self.__name))
                #print_statement = ast.Expr(ast.Call(print_func, [message], []))
                #print(self.__name)
                print(i, body)
                #body.insert(i, ast.Str("aaaaa"))
                lhs = body[i].test.left.id
                op = body[i].test.ops[0]
                rhs = body[i].test.comparators
                print(rhs)
                #print(op[0])
                #print(body[i].test.left)
                #print("bbbbbb")
                
        #self.__name = None
        return True

    def pre_Call(self):
        self.__name = self.cur_node.func.id
        return True
    
'''
    def pre_If(self):
        self.__name = self.cur_node.test.left.id
        return True
'''

walker = ChangeIf()
walker.walk(_ast)   # modify the tree in place

print(astor.to_source(_ast))
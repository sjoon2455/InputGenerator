import sys
import astor
import ast
from target import func
from tree_walk import * 
from trace import Trace
from CountDepth import CountDepth
from traceHelper import Helper

helper = Helper()

#sys.argv[1]

count = CountDepth()
trace = Trace()
_ast = astor.code_to_ast(func)


class ChangeIf(TreeWalk):
    def pre_body_name(self):
        body = self.cur_node
        for i, child in enumerate(body[:]):
            self.walk(child)
            if isinstance(child, ast.If):
                count.incr()
                lhs = body[i].test.left.id
                op = body[i].test.ops[0]
                rhs = body[i].test.comparators[0]
                depth = count.getCount()
                
                #id에 depth 넣는 작업 
                traceFunction = trace.whichTracetoUse(op, lhs, rhs)
            
                args1 = ast.Num()
                args1.n = depth
                args2 = ast.Str(lhs)
                args3 = rhs
                body[i].test = ast.Expr(ast.Call(ast.Name("traceFunction"), [args1, args2, args3], []))

        return True

    def pre_Call(self):
        self.__name = self.cur_node.func.id
        return True

walker = ChangeIf()
walker.walk(_ast)   # modify the tree in place
#print(astor.dump(_ast))
print(astor.to_source(_ast))
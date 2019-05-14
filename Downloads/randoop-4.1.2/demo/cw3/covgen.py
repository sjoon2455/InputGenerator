import astor
import ast
from target import func
from tree_walk import * 
from trace import Trace


trace = Trace()
_ast = astor.code_to_ast(func)


class ChangeIf(TreeWalk):
    def pre_body_name(self):
        body = self.cur_node
        for i, child in enumerate(body[:]):
            self.walk(child)
            if isinstance(child, ast.If):
                lhs = body[i].test.left.id
                op = body[i].test.ops[0]
                rhs = body[i].test.comparators[0]
                #print(trace.whichTracetoUse(op, lhs, rhs))
                #body[i].test.left.id = ast.Str("aaaaaaaa")
                body[i].test = ast.Compare()
        return True

    def pre_Call(self):
        self.__name = self.cur_node.func.id
        return True


walker = ChangeIf()
walker.walk(_ast)   # modify the tree in place

print(astor.to_source(_ast))
import sys
import astor
import ast
import random
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
#_ast = astor.code_to_ast(func(4, 2))


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
                traceFunction = trace.whichTracetoUse(op, lhs, rhs)
                args1 = ast.Num()
                args1.n = depth
                args2 = ast.Str(lhs)
                args3 = rhs
                body[i].test = ast.Call(ast.Name("traceFunction"), [args1, args2, args3], [])
        return True

    def pre_Call(self):
        self.__name = self.cur_node.func.id
        return True

walker = ChangeIf()
walker.walk(_ast)   # modify the tree in place
dd = _ast.args.args

len = len(dd)
#print(len)

min = -1000
max = 1000

map = {}
for i in range(len):
    map[ dd[i] ] = random.randint(min, max)

print(map)


#print(astor.dump_tree(dd))
#print(astor.to_source(_ast))

'''     
1. 변수 업데이트 하는 거 해야함. AugAssign 나오면!

2. 
1T:
1F:
이런 식으로!

3. AVM도 해야된다... ㅋㅋ
'''
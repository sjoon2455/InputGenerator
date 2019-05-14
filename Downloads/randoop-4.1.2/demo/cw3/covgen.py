# -*- coding: utf-8 -*-
#covgen.py
'''
tree walk 상속받고 pre_If 등으로 if 만 뽑아서 분석을 .body .orElse....
if 안에 condition을 trace.greaterThan(숫자, num1, num2)로 바꿔서 숫자를 구함
or else에 들어가면 f고 if에 들어가면 t고 이런 식으로 F, T 구함
숫자+T인지 숫자+F인지 판단 가능
app. v = number of branches - 숫자(현재)
branch distance = 이미 만들어 놓음
fitness = app. v + branch distance
+-1인풋에 대해서도 함.

Q. Parsing 왜 안 됨? 
Q. assignment 어케 업데이트 함?
Q. While loop 어케 처리 함?
'''

import sys
import astor
import ast
from tree_walk import *
from target import func


if __name__ == '__main__':
    _ast = astor.code_to_ast(func)
    
#print(func(1, 2))

class walker(TreeWalk):
    def __init__(self, node):
        self.node = node
    def pre_If(self):
        pass
        

#a = walker(root)
#print(a)
#for node in a.walk(root):
    #print(node)

#print(a.walk(root)) why print None?


'''
def branchDist(pred):
    operand1 = get from id tag
    operand2 = get from comparator tag
    K = 1
    if operator == "==":
        return abs(operand1 - operand2)
    elif operator == "!=":
        return -abs(operand1-operand2)
    elif operator == "<":
        return operand1 - operand2 + K
    elif operator == ">":
        return operand2 - operand1 + K
    elif operator == "<=":
        return operand1 - operand2 + K
    elif operator == ">=":
        return operand2 - operand1 + K
'''
#trace.py
import ast
from traceHelper import *

class Trace(Helper):
    

    def whichTracetoUse(self, op, a, b):
        if isinstance(op, ast.Eq):
            return equals(id, a, b)
        if isinstance(op, ast.NotEq):
            return notEquals(id, a, b)
        if isinstance(op, ast.LtE):
            return lessThanOrEquals(id, a, b)
        if isinstance(op, ast.Lt):
            return lessThan(id, a, b)
        if isinstance(op, ast.GtE):
            return greaterThanOrEquals(id, a, b)
        if isinstance(op, ast.Gt):
            return greaterThan(id, a, b)
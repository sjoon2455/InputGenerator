#trace.py
import ast
#from traceHelper import Helper

class Trace:
    #get id 가 있어야하긴 함
    
    def whichTracetoUse(self, op, a, b):
        if isinstance(op, ast.Eq):
            return "helper.equals({}, {}, {})".format(op, a, b)
        if isinstance(op, ast.NotEq):
            return "helper.notEquals({}, {}, {})".format(op, a, b)
        if isinstance(op, ast.LtE):
            return "helper.lessThanOrEquals({}, {}, {})".format(op, a, b)
        if isinstance(op, ast.Lt):
            return "helper.lessThan({}, {}, {})".format(op, a, b)
        if isinstance(op, ast.GtE):
            return "helper.greaterThanOrEquals({}, {}, {})".format(op, a, b)
        if isinstance(op, ast.Gt):
            return "helper.greaterThan({}, {}, {})".format(op, a, b)
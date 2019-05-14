#traceHelper.py

class Helper:
    def equals(self, id, a, b):
        return a==b
    def notEquals(self, id, a, b):
        return a!=b
    def lessThanOrEquals(self, id, a, b):
        return a <= b
    def lessThan(self, id, a, b):
        return a<b
    def greaterThanOrEquals(self, id, a, b):
        return b<=a
    def greaterThan(self, id, a, b):
        return b<a
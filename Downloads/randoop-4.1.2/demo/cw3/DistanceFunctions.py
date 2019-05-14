class DistanceFunctions :
    K = 1
    
    def equals(boo1, boo2):
        if boo1==boo2:
            return 0
        return K

    def equals(a, b):
        return abs(a-b)+K
    
    def notEquals(boo1, boo2):
        if boo1 != boo2:
            return 0
        return K

    def notEquals(a, b):
        if a==b:
            return K
        return 0

    def greaterThan(a, b):
        if a>b:
            return 0
        return (b-a) + K
    

    def greaterThanOrEquals(a, b):
        if a>= b:
            return 0
        return (b-a) + K

    def lessThan(a, b):
        if a<b:
            return 0
        return (a-b) +K

    def lessThanOrEquals(a, b):
        if a <= b:
            return 0
        return (a-b) + K
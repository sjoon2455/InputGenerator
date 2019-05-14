#Normalize.py

class normalize:
    alpha = 1.001
    beta = 1.0

    def omega(n):
        return 1-alpha**(-n)
    def omega2(n):
        return n/(n+beta)
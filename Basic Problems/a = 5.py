from math import sqrt
def Fib(n):
    res = (((1 + sqrt(5))**n) - ((1 - sqrt(5))**n)) / (2**n*sqrt(5))
    print(int(res),str(n))
Fib(12)
    
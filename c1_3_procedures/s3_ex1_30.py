import sys
sys.setrecursionlimit(10000000)

from util import logl
from util import newl
from util import even
from util import cube
from util import inc

def sum(term, a, next, b):
    def iter(a, result):
        logl("(" + str(a) + ", " + str(result) + ")")

        if a > b:
            return result
        else:
            return iter(next(a), term(a) + result)

    return iter(a, 0)

def simpson_integral(f, a, b, n):
    def h():
        return (b - a) / n

    def y(k):
        return f(a + k * h())

    def term(k):
        if k == 0 or k == n:
            factor = 1
        elif even(k):
            factor = 2
        else:
            factor = 4

        return factor * y(k)
        
    return (h() / 3) * sum(term, 0, inc, n)

print(simpson_integral(cube, 0, 1, 100))
newl()

print(simpson_integral(cube, 0, 1, 1000))
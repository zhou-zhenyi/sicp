import sys
sys.setrecursionlimit(10000000)

from util import logl
from util import newl
from util import cube
from util import inc
from util import identity

def sum_integers(a, b):
    # if a > b:
    #     return 0
    # else:
    #     return a + sum_integers(a + 1, b)
    return sum(identity, a, inc, b)

def sum_cubes(a, b):
    # if a > b:
    #     return 0
    # else:
    #     return cube(a) + sum_cubes(a + 1, b)
    return sum(cube, a, inc, b)

def pi_sum(a, b):
    # if a > b:
    #     return 0
    # else:
    #     return 1.0 / (a * (a + 2)) + pi_sum(a + 4, b)
    def pi_term(x):
        return 1.0 / (x * (x + 2))

    def pi_next(x):
        return x + 4

    return sum(pi_term, a, pi_next, b)

def sum(term, a, next, b):
    logl("(" + str(a) + ", " + str(b) + ")")

    if a > b:
        return 0
    else:
        return term(a) + sum(term, next(a), next, b)

print(sum_integers(3, 5))
newl()

print(sum_cubes(3, 5))
newl()

print(pi_sum(3, 5))
newl()

def integral(f, a, b, dx):
    def add_dx(x):
        return x + dx
    
    return sum(f, a + dx / 2.0, add_dx, b) * dx

print(integral(cube, 0, 1, 0.01))
newl()

print(integral(cube, 0, 1, 0.001))
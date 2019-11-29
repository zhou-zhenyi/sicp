from util import logl
from util import newl

def expt_mult(a, b):
    logl("(" + str(a) + ", " + str(b) + ")")

    if b == 0:
        return 0
    else:
        return a + expt_mult(a, b - 1)

print(expt_mult(3, 9))

newl()

def double(x):
    return x + x

def halve(x):
    return x / 2

def even(n):
    return n % 2 == 0

def fast_expt(a, b):
    logl("(" + str(a) + ", " + str(b) + ")")

    if b == 0:
        return 0
    elif even(b):
        return double(fast_expt(a, halve(b)))
    else:
        return a + fast_expt(a, b - 1)

print(fast_expt(3, 9))
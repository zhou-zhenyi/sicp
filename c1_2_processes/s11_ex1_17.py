from util import logl
from util import newl
from util import double
from util import halve
from util import even

def expt_mult(a, b):
    logl("(" + str(a) + ", " + str(b) + ")")

    if b == 0:
        return 0
    else:
        return a + expt_mult(a, b - 1)

print(expt_mult(3, 9))

newl()

def fast_expt(a, b):
    logl("(" + str(a) + ", " + str(b) + ")")

    if b == 0:
        return 0
    elif even(b):
        return double(fast_expt(a, halve(b)))
    else:
        return a + fast_expt(a, b - 1)

print(fast_expt(3, 9))
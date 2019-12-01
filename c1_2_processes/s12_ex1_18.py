from util import logl
from util import double
from util import halve
from util import even

def mult(a, b):
    def mult_iter(r, a, b):  
        logl("(" + str(r) + ", " + str(a) + ", " + str(b) + ")")

        if b == 0:
            return r
        elif even(b):
            return mult_iter(r, double(a), halve(b))
        else:
            return mult_iter(r + a, a, b - 1)

    return mult_iter(0, a, b)

print(mult(3, 9))
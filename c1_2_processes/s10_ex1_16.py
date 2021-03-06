from util import logl
from util import square
from util import even

def expt(b, n):
    def expt_iter(a, b, n):
        logl("(" + str(a) + ", " + str(b) + ", " + str(n) + ")")

        if n == 0:
            return a
        elif even(n):
            return expt_iter(a, square(b), n / 2)
        else:
            return expt_iter(a * b, b, n - 1)

    return expt_iter(1, b, n)

print(expt(5, 3))
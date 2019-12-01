from util import logl
from util import square
from util import even

def fib(n):
    return fib_iter(1, 0, 0, 1, n)

def fib_iter(a, b, p, q, count):
    logl("(" + str(a) + ", " + str(b) + ", " + str(p) +
         ", " + str(q) + ", " + str(count) + ")")

    if count == 0:
        return b
    elif even(count):
        return fib_iter(a,
                        b,
                        square(p) + square(q),
                        2 * p * q + square(q),
                        count / 2)
    else:
        return fib_iter((b * q) + (a * q) + (a * p),
                        (b * p) + (a * q),
                        p,
                        q,
                        (count - 1))

print(fib(10))
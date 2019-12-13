from util import logl
from util import newl
from util import even
from util import inc
from util import identity

def prod_recu(term, a, next, b):
    logl("(" + str(a) + ", " + str(b) + ")")

    if a > b:
        return 1
    else:
        return term(a) * prod_recu(term, next(a), next, b)

def prod_iter(term, a, next, b):
    def iter(a, result):
        logl("(" + str(a) + ", " + str(result) + ")")

        if a > b:
            return result
        else:
            return iter(next(a), term(a) * result)

    return iter(a, 1)

def factorial_r(n):
    return prod_recu(identity, 1, inc, n)

def factorial_i(n):
    return prod_iter(identity, 1, inc, n)

print(factorial_r(6))
newl()

print(factorial_i(6))
newl()

def term(k):
    if even(k):
        a = k + 2
        b = a + 1
    else:
        a = k + 3
        b = a - 1

    return a / b

def pi_recu():
    return prod_recu(term, 0, inc, 99) * 4

def pi_iter():
    return prod_iter(term, 0, inc, 99) * 4

print(pi_recu())
newl()

print(pi_iter())
from util import logl
from util import newl

def f_recu(n):
    logl("(" + str(n) + ")")

    if n < 3:
        return n
    else:
        return f_recu(n - 1) + 2 * f_recu(n - 2) + 3 * f_recu(n - 3)

print(f_recu(7))

newl()

def f_iter(a, b, c, i, n):
    logl("(" + str(a) + ", " + str(b) + ", " + str(c) +
         ", " + str(i) + ", " + str(n) + ")")

    if n < 3:
        return n
    elif i > n:
        return c
    else:
        return f_iter(b, c, c + 2 * b + 3 * a, i + 1, n)

def f(n):
    return f_iter(0, 1, 2, 3, n)

print(f(7))
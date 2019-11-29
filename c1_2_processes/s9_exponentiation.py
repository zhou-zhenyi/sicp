from util import logl
from util import newl

def expt(b, n):
    # if n == 0:
    #     return 1
    # else:
    #     return b * expt(b, n - 1)
    return expt_iter(b, n, 1)

def expt_iter(b, counter, product):
    logl("(" + str(b) + ", " + str(counter) + ", " + str(product) + ")")

    if counter == 0:
        return product
    else:
        return expt_iter(b, counter - 1, b * product)

print(expt(2, 12))

newl()

def fast_expt(b, n):
    logl("(" + str(b) + ", " + str(n) + ")")

    if n == 0:
        return 1
    elif even(n):
        return square(fast_expt(b, n / 2))
    else:
        return b * fast_expt(b, n - 1)

def square(x):
    return x * x

def even(n):
    return n % 2 == 0

print(fast_expt(2, 12))
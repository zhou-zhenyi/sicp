from random import randint

from util import logl
from util import newl
from util import square
from util import even

def expmod(base, exp, m):
    logl("(" + str(base) + ", " + str(exp) + ", " + str(m) + ")")

    if exp == 0:
        return 1
    elif even(exp):
        return square(expmod(base, exp / 2, m)) % m
    else:
        return base * expmod(base, exp - 1, m) % m

def fermat_test(n):
    def try_it(a):
        return expmod(a, n, n) == a

    return try_it(randint(1, n - 1))

print(fermat_test(113))

newl()

def fast_prime(n, times):
    logl("(" + str(n) + ", " + str(times) + ")")
    
    if times == 0:
        return True
    elif fermat_test(n):
        return fast_prime(n, times - 1)
    else:
        return False

print(fast_prime(113, 3))
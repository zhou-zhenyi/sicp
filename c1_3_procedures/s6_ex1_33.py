from util import logl
from util import newl
from util import square
from util import prime
from util import gcd
from util import identity
from util import inc
from util import add
from util import mul

def filtered_accumulate(filter, combiner, null_value, term, a, next, b):
    logl("(" + str(a) + ", " + str(b) + ")")

    if a > b:
        return null_value
    elif filter(a):
        return combiner(term(a), filtered_accumulate(filter, combiner, null_value, term, next(a), next, b))
    else:
        return filtered_accumulate(filter, combiner, null_value, term, next(a), next, b)

def sum_prime(a, b):
    return filtered_accumulate(prime, add, 0, square, a, inc, b)

def fact_gcd(n):
    def is_gcd(i):
        if i < n and gcd(i, n) == 1:
            return True
        
        return False

    return filtered_accumulate(is_gcd, mul, 1, identity, 1, inc, n)

print(sum_prime(1, 10))
newl()

print(fact_gcd(10))
from math import log

from util import logl
from util import newl
from util import average

def fixed_point(f, first_guess):
    def close_enough(v1, v2):
        return abs(v1 - v2) < 0.00001

    def try_it(guess):
        logl("(" + str(guess) + ")")

        next = f(guess)

        if close_enough(guess, next):
            return next

        return try_it(next)

    return try_it(first_guess)

print(fixed_point(lambda x: log(1000) / log(x), 1.1))
newl()

print(fixed_point(lambda x: average(x, log(1000) / log(x)), 1.1))
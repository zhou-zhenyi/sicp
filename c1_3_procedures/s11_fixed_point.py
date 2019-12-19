from math import cos
from math import sin

from util import average

tolerance = 0.00001

def fixed_point(f, first_guess):
    def close_enough(v1, v2):
        return abs(v1 - v2) < tolerance

    def try_it(guess):
        next = f(guess)

        if close_enough(guess, next):
            return next

        return try_it(next)

    return try_it(first_guess)

print(fixed_point(cos, 1.0))
print(fixed_point(lambda y: sin(y) + cos(y), 1.0))

def sqrt(x):
    return fixed_point(lambda y: average(y, x / y), 1.0)

print(sqrt(9))
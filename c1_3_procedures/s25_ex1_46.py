from math import cos

from util import square
from util import average

def iterative_improve(test, improve):
    def iter(x):
        if test(x):
            return x

        return iter(improve(x))

    return lambda x: iter(x)

def sqrt(x):
    def improve(guess):
        return average(guess, (x / guess))

    def good_enough(guess):
        return abs(square(guess) - x) < 0.001

    return iterative_improve(good_enough, improve)(1.0)

def fixed_point(f, first_guess):
    def close_enough(guess):
        return abs(guess - f(guess)) < 0.00001

    return iterative_improve(close_enough, f)(first_guess)

print(sqrt(9))
print(fixed_point(cos, 1.0))
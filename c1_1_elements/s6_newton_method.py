from s3_compound import square
from s4_conditional import abs

def sqrt_iter(guess, x):
    if good_enough(guess, x):
        return guess
    else:
        return sqrt_iter(improve(guess, x), x)

def improve(guess, x):
    return average(guess, (x / guess))

def average(x, y):
    return (x + y) / 2

def good_enough(guess, x):
    return abs(square(guess) - x) < 0.001

def sqrt(x):
    return sqrt_iter(1.0, x)

print(sqrt(9))
print(sqrt(100 + 37))
print(sqrt(sqrt(2) + sqrt(3)))
print(square(sqrt(1000)))
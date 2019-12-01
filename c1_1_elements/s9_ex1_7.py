def sqrt_iter(guess, last_guess, x):
    if good_enough(guess, last_guess):
        return guess
    else:
        return sqrt_iter(improve(guess, x), guess, x)

def improve(guess, x):
    return average(guess, (x / guess))

def average(x, y):
    return (x + y) / 2

def good_enough(guess, last_guess):
    return abs(guess - last_guess) < 0.001

def square(x):
    return x * x

def abs(x):
    if x < 0:
        return 0 - x
    return x

def sqrt(x):
    return sqrt_iter(1.0, x, x)

print(sqrt(9))
print(sqrt(100 + 37))
print(sqrt(sqrt(2) + sqrt(3)))
print(square(sqrt(1000)))
print(sqrt(1000000000000000000000))
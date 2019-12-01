def cbrt_iter(guess, last_guess, x):
    if good_enough(guess, last_guess):
        return guess
    else:
        return cbrt_iter(improve(guess, x), guess, x)

def improve(guess, x):
    return ((x / square(guess)) + 2 * guess) / 3

def good_enough(guess, last_guess):
    return abs(guess - last_guess) < 0.001

def square(x):
    return x * x

def abs(x):
    if x < 0:
        return 0 - x
    return x

def cbrt(x):
    return cbrt_iter(1.0, x, x)

print(cbrt(9))
print(cbrt(216))
print(cbrt(10000000000000000000))
from util import logl
from util import newl
from util import square

def smallest_divisor(n):
    return find_divisor(n, 2)

def find_divisor(n, test_divisor):
    logl("(" + str(n) + ", " + str(test_divisor) + ")")

    if square(test_divisor) > n:
        return n
    elif divides(test_divisor, n):
        return test_divisor
    else:
        return find_divisor(n, test_divisor + 1)

def divides(a, b):
    return b % a == 0

x = smallest_divisor(112)
print(x)

newl()

def prime(n):
    return n == smallest_divisor(n)

print(prime(x))
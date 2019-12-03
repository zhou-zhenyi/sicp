import sys
sys.setrecursionlimit(10000000)

from random import randint

from util import square
from util import even

def miller_rabin_test(n):
    def expmod(base, exp, m):
        def sqrmod(x):
            def check_sqrt(x, square):
                if square == 1 and x != 1 and x != m - 1:
                    return 0

                return square

            return check_sqrt(x, square(x)) % m

        if exp == 0:
            return 1
        elif even(exp):
            return sqrmod(expmod(base, exp / 2, m))
        else:
            return base * expmod(base, exp - 1, m) % m
    
    def try_it(a):
        def check_it(x):
            return x != 0 and x == 1

        return check_it(expmod(a, n - 1, n))

    return try_it(randint(1, n - 1))

def fast_prime(n, times):
    if times == 0:
        return True
    elif miller_rabin_test(n):
        return fast_prime(n, times - 1)
    else:
        return False

def check_carmichael(n):
    return fast_prime(n, 100)

print(check_carmichael(112))
print(check_carmichael(113))
print(check_carmichael(561))
print(check_carmichael(1105))
print(check_carmichael(1729))
print(check_carmichael(2465))
print(check_carmichael(2821))
print(check_carmichael(6601))
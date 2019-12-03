import sys
sys.setrecursionlimit(10000000)

from time import time_ns
from random import randint

from util import square
from util import even

def timed_prime_test(n):
    return start_prime_test(n, time_ns())

def start_prime_test(n, start_time):
    is_prime = fast_prime(n, 1)

    if is_prime:
        report_prime(n, time_ns() - start_time)

    return is_prime

def report_prime(n, elapsed_time):
    print(str(n) + " *** " + str(elapsed_time))

def fast_prime(n, times):
    def fermat_test(n):
        def try_it(a):
            def expmod(base, exp, m):
                if exp == 0:
                    return 1
                elif even(exp):
                    return (expmod(base, exp / 2, m) * expmod(base, exp / 2, m)) % m
                else:
                    return base * expmod(base, exp - 1, m) % m

            return expmod(a, n, n) == a

        return try_it(randint(1, n - 1))
    
    if times == 0:
        return True
    elif fermat_test(n):
        return fast_prime(n, times - 1)
    else:
        return False

def search_for_prime(n, i):
    if i == 0:
        return
    elif even(n):
        n += 1
    else:
        n += 2

    if timed_prime_test(n):
        i -= 1

    search_for_prime(n, i)

search_for_prime(1000, 3)
search_for_prime(10000, 3)
search_for_prime(100000, 3)
search_for_prime(1000000, 3)
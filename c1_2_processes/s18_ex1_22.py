import sys
sys.setrecursionlimit(10000000)

from time import time_ns

from util import square
from util import even
from util import prime

def timed_prime_test(n):
    return start_prime_test(n, time_ns())

def start_prime_test(n, start_time):
    is_prime = prime(n)

    if is_prime:
        report_prime(n, time_ns() - start_time)

    return is_prime

def report_prime(n, elapsed_time):
    print(str(n) + " *** " + str(elapsed_time))

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
from time import time

from util import square

def timed_prime_test(n):
    print("\n")
    print(n)
    start_prime_test(n, time())

def start_prime_test(n, start_time):
    if prime(n):
        return report_prime(time() - start_time)

def report_prime(elapsed_time):
    print(" *** ")
    print(elapsed_time)

def prime(n):
    def smallest_divisor(n):
        def find_divisor(n, test_divisor):
            def divides(a, b):
                return b % a == 0

            if square(test_divisor) > n:
                return n
            elif divides(test_divisor, n):
                return test_divisor
            else:
                return find_divisor(n, test_divisor + 1)

        return find_divisor(n, 2)

    return n == smallest_divisor(n)

timed_prime_test(113)
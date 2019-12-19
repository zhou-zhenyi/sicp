num = 0

def line():
    global num
    num += 1
    return num

def newl():
    global num
    num = 0

def logl(msg):
    print(str(line()) + ": " + msg)

def square(x):
    return x * x

def double(x):
    return x + x

def halve(x):
    return x / 2

def even(n):
    return n % 2 == 0

def average(x, y):
    return (x + y) / 2

def cube(x):
    return x * x * x

def inc(n):
    return n + 1

def identity(x):
    return x

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

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

    if n == 1:
        return False
    else:
        return n == smallest_divisor(n)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def sum(term, a, next, b):
    if a > b:
        return 0
    else:
        return term(a) + sum(term, next(a), next, b)

def fixed_point(f, first_guess):
    def close_enough(v1, v2):
        return abs(v1 - v2) < 0.00001

    def try_it(guess):
        next = f(guess)

        if close_enough(guess, next):
            return next

        return try_it(next)

    return try_it(first_guess)
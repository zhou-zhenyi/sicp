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

def cont_frac(n, d, k):
    def iter(i, x):
        if i == 0:
            return x
        
        return iter(i - 1, n(i) / (d(i) + x))

    return iter(k, 0)

def average_damp(f):
    return lambda x: average(x, f(x))

def newtons_method(g, guess):
    def newton_transform(g):
        def deriv(g):
            return lambda x: (g(x + 0.00001) - g(x)) / 0.00001

        return lambda x: x - (g(x) / deriv(g)(x))

    return fixed_point(newton_transform(g), guess)

def repeated(f, n):
    def compose(f, g):
        return lambda x: f(g(x))

    if n == 1:
        return lambda x: f(x)
    else:
        return repeated(compose(f, f), n - 1)
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
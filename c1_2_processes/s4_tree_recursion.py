def fib(n):
    # if n == 0:
    #     return 0
    # elif n == 1:
    #     return 1
    # else:
    #     return fib(n - 1) + fib(n - 2)
    return fib_iter(1, 0, n)

def fib_iter(a, b, count):
    if count == 0:
        return b
    else:
        return fib_iter(a + b, a, count - 1)

print(fib(5))
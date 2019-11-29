from util import logl

def factorial(n):
    logl("(" + str(n) + ")")

    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(6))
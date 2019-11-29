from util import logl

def multiply(a, b):
    logl("(" + str(a) + ", " + str(b) + ")")

    if b == 0:
        return 0
    else:
        return a + multiply(a, b - 1)

print(multiply(3, 5))
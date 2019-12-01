from util import logl

def cube(x):
    return x * x * x

def p(x):
    return 3 * x - 4 * cube(x)

def sine(angle):
    logl("(" + str(angle) + ")")

    if not(abs(angle) > 0.1):
        return angle
    else:
        return p(sine(angle / 3.0))

print(sine(12.15))
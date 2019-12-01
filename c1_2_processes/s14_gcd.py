from util import logl

def gcd(a, b):
    logl("(" + str(a) + ", " + str(b) + ")")

    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(206, 40))
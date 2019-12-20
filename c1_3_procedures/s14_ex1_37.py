from util import logl
from util import newl

def cont_frac_i(n, d, k):
    def iter(i, x):
        logl("(" + str(i) + ", " + str(x) + ")")

        if i == 0:
            return x
        
        return iter(i - 1, n(i) / (d(i) + x))

    return iter(k, 0)

def cont_frac_r(n, d, k):
    def recu(i):
        logl("(" + str(i) + ")")

        if i > k:
            return 0
        
        return n(i) / (d(i) + recu(i + 1))

    return recu(1)

print(cont_frac_i(lambda i: 1.0, lambda i: 1.0, 11))
newl()

print(cont_frac_r(lambda i: 1.0, lambda i: 1.0, 11))
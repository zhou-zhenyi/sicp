from util import square
from util import cont_frac

def tan_cf(x, k):
    def n(i):
        if i == 1:
            return x
        else:
            return - square(x)

    def d(i):
        return 2 * i - 1

    return cont_frac(n, d, k)

print(tan_cf(60, 200))
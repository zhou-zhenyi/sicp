from util import cont_frac

def d(i):
    n = i + 1

    if n % 3 == 0:
        return 2 * (n / 3)
    else:
        return 1

def e():
    return 2 + cont_frac(lambda i: 1, d, 100)

print(e())
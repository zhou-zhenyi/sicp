from util_pair import cons, car, cdr
from util import gcd

def make_rat(n, d):
    # return cons(n, d)
    g = gcd(n, d)
    
    return cons(int(n / g), int(d / g))

def numer(x):
    return car(x)

def denom(x):
    return cdr(x)

def add_rat(x, y):
    return make_rat(numer(x) * denom(y) + numer(y) * denom(x), denom(x) * denom(y))

def sub_rat(x, y):
    return make_rat(numer(x) * denom(y) - numer(y) * denom(x), denom(x) * denom(y))

def mul_rat(x, y):
    return make_rat(numer(x) * numer(y), denom(x) * denom(y))

def div_rat(x, y):
    return make_rat(numer(x) * denom(y), denom(x) * numer(y))

def equal_rat(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)

def print_rat(x):
    print(str(numer(x)) + "/" + str(denom(x)))

one_half = make_rat(1, 2)
print_rat(one_half)

one_third = make_rat(1, 3)
print_rat(one_third)

print_rat(add_rat(one_half, one_third))
print_rat(mul_rat(one_half, one_third))
print_rat(add_rat(one_third, one_third))
from util_pair import cons, car, cdr
from util_interval import make_interval, print_interval
from util_interval import add_interval, mul_interval, div_interval

def lower_bound(z):
    return min([car(z), cdr(z)])

def upper_bound(z):
    return max([car(z), cdr(z)])

z1 = make_interval(2, 5)
z2 = make_interval(7, 3)

print_interval(z1)
print_interval(z2)

print_interval(add_interval(z1, z2))
print_interval(mul_interval(z1, z2))
print_interval(div_interval(z1, z2))
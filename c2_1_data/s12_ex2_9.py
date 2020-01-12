from util_interval import make_interval, lower_bound, upper_bound, print_interval
from util_interval import add_interval, sub_interval, mul_interval, div_interval

def interval_width(x):
    return (upper_bound(x) - lower_bound(x)) / 2

z1 = make_interval(2, 5)
z2 = make_interval(7, 3)
z3 = add_interval(z1, z2)
z4 = sub_interval(z1, z2)
z5 = mul_interval(z1, z2)
z6 = div_interval(z1, z2)

print_interval(z1)
print_interval(z2)

print(interval_width(z1) + interval_width(z2))

print(interval_width(z3))
print(interval_width(z4))
print(interval_width(z5))
print(interval_width(z6))
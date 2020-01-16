from util_interval import make_interval, lower_bound, upper_bound, print_interval
from util_interval import add_interval, sub_interval, mul_interval

def div_interval(x, y):
    if lower_bound(y) * upper_bound(y) <= 0:
        print("Division error: [" + str(lower_bound(y)) + ", " + str(upper_bound(y)) + "]")
        return make_interval(0, 0)
    else:
        return mul_interval(x, make_interval(1.0 / upper_bound(y), 1.0 / lower_bound(y)))

z1 = make_interval(2, 5)
z2 = make_interval(-1, 1)

print_interval(z1)
print_interval(z2)

print_interval(div_interval(z1, z2))
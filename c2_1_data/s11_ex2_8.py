from util_interval import make_interval, lower_bound, upper_bound, print_interval

def sub_interval(x, y):
    return make_interval(lower_bound(x) - upper_bound(y),
                         upper_bound(x) - lower_bound(y))

z1 = make_interval(2, 5)
z2 = make_interval(7, 3)

print_interval(z1)
print_interval(z2)

print_interval(sub_interval(z1, z2))
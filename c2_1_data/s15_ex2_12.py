from util_interval import make_interval, lower_bound, upper_bound, print_interval

def make_center_width(c, w):
    return make_interval(c - w, c + w)

def center(i):
    return (lower_bound(i) + upper_bound(i)) / 2

def width(i):
    return (upper_bound(i) - lower_bound(i)) / 2

z1 = make_center_width(3.5, 0.15)

print_interval(z1)
print(center(z1))
print(width(z1))

def make_center_percent(c, p):
    r = p / 100

    return make_interval(c * (1 + r), c * (1 - r))

def percent(i):
    return (upper_bound(i) - lower_bound(i)) / (upper_bound(i) + lower_bound(i)) * 100

z2 = make_center_percent(4, 25)

print_interval(z2)
print(center(z2))
print(percent(z2))
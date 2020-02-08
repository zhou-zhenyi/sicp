from util_pair import cons, car, cdr

def add_interval(x, y):
    return make_interval(lower_bound(x) + lower_bound(y),
                         upper_bound(x) + upper_bound(y))

def sub_interval(x, y):
    return make_interval(lower_bound(x) - upper_bound(y),
                         upper_bound(x) - lower_bound(y))

def mul_interval(x, y):
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)

    return make_interval(min([p1, p2, p3, p4]),
                         max([p1, p2, p3, p4]))

def div_interval(x, y):
    return mul_interval(x, make_interval(1.0 / upper_bound(y), 1.0 / lower_bound(y)))

def make_interval(a, b):
    return cons(a, b)

def lower_bound(z):
    return min([car(z), cdr(z)])

def upper_bound(z):
    return max([car(z), cdr(z)])

def print_interval(x):
    print("[" + str(lower_bound(x)) + ", " + str(upper_bound(x)) + "]")
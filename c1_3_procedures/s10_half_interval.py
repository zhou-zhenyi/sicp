from math import sin
from util import average

def search(f, neg_point, pos_point):
    midpoint = average(neg_point, pos_point)

    if close_enough(neg_point, pos_point):
        return midpoint
    
    test_value = f(midpoint)

    if test_value > 0:
        return search(f, neg_point, midpoint)
    elif test_value < 0:
        return search(f, midpoint, pos_point)
    else:
        return midpoint

def close_enough(x, y):
    return abs(x - y) < 0.001

def half_interval_method(f, a, b):
    a_value = f(a)
    b_value = f(b)

    if a_value < 0 and b_value > 0:
        return search(f, a, b)
    elif b_value < 0 and a_value > 0:
        return search(f, b, a)
    else:
        print("Values are not of opposite sign " + str(a) + " " + str(b))

print(half_interval_method(sin, 2.0, 4.0))
print(half_interval_method(lambda x: x * x * x - 2 * x - 3, 1.0, 2.0))
from util import average
from util import square
from util import fixed_point

def average_damp(f):
    return lambda x: average(x, f(x))

print(average_damp(square)(10))

def sqrt(x):
    return fixed_point(average_damp(lambda y: x / y), 1.0)

print(sqrt(9))

def cube_root(x):
    return fixed_point(average_damp(lambda y: x / square(y)), 1.0)

print(cube_root(9))
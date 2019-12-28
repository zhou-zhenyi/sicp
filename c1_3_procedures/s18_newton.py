from util import cube
from util import square
from util import fixed_point
from util import average_damp

def deriv(g):
    dx = 0.00001

    return lambda x: (g(x + dx) - g(x)) / dx

print(deriv(cube)(5))

def newton_transform(g):
    return lambda x: x - (g(x) / deriv(g)(x))

def newtons_method(g, guess):
    return fixed_point(newton_transform(g), guess)

def sqrt(x):
    return newtons_method(lambda y: square(y) - x, 1.0)

print(sqrt(9))

def fixed_point_of_transform(g, transform, guess):
    return fixed_point(transform(g), guess)

def sqrt2(x):
    return fixed_point_of_transform(lambda y: x / y, average_damp, 1.0)

print(sqrt2(9))

def sqrt3(x):
    return fixed_point_of_transform(lambda y: square(y) - x, newton_transform, 1.0)

print(sqrt3(9))
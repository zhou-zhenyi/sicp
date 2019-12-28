from util import square
from util import cube
from util import newtons_method

def cubic(a, b, c):
    return lambda x: cube(x) + a * square(x) + b * x + c

print(newtons_method(cubic(1, 2, 3), 1))
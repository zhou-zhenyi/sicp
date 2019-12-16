from util import square
from util import cube
from util import sum

def pi_sum(a, b):
    return sum(lambda x: 1.0 / (x * (x + 2)), a, lambda x: x + 4, b)

print(pi_sum(3, 5))

def integral(f, a, b, dx):
    return sum(f, a + dx / 2.0, lambda x: x + dx, b) * dx

print(integral(cube, 0, 1, 0.01))

f = lambda x, y, z: x + y + square(z)

print(f(1, 2, 3))
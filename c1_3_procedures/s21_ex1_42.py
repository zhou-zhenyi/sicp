from util import square
from util import inc

def compose(f, g):
    return lambda x: f(g(x))

print(compose(square, inc)(6))
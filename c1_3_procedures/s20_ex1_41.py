from util import inc

def double(f):
    return lambda x: f(f(x))

print(double(double(double))(inc)(5))
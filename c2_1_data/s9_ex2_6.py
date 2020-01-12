from util import inc

def zero():
    return lambda f: lambda x: x

def add_1(n):
    return lambda f: lambda x: f(n(f)(x))

print(zero()(inc)(0))
print(add_1(zero())(inc)(0))
print(add_1(add_1(zero()))(inc)(0))

def one():
    return lambda f: lambda x: f(x)

def two():
    return lambda f: lambda x: f(f(x))

print(one()(inc)(0))
print(two()(inc)(0))

def add(a, b):
    return lambda f: lambda x: a(f)(b(f)(x))

print(add(one(), two())(inc)(0))
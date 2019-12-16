from util import square

def f(x, y):
    # def f_helper(a, b):
    #     return x * square(a) + y * b + a * b

    # return f_helper(1 + (x * y), 1 - y)

    # l = lambda a, b: x * square(a) + y * b + a * b

    # return l(1 + x * y, 1 - y)
    a = 1 + (x * y)
    b = 1 - y

    return x * square(a) + y * b + a * b

print(f(3, 4))
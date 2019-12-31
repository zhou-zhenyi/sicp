from util import square

def repeated(f, n):
    def compose(f, g):
        return lambda x: f(g(x))

    if n == 1:
        return lambda x: f(x)
    else:
        return repeated(compose(f, f), n - 1)

print(repeated(square, 2)(5))
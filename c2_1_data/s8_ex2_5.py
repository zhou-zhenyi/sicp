def count(z, n, t):
    x = z / n

    if x - int(x) == 0:
        return count(x, n, t + 1)

    return t

def cons(a, b):
    return (2 ** a) * (3 ** b)

def car(z):
    return count(z, 2, 0)

def cdr(z):
    return count(z, 3, 0)

z = cons(11, 13)

print(z)
print(car(z))
print(cdr(z))
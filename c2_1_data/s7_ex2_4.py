def cons(x, y):
    return lambda m: m(x, y)

def car(z):
    return z(lambda p, q: p)

def cdr(z):
    return z(lambda p, q: q)

x = cons(1, 2)

print(car(x))
print(cdr(x))

y = cons(3, 4)
z = cons(x, y)

print(car(car(z)))
print(car(cdr(z)))
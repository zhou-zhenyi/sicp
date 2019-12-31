from util import cons, car, cdr

x = cons(1, 2)

print(car(x))
print(cdr(x))

y = cons(3, 4)
z = cons(x, y)

print(car(car(z)))
print(car(cdr(z)))
from util import logl
from util import newl

def A(x, y):
    logl("(" + str(x) + ", " + str(y) + ")")

    if y == 0:
        return 0
    elif x == 0:
        return 2 * y
    elif y == 1:
        return 2
    else:
        return A(x - 1, A(x, y - 1))

print(A(1, 10))
newl()
print(A(2, 4))
newl()
print(A(3, 3))
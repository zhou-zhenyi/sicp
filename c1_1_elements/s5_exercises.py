print(
    (5 + 4 + (2 - (3 - (6 + 4 / 5))))
    /
    (3 * (6 - 2) * (2 - 7))
)

def square(x):
    return x * x

def sum_of_square(a, b):
    return square(a) + square(b)

def sum_of_greater(a, b, c):
    if a >= c and b >= c:
        return sum_of_square(a, b)
    elif a >= b and c >= b:
        return sum_of_square(a, c)
    else:
        return sum_of_square(b, c)

print(sum_of_greater(1, 2, 3))
print(sum_of_greater(1, 1, 1))
print(sum_of_greater(1, 2, 2))
print(sum_of_greater(1, 1, 2))

def p():
    p()

def test(x, y):
    if x == 0:
        0
    else:
        p()

test(0, p())
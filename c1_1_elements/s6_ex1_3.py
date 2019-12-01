def sum_of_square(a, b):
    return square(a) + square(b)

def sum_of_greater(a, b, c):
    if a >= c and b >= c:
        return sum_of_square(a, b)
    elif a >= b and c >= b:
        return sum_of_square(a, c)
    else:
        return sum_of_square(b, c)

def square(x):
    return x * x

print(sum_of_greater(1, 2, 3))
print(sum_of_greater(1, 1, 1))
print(sum_of_greater(1, 2, 2))
print(sum_of_greater(1, 1, 2))
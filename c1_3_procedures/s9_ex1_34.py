from util import square

def f(g):
    return g(2)

print(f(square))
print(f(lambda z: z * (z + 1)))
# print(f(f))
from util import square
from util import repeated

def smooth(f):
    dx = 0.00001

    return lambda x: (f(x - dx) + f(x) + f(x + dx)) / 3

print(repeated(smooth(square), 2)(5))
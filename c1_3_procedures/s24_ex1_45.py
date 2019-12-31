from math import log
from math import floor

from util import fixed_point
from util import average_damp
from util import repeated

def n_sqrt(x, n):
    def log2(x):
        return log(x) / log(2)

    return fixed_point(repeated(average_damp, floor(log2(n)))(lambda y: x / pow(y, n - 1)), 1.0)

print(n_sqrt(32, 5))
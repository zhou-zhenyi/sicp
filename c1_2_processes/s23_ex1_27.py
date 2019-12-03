import sys
sys.setrecursionlimit(10000000)

from util import square
from util import even

def fermat_test(a, n):
    def expmod(base, exp, m):
        if exp == 0:
            return 1
        elif even(exp):
            return square(expmod(base, exp / 2, m)) % m
        else:
            return base * expmod(base, exp - 1, m) % m
    
    if a == n:
        return True
    elif expmod(a, n, n) == a and a < n:
        return fermat_test(a + 1, n)
    else:
        return False

def check_carmichael(n):
    return fermat_test(1, n)

print(check_carmichael(112))
print(check_carmichael(113))
print(check_carmichael(561))
print(check_carmichael(1105))
print(check_carmichael(1729))
print(check_carmichael(2465))
print(check_carmichael(2821))
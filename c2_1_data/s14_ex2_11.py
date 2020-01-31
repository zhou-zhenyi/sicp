from util_interval import make_interval, lower_bound, upper_bound, print_interval
from util_interval import add_interval, sub_interval, div_interval

def mul_interval(x, y):
    lx = lower_bound(x)
    ux = upper_bound(x)
    ly = lower_bound(y)
    uy = upper_bound(y)
    
    if lx > 0 and ux > 0:
        if ly > 0 and uy > 0:
            return make_interval(lx * ly, ux * uy)
        elif ly < 0 and uy < 0:
            return make_interval(ux * ly, lx * uy)
        else:
            return make_interval(ux * ly, ux * uy)
    elif lx < 0 and ux < 0:
        if ly > 0 and uy > 0:
            return make_interval(ux * ly, lx * uy)
        elif ly < 0 and uy < 0:
            return make_interval(ux * uy, lx * ly)
        else:
            return make_interval(lx * uy, lx * ly)
    else:
        if ly > 0 and uy > 0:
            return make_interval(lx * uy, ux * uy)
        elif ly < 0 and uy < 0:
            return make_interval(ux * ly, lx * ly)
        else:
            l1 = lx * uy
            l2 = ux * ly
            u1 = lx * ly
            u2 = ux * uy

            return make_interval(min([l1, l2]), max([u1, u2]))

zx1 = make_interval(2, 5)
zx2 = make_interval(-6, -3)
zx3 = make_interval(-4, 7)

zy1 = make_interval(3, 4)
zy2 = make_interval(-5, -2)
zy3 = make_interval(-1, 6)

print_interval(mul_interval(zx1, zy1))
print_interval(mul_interval(zx1, zy2))
print_interval(mul_interval(zx1, zy3))
print_interval(mul_interval(zx2, zy1))
print_interval(mul_interval(zx2, zy2))
print_interval(mul_interval(zx2, zy3))
print_interval(mul_interval(zx3, zy1))
print_interval(mul_interval(zx3, zy2))
print_interval(mul_interval(zx3, zy3))
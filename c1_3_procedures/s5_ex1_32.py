from util import logl
from util import newl
from util import identity
from util import inc
from util import add
from util import mul

def accu_recu(combiner, null_value, term, a, next, b):
    logl("(" + str(a) + ", " + str(b) + ")")

    if a > b:
        return null_value
    else:
        return combiner(term(a), accu_recu(combiner, null_value, term, next(a), next, b))

def accu_iter(combiner, null_value, term, a, next, b):
    def iter(a, result):
        logl("(" + str(a) + ", " + str(result) + ")")

        if a > b:
            return result
        else:
            return iter(next(a), combiner(a, result))

    return iter(a, null_value)

def sum_recu(a, b):
    return accu_recu(add, 0, identity, a, inc, b)

def sum_iter(a, b):
    return accu_iter(add, 0, identity, a, inc, b)

def prod_recu(a, b):
    return accu_recu(mul, 1, identity, a, inc, b)

def prod_iter(a, b):
    return accu_iter(mul, 1, identity, a, inc, b)

print(sum_recu(1, 6))
newl()

print(sum_iter(1, 6))
newl()

print(prod_recu(1, 6))
newl()

print(prod_iter(1, 6))
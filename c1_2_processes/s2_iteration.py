from util import logl

def factorial(n):
    return fact_iter(1, 1, n)

def fact_iter(product, counter, max_count):
    logl("(" + str(product) + ", " + str(counter) + ", " + str(max_count) + ")")

    if counter > max_count:
        return product
    else:
        return fact_iter(counter * product, counter + 1, max_count)

print(factorial(6))
def cons(x, y):
    def dispatch(m):
        if m == 0:
            return x
        elif m == 1:
            return y
        else:
            print("Argument not 0 or 1 -- CONS " + m)
    
    return dispatch

def car(z):
    return z(0)

def cdr(z):
    return z(1)

def list(items):
    sequence = None
    items.reverse()

    for item in items:
        sequence = cons(item, sequence)

    return sequence

def print_list(list):
    a = car(list)
    b = cdr(list)

    string = "(" + str(a)

    while b != None:
        a = car(b)
        b = cdr(b)
        string = string + " " + str(a)
    else:
        print(string + ")")
        return
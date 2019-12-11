num = 0

def line():
    global num
    num += 1
    return num

def newl():
    global num
    num = 0

def logl(msg):
    print(str(line()) + ": " + msg)

def square(x):
    return x * x

def double(x):
    return x + x

def halve(x):
    return x / 2

def even(n):
    return n % 2 == 0

def cube(x):
    return x * x * x

def inc(n):
    return n + 1
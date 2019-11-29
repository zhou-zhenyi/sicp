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
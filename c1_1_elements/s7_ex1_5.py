def p():
    p()

def test(x, y):
    if x == 0:
        0
    else:
        p()

test(0, p())
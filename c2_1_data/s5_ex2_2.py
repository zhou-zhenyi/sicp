from util_pair import cons, car, cdr
from util import average

def make_segment(start, end):
    return cons(start, end)

def start_segment(segment):
    return car(segment)

def end_segment(segment):
    return cdr(segment)

def make_point(x, y):
    return cons(x, y)

def x_point(point):
    return car(point)

def y_point(point):
    return cdr(point)

def print_point(point):
    print("(" + str(x_point(point)) + ", " + str(y_point(point)) + ")")

def midpoint_segment(segment):
    return cons(average(x_point(start_segment(segment)),
                        x_point(end_segment(segment))),
                average(y_point(start_segment(segment)),
                        y_point(end_segment(segment))))

a = make_point(1, 2)
b = make_point(5, 4)
x = make_segment(a, b)
c = midpoint_segment(x)

print_point(c)
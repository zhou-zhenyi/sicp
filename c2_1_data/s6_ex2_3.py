from util import cons, car, cdr
from util import double

def make_point(x, y):
    return cons(x, y)

def x_point(point):
    return car(point)

def y_point(point):
    return cdr(point)

def make_rectangle(left_top, right_bottom):
    return cons(left_top, right_bottom)

def left_top(rectangle):
    return car(rectangle)

def right_bottom(rectangle):
    return cdr(rectangle)

def rectangle_perimeter(rectangle):
    return double((x_point(right_bottom(rectangle)) - x_point(left_top(rectangle))) + 
                  (y_point(left_top(rectangle)) - y_point(right_bottom(rectangle))))

def rectangle_area(rectangle):
    return ((x_point(right_bottom(rectangle)) - x_point(left_top(rectangle))) *
            (y_point(left_top(rectangle)) - y_point(right_bottom(rectangle))))

a = make_point(1, 7)
b = make_point(6, 4)
x = make_rectangle(a, b)

print(str(rectangle_perimeter(x)))
print(str(rectangle_area(x)))

def make_rectangle_2(left_top, x, y):
    return cons(left_top, make_point(x_point(left_top) + x, y_point(left_top) - y))

y = make_rectangle_2(a, 5, 3)

print(str(rectangle_perimeter(y)))
print(str(rectangle_area(y)))
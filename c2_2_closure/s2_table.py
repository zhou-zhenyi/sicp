from util_pair import cons, car, cdr, list, null, print_list

x = cons(1, cons(2, cons(3, cons(4, None))))
print_list(x)

def list_ref(items, n):
    if (n == 0):
        return car(items)

    return list_ref(cdr(items),  n - 1)

squares = list([1, 4, 9, 16, 25])
print(list_ref(squares, 3))

def length(items):
    if (null(items)):
        return 0
    
    return 1 + length(cdr(items))

odds = list([1, 3, 5, 7])
print(length(odds))

def append(list1, list2):
    if null(list1):
        return list2

    return cons(car(list1), append(cdr(list1), list2))

print_list(append(squares, odds))
print_list(append(odds, squares))
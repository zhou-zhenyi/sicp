from util_pair import cons, car, cdr, list, print_list

x = cons(1, cons(2, cons(3, cons(4, None))))
print_list(x)

one_through_four = list([1, 2, 3, 4])
print_list(one_through_four)
print(car(one_through_four))
print_list(cdr(one_through_four))
print(car(cdr(one_through_four)))
print_list(cons(10, one_through_four))
print_list(cons(5, one_through_four))
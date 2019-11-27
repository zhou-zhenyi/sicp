def pascal_triangle(n):
    def sum_of_nodes(sum, i, n):
        def node(i, n):
            if i == 1 or i == n:
                return 1
            else:
                return node(i - 1, n - 1) + node(i, n - 1)

        if n == 0:
            return sum
        elif i == 0:
            return sum_of_nodes(sum, n - 1, n - 1)
        else:
            return sum_of_nodes(sum + node(i, n), i - 1, n)

    return sum_of_nodes(0, n, n)

print(pascal_triangle(1))
print(pascal_triangle(2))
print(pascal_triangle(3))
print(pascal_triangle(4))
print(pascal_triangle(5))
print(pascal_triangle(6))
print(pascal_triangle(7))
        
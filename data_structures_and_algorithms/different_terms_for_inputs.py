def print_items(a, b):
    # this is O(a)
    for i in range(a):
        print(i)

    # this is O(b)
    for j in range(b):
        print(j)

    # O(a+b)


def print_items_two(a, b):
    # this is O(a*b)
    for i in range(a):
        for j in range(b):
            print(i, j)


print_items(1, 10)
print_items_two(1, 10)

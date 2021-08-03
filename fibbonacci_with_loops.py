def fib(n):
    first_num = 0
    second_num = 1

    if n <= 0:
        return -1

    if n == 1:
        return first_num

    if n == 2:
        return second_num

    k = 3
    while k <= n:
        fib_num = first_num + second_num
        first_num = second_num
        second_num = fib_num
        k += 1

    return fib_num


fib_of = 7
print(fib(fib_of))

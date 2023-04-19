#!/bin/python3

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonely_integer(a:list):
    for num in a:
        if a.count(num) == 1:
            return num


if __name__ == '__main__':
    a = [1, 2, 3, 4, 3, 2, 1]
    result = lonely_integer(a)
    print(result)


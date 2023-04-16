#!/bin/python3


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()

    min = sum(arr[:-1])
    max = sum(arr[1:])
    print(f"{min} {max}")


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]  # list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

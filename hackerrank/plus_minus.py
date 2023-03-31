#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive_ratio = len([num for num in arr if num > 0]) / len(arr)
    negative_ratio = len([num for num in arr if num < 0]) / len(arr)
    zero_ratio = len([num for num in arr if num == 0]) / len(arr)
    print("{:.6f}".format(positive_ratio))
    print("{:.6f}".format(negative_ratio))
    print("{:.6f}".format(zero_ratio))


if __name__ == '__main__':
    n = 6  # int(input().strip())

    arr = [-4, 3, -9, 0, 4, 1]  # list(map(int, input().rstrip().split()))

    plusMinus(arr)

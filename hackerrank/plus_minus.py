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

def plus_minus(array):
    # Write your code here
    positive_ratio = len([num for num in array if num > 0]) / len(array)
    negative_ratio = len([num for num in array if num < 0]) / len(array)
    zero_ratio = len([num for num in array if num == 0]) / len(array)
    print("{:.6f}".format(positive_ratio))
    print("{:.6f}".format(negative_ratio))
    print("{:.6f}".format(zero_ratio))


if __name__ == '__main__':
    n = 6  # int(input().strip())
    arr = [-4, 3, -9, 0, 4, 1]  # list(map(int, input().rstrip().split()))
    plus_minus(arr)

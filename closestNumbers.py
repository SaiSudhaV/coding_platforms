#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr, n):
    temp1, res = sorted(arr), []
    min_value = min([temp1[i+1] - temp1[i] for i in range(n - 1)])
    for i in range(n - 1):
        if (temp1[i+1] - temp1[i]) == min_value:
            res.append(temp1[i])
            res.append(temp1[i + 1])
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr, n)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

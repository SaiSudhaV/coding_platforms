#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(ar, k, n):
    res, i = 100 - (ar[k % n] * 2 + 1) , k % n
    while i:
        i = (i + k) % n
        res -= ar[i] * 2 + 1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n, k = map(int, input().split())
    ar = list(map(int, input().split()))

    result = jumpingOnClouds(ar, k, n)

    fptr.write(str(result) + '\n')

    fptr.close()

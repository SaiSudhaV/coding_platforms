#!/bin/python

import math
import os
import random
import re
import sys

# Complete the larrysArray function below.
def larrysArray(A):
    n = len(A)
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] > A[j]:
                res += 1
    return "YES" if res % 2 == 0 else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        A = map(int, raw_input().rstrip().split())

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()

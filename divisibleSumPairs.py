#!/bin/python

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):     
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    return count

if __name__ == '__main__':
    nk = raw_input().split()
    n = int(nk[0])
    k = int(nk[1])
    ar = map(int, raw_input().rstrip().split())
    result = divisibleSumPairs(n, k, ar)
    print(str(result) + '\n')

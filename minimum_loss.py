#!/bin/python3

import math
import os
import random
import re
import sys
from math import inf
#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(ar, br):
    res = inf
    for i in range(n - 1):
        if ar.index(br[i + 1]) < ar.index(br[i]) and br[i + 1] - br[i] < res:
            res = br[i + 1] - br[i]
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().split()))

    result = minimumLoss(price, sorted(price))

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

def workbook(n, k, arr):
    res, tem, i, p = 0, 1, 0, 1
    while i < n:
        if tem <= p:
            if p <= min(tem + k - 1, ar[i]):
                res += 1
        tem, p = tem + k, p + 1
        if ar[i] < tem:
            tem, i = 1, i + 1
    return res

if __name__ == "__main__":
    n, k = map(int, input().split())
    ar = list(map(int, input().split()))
    print(workbook(n, k, ar))
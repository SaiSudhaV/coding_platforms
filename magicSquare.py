#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
magicSquare = [[8,1,6,3,5,7,4,9,2], [6,1,8,7,5,3,2,9,4], [4,9,2,3,5,7,8,1,6], [2,9,4,7,5,3,6,1,8], [8,3,4,1,5,9,6,7,2], [4,3,8,9,5,1,2,7,6], [6,7,2,1,5,9,8,3,4], [2,7,6,9,5,1,4,3,8]]

def calculate_cost(ques, ar):
    return sum(abs(i - j) for i, j in zip(ques, ar))

def formingMagicSquare(ar, n):
    res = 9999999
    if ar in magicSquare:
        return 0
    for i in range(n):
        cost = calculate_cost(ar, magicSquare[i])
        res = min(cost, res)
    return res

if __name__ == '__main__':
    ar, n = [], len(magicSquare)
    for i in range(3):
        a1, a2, a3 = map(int, input().split())
        ar.append(a1)
        ar.append(a2)
        ar.append(a3)
    result = formingMagicSquare(ar, n)
    print(str(result))

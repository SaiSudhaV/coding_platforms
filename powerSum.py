#!/bin/python3

import math
import os
import random
import re
import sys

def powerSum(X, N, k):
    res = k ** N
    k += 1
    return 1 if res == X else 0 if res > X else powerSum(X, N, k) + powerSum(X - res, N, k)

if __name__ == '__main__':
    X = int(input())
    N = int(input())
    result = powerSum(X, N, 1)
    print(str(result))
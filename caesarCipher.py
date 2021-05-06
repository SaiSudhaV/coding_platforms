#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    res = []
    for i in s:
        num = ord(i)
        res.append(chr(((num - 97 + k) % 26) + 97) if 97 <= num <= 122 else chr(((num - 65 + k) % 26) + 65) if 65 <= num <= 90 else i)
    return ''.join([i for i in res])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    tem = "abcdefghijklmnopqrstuvwxyz "
    return "pangram" if set([i.lower() for i in s]) == set([i for i in tem]) else "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')
    fptr.close()
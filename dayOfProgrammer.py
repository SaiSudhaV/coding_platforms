#!/bin/python

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def isLeap(year):
    return True if ((year <= 1917) & (year % 4 == 0)) or ((year > 1918) & (year % 400 == 0 or ((year % 4 == 0) & (year % 100 != 0)))) else False

def dayOfProgrammer(year):
    dd = 256 - 244 if isLeap(year) else 256 - 243
    mm, yyyy = "09" , year
    date = [dd, mm, yyyy]
    return "26.09.1918" if year == 1918 else ".".join([str(i) for i in date])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(raw_input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()

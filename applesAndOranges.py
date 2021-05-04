import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesCount = [i for i in apples if a + i >= s]
    orangesCount = [i for i in apples if a + i >= s]
    lst = [len(applesCount), len(orangesCount)]
    return '\n'.join(map(str, lst))

if __name__ == '__main__':
    st = raw_input().split()

    s = int(st[0])

    t = int(st[1])

    ab = raw_input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = raw_input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = map(int, raw_input().rstrip().split())

    oranges = map(int, raw_input().rstrip().split())

    print(countApplesAndOranges(s, t, a, b, apples, oranges))

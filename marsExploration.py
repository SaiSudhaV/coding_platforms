#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    res = 0
    tem = "SOS"
    for i in range(len(s)):
        if s[i] != tem[i % 3]:
            res += 1
    return res

if __name__ == '__main__':
    s = input()
    print(marsExploration(s))
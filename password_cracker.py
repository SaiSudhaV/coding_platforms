#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'passwordCracker' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY passwords
#  2. STRING loginAttempt
#

def passwordCracker(passwords, loginAttempt, res, k):
    for i in range(1, len(loginAttempt) + 1):
        if loginAttempt[:i] in passwords:
            temp = k + [loginAttempt[:i]]
            if i >= len(loginAttempt):
                res.append(temp)
            else:
                passwordCracker(passwords, loginAttempt[i:], res, temp)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        passwords = list(map(str, input().split()))
        loginAttempt = input()
        res = []
        passwordCracker(passwords, loginAttempt, res, []) 
        res = [j for i in res for j in i]
        print("WRONG PASSWORD" if not res else " ".join(str(i) for i in res))

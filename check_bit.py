import os
import sys

def checkBit(n, i):
    lst = [j for j in str(n)]
    if(lst[i - 1] == '1'):
        return "true"
    return "false"

if __name__ == '__main__':
    
    x, y = input().split()
    num, i = [int(x) for x in [x, y]]
    
    result = checkBit(num, i)
    print(result)

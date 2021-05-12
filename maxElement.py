import os
import random
import re
import sys

def find_largest(ar):
    return max(ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    
    ar = list(map(int, input().rstrip().split()))
    result = find_largest(ar)
    
    fptr.write(str(result) + '\n')
    
    fptr.close()

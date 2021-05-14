import os
import sys

def oddElementSum(ar):
    return sum([i for i in ar if i % 2 != 0])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    ar_count = int(input())
    
    ar = list(map(int, input().rstrip().split()))
    
    result = oddElementSum(ar)
    
    fptr.write(str(result) + '\n')
    
    fptr.close()

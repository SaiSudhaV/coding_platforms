import os
import sys

def reverse(ar):
    lst = [i for i in ar]
    lst1 = reversed(lst)
    
    return ' '.join([str(elem) for elem in lst1]) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    ar_count = int(input())
    
    ar = list(map(int, input().rstrip().split()))
    
    result = reverse(ar)
    
    fptr.write(result + '\n')
    
    fptr.close()

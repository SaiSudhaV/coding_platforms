import os
import sys

def harshard(n):
    if 1 <= n <= pow(10, 9):
        lst = [int(i) for i in str(n)]
        if (n % sum([i for i in lst]) == 0):
            return "Yes"
        return "No"
    
    
if __name__ == '__main__':
    n =int(input())
    
    result = harshard(n)
    print(result)

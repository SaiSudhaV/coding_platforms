import sys
import os

def nextRound(arr, n, k):
    count = 0 
    for i in range(n):
        if 0 < arr[i] >= arr[k - 1] :
            count += 1
    return count
 
if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split())
    print(nextRound(arr, n, k))

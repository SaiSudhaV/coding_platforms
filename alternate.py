# cook your dish here
import numpy

def alternate(arr, n):
    res = [1 for i in range(n)]
    for i in range(n - 2, -1, -1):
        if ( arr[i] > 0 and arr[i + 1] < 0 )or ( arr[i] < 0 and arr[i + 1] > 0 ) :
            res[i] += res[i + 1]
    return " ".join(str(i) for i in res)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        print(alternate(arr, n))

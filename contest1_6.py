import sys

def find_ceil(ar, n, k):
    res, low, high = sys.maxsize, 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if ar[mid] == k:
            return ar[mid]
        elif ar[mid] < k:
            low = mid + 1
        else:
            res = ar[mid]
            high = mid - 1
    return res
    
if __name__ == "__main__":
    n = int(input())
    ar = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        k = int(input())
        print(find_ceil(sorted(ar), n, k))
# cook your dish here

from math import inf

def min_diff(ar, n):
    res = inf
    for i in range(n):
        if i != n - 1:
            tem = ar[i + 1] - ar[i]
            res = min(res, tem)
        else:
            break
    return res

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, ar = int(input()), list(map(int, input().split()))
        print(min_diff(sorted(ar), n))
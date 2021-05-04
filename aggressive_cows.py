def binary_search(ar, n, p):
    res, low, high = 0, 0, n
    while low <= high:
        mid = (high + low) // 2
        if is_valid(ar, n, mid, p):
            low, res = mid + 1, mid
        else:
            high = mid - 1
    return res

def is_valid(ar, n, k, p):
    int tem, res = 1, ar[0]
    for i in range(1, n):
        if ar[i] - res >= k:
            tem += 1
            if tem == p:
                return True
            res = ar[i]
    return False

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        ar = []
        for i in range(n):
            ar.append(int(input()))
        print(binary_search(ar, n, k))
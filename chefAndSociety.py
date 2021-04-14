def chefAndSociety(arr, n, t):
    m = arr[n // 2 - 1]
    res = []
    for i in range(n - 1):
        tem = [max(abs(arr[j] - m), 0) for j in range(i + 1, n)]
        s = sum(tem)
        if s > t:
            res.append(s)
    return " ".join([str(i) for i in [m, min(res) + 1]])
    
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, t = map(int, input().split())
        arr = list(map(int, input().split()))
        print(chefAndSociety(arr, n, t))
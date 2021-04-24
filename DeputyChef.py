def deputyChef(a, d):
    res = []
    for i in range(n):
        if(a[i - 1] + a[(i + 1) % n] < d[i]):
            res.append(d[i])
    if(res):
        return max(res)
    else:
        return -1

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        d = list(map(int,input().split()))
        print(deputyChef(a, d))
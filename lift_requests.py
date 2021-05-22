# cook your dish here

def solve(ar, n):
    res = [ar[0]]
    for i in range(n):
        res.append(abs(ar[i] - ar[i + 1]))
    return sum(res)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        ar = []
        n, k = map(int, input().split())
        for i in range(k):
            x, y = map(int, input().split())
            ar.append(x)
            ar.append(y)
        print(solve(ar, len(ar) - 1))
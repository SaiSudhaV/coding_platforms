# cook your dish here

def total_points(a, b, n):
    res = []
    for i in range(n):
        tem = 0 if (a[i] * 20 - b[i] * 10) < 0 else a[i] * 20 - b[i] * 10
        res.append(tem)
    return max(res)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a, b = list(map(int, input().split())), list(map(int, input().split()))
        print(total_points(a, b, n))
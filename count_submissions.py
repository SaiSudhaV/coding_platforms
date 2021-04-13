# cook your dish here

def submissionCount(a, b, n):
    res = 0
    for i in range(n):
        if b[i] > 5 + a[i]:
            res += 1
    return res

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        a, b = [], []
        for i in range(n):
            tem = input().split()
            a.append(int(tem[0]))
            b.append(int(tem[1]))
        print(submissionCount(a, b, n))
# cook your dish here

def determine(ar, m, n):
    ar = [i for i in range(n) if i in  ar]
    res1, res2 = [], []
    for i in range(len(ar)):
        if i % 2:
            res1.append(ar[i])
        else:
            res2.append(ar[i])
    return "\n".join(i for i in [" ".join(str(i) for i in res2), " ".join(str(i) for i in res1)])

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        m, n = map(int, input().split())
        ar = list(map(int, input().split()))
        print(determine([i for i in range(1, m + 1)], m, n))
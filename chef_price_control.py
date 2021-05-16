# cook your dish 

def revenue_amount(ar, n, k):
    res = []
    for i in ar:
        if i > k:
            res.append(i - k)
    return sum(res)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        ar = list(map(int, input().split()))
        print(revenue_amount(ar, n, k))
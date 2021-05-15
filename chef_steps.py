# cook your dish here

def is_traversable(ar, n, k):
    res = []
    for i in ar:
        if i % k:
            res.append(0)
        else:
            res.append(1)
    return "".join(str(i) for i in res)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        ar = list(map(int, input().split()))
        print(is_traversable(ar, n, k))
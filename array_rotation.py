# cook your dish here

def f(ar, n, k):
    ar = ar[-k:] + ar[: n - k]
    return ar
    
def concat(ar, br):
    res = ar
    for i in br:
        res.append(i)
    return res

def array_rotation(ar, qr, t):
    res = []
    for i in qr:
        ar = concat(ar, f(ar, len(ar), i))
        res.append(sum(ar))
    return "\n".join(str(i) for i in res)

if __name__ == "__main__":
    n = int(input())
    ar = list(map(int, input().split()))
    t = int(input())
    qr = list(map(int, input().split()))
    print(array_rotation(ar, qr, t))
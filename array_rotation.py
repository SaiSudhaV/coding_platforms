# cook your dish here

def array_rotation(k, t):
    res = []
    for i in range(t):
        k = (k * 2) % 1000000007
        res.append(k)
    return "\n".join(str(i) for i in res)

if __name__ == "__main__":
    n = int(input())
    ar = list(map(int, input().split()))
    t = int(input())
    qr = list(map(int, input().split()))
    print(array_rotation(sum(ar), t))
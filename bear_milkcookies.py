# cook your dish here

def check(ar, n):
    res = 1
    if ar[-1] != "cookie":
        for i in range(n):
            if ar[i] == "cookie" and ar[i + 1] != "milk":
                res = 0
                break
        return "YES" if res != 0 else "NO"
    return "NO"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, ar = int(input()), input().split()
        print(check(ar, n))
def fact(n):
    if n == 0 or n == 1:
        return n
    else:
        return n * fact(n - 1)

def ncr(n, r):
    return fact(n) / (fact(n - r) * fact(r))

def evenSubstrings(s):
    return int(ncr(len(s), 2))

if __name__ == "__main__":
    n = int(input())
    k = str(input())
    if len(k) <= n: 
        res = evenSubstrings(k)
        print(res)

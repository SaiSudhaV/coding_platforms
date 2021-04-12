def does_subset_exist(ar, n):
    tem = 0
    if n == 1:
        return "YES" if check2power(ar[0]) else "NO"
    for i in range(32):
        tem |= (1 << i)
    for i in range(32):
        res, k = tem, 1 << i
        for j in range(n):
            if ar[j] & k:
                res &= ar[j]
        if check2power(res):
            return "YES"
    return "NO"

def check2power(n):
    return n & (n - 1) == 0 and n
    
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        ar = list(map(int, input().split()))
        print(does_subset_exist(ar, n))
def gen_LPS(s, n):
    lps = [0] * n
    m, i = 0, 1
    while i < n:
        if s[i] == s[m]:
            m += 1
            lps[i] = m
            i += 1
        else:
            if m != 0:
                m = lps[m - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def substring_available(s, n):
    idx = 1
    for i in range(n - 1, -1, -1):
        if s[i]==0:
            idx = i + 1
            break
    if s[-1] == n - idx and s[-1] % idx == 0:
        return idx
    return n

def find_substring(s, n):
    lps = gen_LPS(s, n)
    m, i = substring_available(lps, len(lps)), 1
    while True:
        if ((i * (i + 1)) // 2) % m == 0:
            return i
        i += 1
            
def hcf(x, y):
    return y if x % y == 0 else hcf(y, x % y)

def solve(A):
    res = 1
    for i in A:
        tem = find_substring(i, len(i))
        res = (res * tem) // hcf(tem, res)
    return res % 1000000007
# cook your dish here

def even_term_sum(n, p, a, d):
    return p * ((n // 2) * (2 * a + (n - 1) * d))

def odd_term_sum(n, p, a, d):
    return p * (n * (a + ((n - 1)) // 2) * d)

def solve(D, d, p, q, n):
    return (D % d) * (p + n * q)

def amount_printed(D, d, P, Q):
    n = D // d
    res = even_term_sum(n, d, P, Q) if n % 2 == 0 else odd_term_sum(n, d, P, Q)
    return res + solve(D, d, P, Q, n)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        D, d, P, Q = map(int, input().split())
        print(amount_printed(D, d, P, Q))
def factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]
    
def primeFactors(n):
    return [i for i in range(2, n) if n % i == 0]

def strangeNumber(n, k):
    res = 0
    for i in range(1, 1000000000):
        if len(factors(i)) == n and len(primeFactors(i)) == k:
            res = 1
            break
    return 0 if res == 0 else 1
    
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        print(strangeNumber(n, k))

import math

def evenOdds(k, n):
    temp = math.ceil(n / 2) if n & 1 else n / 2
    return (2 * k - 1) if k <= temp else (2 * (k - temp))
    
if __name__ == "__main__":
    n, k = map(int, input().split())
    print(int(evenOdds(k, n)))

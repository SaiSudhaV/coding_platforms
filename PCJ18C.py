import math
def polygonCakes(n, a, k):
        num = n * (n - 1) * a + (k - 1) * ((n - 2) * 360 - 2 * a * n)
        den = n * (n - 1)
        x = num // math.gcd(num,den)
        y = den // math.gcd(num,den)
        print("%d %d"%(x, y))
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, a, k = map(int,input().split())
        polygonCakes(n, a, k)
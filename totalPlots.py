# cook your dish here
from math import gcd

def totalPlot(n, m):
    return (n * m) // (gcd(n, m) ** 2)
  
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = map(int,input().split())
        print(totalPlot(n, m))

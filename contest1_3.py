from math import sqrt as sq

def divisors(n):
    res = []
    for i in range(1, int(sq(n)) + 1):
        if (n % i == 0) :
            res.append(2 if n // i != i else 1)
    return sum(res)
    
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print(divisors(n))

# cook your dish here

def factorial(n):
    res = 0
    while n >= 5:
        n //= 5
        res += n
    return res

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print(factorial(n))
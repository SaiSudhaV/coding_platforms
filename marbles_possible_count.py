# your code goes here

def factorial(n):
    return 1 if n == 0 or n == 1 else n * factorial(n - 1)

def possible_chances(n, k, p):
    tem, s, s1 = 1, max(k, p), min(k, p)
    for i in range(s, n):
        tem *= i + 1
    res = tem // factorial(s1)
    return res

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        print(possible_chances(n - 1, k - 1, n - k))
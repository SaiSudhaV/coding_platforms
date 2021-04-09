# cook your dish here

def calculatorOutput(n, k):
    res, tem = 0, 1
    while n > 0 or k > 0:
        res += ((n + k) % 10) * tem
        tem, n, k = 10, n // 10, k // 10
    return res

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        print(calculatorOutput(n, k))
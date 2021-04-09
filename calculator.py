# cook your dish here

def calculatorOutput(n, k):
    res = ""
    while n > 0 or k > 0:
        tem = ((n % 10) + (k % 10)) % 10
        res, n, k = res + str(tem), n // 10, k // 10
    return int(res[::-1])

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        print(calculatorOutput(n, k))
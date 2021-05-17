# cook your dish here

def modular_equation(n, m):
    res, tem = [], [1] * (n + 1)
    for i in range(2, n + 1):
        res.append(tem[m % i])
        j = m % i
        while j < n + 1:
            tem[j] += 1
            j += i
    return sum(res)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        print(modular_equation(n, m))
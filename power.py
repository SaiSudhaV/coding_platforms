#your code goes here 

def calculate(x, n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return calculate(x, n - 1) * x
    res = calculate(x, n >> 1)
    return res ** 2

if __name__ == "__main__":
    while True:
        n, k = map(int, input().split())
        if n == 0 and k == 0:
            break
        print(calculate(n, k))
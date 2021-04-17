#your code goes here 

def calculate(x, n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return calculate(x, n - 1) * x % 1000000007
    res = calculate(x, n >> 1)
    return res ** 2

def possible_id_count(n, k):
    num = calculate(n, k + 1) - 1 + 1000000007
    den = calculate(n - 1, 1000000007 - 2)
    return num * den % 1000000007 - 1

if __name__ == "__main__":
    while True:
        n, k = map(int, input().split())
        if n == 0 and k == 0:
            break
        print(possible_id_count(n, k))
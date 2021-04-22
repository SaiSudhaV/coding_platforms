#your code goes here

def calculate_sums(n):
    res = [n * (n + 1) / 2, n * (n + 1), n ** 2, (n * (n + 1) * (2 * n + 1)) / 6, (n * (n + 1) / 2) ** 2]
    res = [int(i) for i in res]
    return " ".join(str(i) for i in res)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print(calculate_sums(n))
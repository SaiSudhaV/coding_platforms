# cook your dish here

def possible_difference(ar, n):
    res = ar[-1]
    for i in range(n - 1):
        res = min(ar[i + 1] - ar[i], res)
    return res

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, ar = int(input()), list(map(int, input().split()))
        print(possible_difference(sorted(ar), n))
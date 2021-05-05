#your code goes here

def solve(ar, n):
    return ar[n // 2]

if __name__ == "__main__":
    n = int(input())
    ar = []
    for i in range(n):
        ar.append(input())
    print(solve(sorted(ar), n))
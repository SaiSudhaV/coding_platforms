# your code goes here

def find_optimal_split(ar, n):
    res = [abs(ar[i + 1] - ar[i]) for i in range(n)]
    return min(res)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        ar = list(map(int, input().split()))
        print(find_optimal_split(sorted(ar), n - 1))
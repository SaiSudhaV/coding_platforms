# cook your dish here

def solve(n, k):
    if n % 2 == 0 and k % 2 == 0:
        return "YES" if abs(n - k) == 2 else "NO"
    elif n % 2 == 0 and k % 2 != 0:
        return "YES" if n == k + 1 else "NO"
    elif n % 2 != 0 and k % 2 == 0:
        return "YES" if k == n + 1 else "NO"
    elif n % 2 != 0 and k % 2 != 0:
        return "YES" if abs(n - k) == 2 else "NO"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        print(solve(n, k))
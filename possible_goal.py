# cook your dish here

def valid_goal(n, x, k):
    return "YES" if x % k == 0 or (n - x + 1) % k == 0 else "NO"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, x, k = map(int, input().split())
        print(valid_goal(n, x, k))
# cook your dish here

def valid_goal(n, x, k):
    tem1 = [k * i for i in range(n + 2)]
    tem2 = [n + 1 - (k * i) for i in range(n + 2)]
    return "YES" if x in tem1 or x in tem2 else "NO"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, x, k = map(int, input().split())
        print(valid_goal(n, x, k))
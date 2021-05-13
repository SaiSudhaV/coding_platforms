# cook your dish here

def is_happy(p):
    return "YES" if p % 2 else "NO"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, ar = int(input()), list(map(int, input().split()))
        print(is_happy(sum(ar)))
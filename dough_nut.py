#your code goes here

def is_capable(n, m, k):
    return "no" if m < (n * k) else "yes"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, m, k = map(int, input().split())
        print(is_capable(n, m, k))
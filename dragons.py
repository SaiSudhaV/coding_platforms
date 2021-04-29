# your code goes here

def can_move(ar, n, s):
    i = 0
    while i <= n - 1 and s > ar[i][0]:
        s += ar[i][1]
        i += 1;
    return "YES" if i > n - 1 else "NO"

if __name__ == "__main__":
    s, n = map(int, input().split())
    ar = []
    for i in range(n):
        x, y = map(int, input().split())
        ar.append([x, y])
    print(can_move(sorted(ar), n, s))
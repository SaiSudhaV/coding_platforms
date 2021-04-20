if __name__ == "__main__":
    t = int(input())
    a1, a2, a3 = [], [], []
    for i in range(t):
        x, y, z = map(int, input().split())
        a1.append(x)
        a2.append(y)
        a3.append(z)
    print("YES" if sum(a1) == sum(a2) == sum(a3) == 0 else "NO")

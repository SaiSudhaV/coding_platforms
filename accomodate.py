if __name__ == "__main__":
    t = int(input())
    add = 0
    for i in range(t):
        n, m = map(int, input().split())
        if m - n >= 2:
            add += 1
    print(add)

if __name__ == "__main__":
    t = int(input())
    res = 0
    for i in range(t):
        s = str(input())
        if s == "X++" or s == "++X":
            res = res + 1
        elif s == "X--" or s == "--X":
            res = res - 1
    print(res)

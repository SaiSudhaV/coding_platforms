def min_moves(h, w, h1, w1):
    res = 0
    while h > h1:
        h = h // 2 if (h // 2) < (h - h1) else h1
        res += 1
    while w > w1:
        w = w // 2 if (w // 2) < (w - w1) else w1
        res += 1
    return res

if __name__ == "__main__":
    h, w, h1, w1 = int(input()), int(input()), int(input()), int(input())
    if not (h < h1 or w < w1):
        print(min_moves(h, w, h1, w1))
def total_boxes_count(n, m, p, k):
    return k + (k - n) // (m - 1)

if __name__ == "__main__":
    t = int(input())
    while t:
        t -= 1
        n, m, p, k = map(int, input().split())
        print(total_boxes_count(n, m, p, k))
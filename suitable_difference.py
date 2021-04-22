#your code goes here

def suitable_difference(ar1, ar2, m, n):
    res, p1, p2 = 0xFFFFFF, 0, 0
    for i in ar1:
        while n > p1 + 1 and ar2[p1 + 1] <= i:
            p1 += 1
        while n > p2 + 1 and ar2[p2] < i:
            p2 += 1
        if ar2[p1] <= i:
            res = min(res, i - ar2[p1])
        if ar2[p2] >= i:
            res = min(res, ar2[p2] - i)
    return res

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        ar1, ar2 = list(map(int, input().split())), list(map(int, input().split()))
        print(suitable_difference(ar1[1:], ar2[1:], len(ar1), len(ar2)))
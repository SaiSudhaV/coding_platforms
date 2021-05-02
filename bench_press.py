# cook your dish here

from math import ceil

def collected_weights(ar, n, a, b):
    tem, res = set(), []
    for i in ar:
        if i in tem:
            res.append(i)
            tem.remove(i)
        else:
            tem.add(i)
    return "YES" if a <= b or sum(res) >= ceil((a - b) / 2) else "NO"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, a, b = map(int, input().split())
        ar = list(map(int, input().split()))
        print(collected_weights(ar, n, a, b))
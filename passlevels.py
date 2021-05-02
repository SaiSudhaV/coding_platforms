def sol(n, p, q):
    k, l = len(p), len(q)
    # initializes all the with 0’s 
    res = [0] * n
    for i in range(1, k):
        res[p[i] - 1] = -1
    for i in range(1, l):
        res[q[i] - 1] = -1
    for _ in res:
        if _ is 0:
            return "Oh, my keyboard!"
    return "I become the guy."
 
if __name__ == "__main__":
    n = int(input())
    p, q = list(map(int, input().split(" "))), list(map(int, input().split(" ")))
    print(sol(n, p, q))

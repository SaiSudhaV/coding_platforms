def distinct_pair_difference(ar, n):
    tem, res = [0 for i in range(n)], []
    tem[0] = ar[0]
    for i in range(1, n):
        tem[i] = tem[i - 1] + ar[i]
    for i in range(n):
        res.append((i + 1) * ar[i] - tem[i])
    return sum(res)
 
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, ar = int(input()), list(map(int, input().split()))
        print(distinct_pair_difference(ar, n))
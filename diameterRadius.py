#your code goes here

def minLightRadius(ar, n, k):
    res = []
    for i in range(1, n):
        res += [(ar[i] - ar[i - 1]) / 2]
    return max(res + [ar[0], k - ar[n - 1]])
 
if __name__ == "__main__":
    n, k = map(int, input().split())
    ar = list(map(int, input().split()))
    print(minLightRadius(sorted(ar), n, k))
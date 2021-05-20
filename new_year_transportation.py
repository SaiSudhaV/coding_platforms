# your code goes here

def can_construct(ar, n, k):
    res = []
    while sum(res) < k:
        res.append(ar[sum(res) - 1])
    return "YES" if sum(res) == k else "NO"
	
if __name__ == "__main__":
    n, k = map(int, input().split())
    ar = list(map(int, input().split()))
    print(can_construct(ar, n, k))
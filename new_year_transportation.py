# your code goes here

def can_construct(ar, n, k):
    res = 1
    while res < k:
        res += ar[res - 1]
    return "YES" if res == k else "NO"
	
if __name__ == "__main__":
    n, k = map(int, input().split())
    ar = list(map(int, input().split()))
    print(can_construct(ar, n, k))
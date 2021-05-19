# your code goes here

def min_operations(ar, n):
    tem = sorted(ar[:])
    if ar != tem:
        return 1 if ar[0] == 1 or ar[-1] == n else 3 if ar[0] == n and ar[-1] == 1 else 2
    return 0
	
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        ar = list(map(int, input().split()))
        print(min_operations(ar, n))
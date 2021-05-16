# your code goes here

def can_equally_distribute(a, b, c, n):
    total = sum([a, b, c, n])
    return "YES" if total % 3 == 0 and max(a, b, c) <= total // 3 else "NO"
	
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a, b, c, n = map(int, input().split())
        print(can_equally_distribute(a, b, c, n))
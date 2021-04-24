# your code goes here

def cookie_count(n, a, d):
	return int(n * (a + (n - 1) * d / 2))

if __name__ == "__main__":
	t = int(input())
	for i in range(t):
		n, a, d = map(int, input().split())
		print(cookie_count(n, a, d))
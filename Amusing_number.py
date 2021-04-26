# your code goes here

def kth_amusing_number(n):
	res = ""
	while n > 1:
		temp = '6' if n % 2 else '5'
		res = temp + res
		n //= 2
	return int(res)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print(kth_amusing_number(n + 1))
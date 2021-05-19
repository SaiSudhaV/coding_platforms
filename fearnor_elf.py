# your code goes here

import math

def radius(n, k):
    return n / 9.8 * math.sqrt(k * 19.6 + n ** 2)
	
if __name__ == "__main__":
    while True:
        n, k = map(int, input().split())
        if n == -1 and k == -1:
            break
        print("%.6f" % radius(n, k))
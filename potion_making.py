# your code goes here

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
    
def min_steps_potion_making(n):
    k = 100
    return k // gcd(n, k)
	
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print(min_steps_potion_making(n))
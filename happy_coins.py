# your code goes here

def last_coin(ar, n):
    return "hhb" if sum([1 for i in ar if i == 'lxh']) % 2 == 0 else "lxh"
	
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        ar = [input() for i in range(n)]
        print(last_coin(ar, n))
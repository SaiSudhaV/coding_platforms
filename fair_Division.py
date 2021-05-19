# your code goes here

def fair_division(ar, n):
    count_1, count_2 = ar.count(1), ar.count(2)
    return "NO" if (count_2 % 2 and not count_1) or count_1 % 2 else "YES"
	
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, ar = int(input()), list(map(int, input().split()))
        print(fair_division(ar, n))
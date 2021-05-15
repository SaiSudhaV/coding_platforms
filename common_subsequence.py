# your code goes here

def possible_smallest_subsequence(ar, br, n, m):
    res = 1
    for i in ar:
        if i in br:
            return " ".join(str(i) for i in ['YES\n1', i])
    return "NO"
	
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        ar, br = set(map(int, input().split())), set(map(int, input().split()))
        print(possible_smallest_subsequence(ar, br, n, m))
#your code goes here

from bisect import bisect_right as br

def possibledays(ar, n, q):
    return br(ar, q)

if __name__ == "__main__":
    n = int(input())
    ar =  list(map(int,input().split()))
    t = int(input())
    for i in range(t):
        q = int(input())
        print(possibledays(sorted(ar), n, q))
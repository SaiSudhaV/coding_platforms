# cook your dish here

def solve(ar, br, n, k):
    t1, t2 = 100, 100
    for i in range(n):
        if br[i] == 0:
            if t1 > ar[i]:
                t1 = ar[i]
        else:
            if t2 > ar[i]:
                t2 = ar[i]
    return "no" if t1 + t2 + k > 100 else "yes"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        ar, br = list(map(int, input().split())), list(map(int, input().split()))
        print(solve(ar, br, n, k))
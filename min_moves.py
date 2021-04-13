#your code goes here 

def min_moves(ar, br, n):
    tem1, tem2 = min(ar), min(br)
    res = [max(ar[i] - tem1, br[i] - tem2) for i in range(n)]
    return sum(res)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        ar, br = list(map(int, input().split())), list(map(int, input().split()))
        print(min_moves(ar, br, n))
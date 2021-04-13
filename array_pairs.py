#your code goes here 

def max_possible_sum(ar, br, n, k):
    i = 0
    while k and ar[i] < br[i]:
        ar[i] = br[i]
        i, k = i + 1, k - 1
    return sum(ar)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        ar, br = list(map(int, input().split())), list(map(int, input().split()))
        print(max_possible_sum(sorted(ar), sorted(br, reverse = True), n, k))
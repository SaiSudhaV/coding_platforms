#your code goes here

def solve(n):
    return 'Mishka' if n > 0 else 'Chris' if n < 0 else 'Friendship is magic!^^'

if __name__ == "__main__":
    t = int(input())
    tem = 0
    for i in range(t):
        n, k = map(int, input().split())
        tem += n > k 
        tem -= n < k
    print(solve(tem))
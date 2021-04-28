# your code goes here

def min_moves(n, k):
    return "-1" if n < k else ((n + 1) // 2 + k - 1) // k * k 

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(min_moves(n, k))
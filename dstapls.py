def distribution(n, k):
    return "YES" if (n // k) % k else "NO"
    
if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n, k=(map(int, input().split()))
        print(distribution(n, k))
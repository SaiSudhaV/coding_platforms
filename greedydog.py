def greedy(n, k):
    return max([n % i for i in range(1, k + 1)])
    
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        print(greedy(n, k))
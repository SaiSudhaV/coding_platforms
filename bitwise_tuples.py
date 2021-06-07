# cook your dish here

def aPowb(a, N):
    return pow((int)(a), (int)(N), 1000000007) % 1000000007

def tuple_count(n, m):
    return aPowb(aPowb(2, n) - 1, m)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        print(tuple_count(n , m))
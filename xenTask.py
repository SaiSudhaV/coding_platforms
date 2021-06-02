# cook your dish here

def total_min_time(ar, br, n):
    tem, tem1, tem2, tem3 = 0, 0, 0, 0
    for i in range(n):
        if tem != 0:
            tem2 += br[i]
            tem = 0
        else:
            tem2 += ar[i]
            tem = 1
    for i in range(n):
        if tem1 == 0:
            tem3 += br[i]
            tem1 = 1
        else:
            tem3 += ar[i]
            tem1 = 0
    return tem2 if tem3 > tem2 else tem3

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, ar, br = int(input()), list(map(int, input().split())), list(map(int, input().split()))
        print(total_min_time(ar, br, n))
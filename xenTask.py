# cook your dish here

def total_min_time(ar, br, n):
    tem1, tem2 = [], []
    for i in range(0, n, 2):
        tem1.append(br[i])
    for j in range(1, n, 2):
        tem1.append(ar[j])
    for i in range(0, n, 2):
        tem2.append(ar[j])
    for j in range(1, n, 2):
        tem2.append(br[j])
    return sum(tem1) if sum(tem1) > sum(tem2) else sum(tem2)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, ar, br = int(input()), list(map(int, input().split())), list(map(int, input().split()))
        print(total_min_time(ar, br, n))
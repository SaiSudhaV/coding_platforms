# cook your dish here

def find_pos(ar, n, k):
    return ar.index(k) + 1
    
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, ar, k = int(input()), list(map(int, input().split())), int(input())
        print(find_pos(sorted(ar), n, ar[k - 1]))
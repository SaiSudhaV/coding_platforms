# cook your dish here

def odd_sum(ar, n):
    return sum([i for i in ar if ar.index(i) % 2 == 0])

def total_min_time(ar, br, n):
    odd1, odd2, even1, even2 = odd_sum(ar, n), odd_sum(br, n), sum(ar) - odd_sum(ar, n), sum(br) - odd_sum(br, n)
    tem1, tem2 = odd2 + even1, odd1 + even2
    return tem2 if tem1 > tem2 else tem1

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, ar, br = int(input()), list(map(int, input().split())), list(map(int, input().split()))
        print(total_min_time(ar, br, n))
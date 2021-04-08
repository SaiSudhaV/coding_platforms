def taskTime(ar, n, x):
    return sum([x // i for i in ar])

def possible_min_time(ar, n, k, low, high):
    while low < high:
        mid = (low + high) >> 1
        tem = taskTime(ar, n, mid)
        if k > tem:
            low = mid + 1
        else:
            high = mid
    return high

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        ar = list(map(int, input().split()))
        print(possible_min_time(ar, n, k, 1, max(ar) * k))
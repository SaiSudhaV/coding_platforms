# cook your dish here
from itertools import combinations as comb

def minimum_time(arr, n):
    temp = []
    count = 0
    min_time = -1
    result = [_ for i in range(1, 3) for _ in comb(arr, i) if sum(_) == ]
    return min_time

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(minimum_time(arr, n))

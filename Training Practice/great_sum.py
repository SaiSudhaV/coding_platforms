# 10 Given a special set of numbers and a special sum. Find all those combinations from the given set, equaling the given sum.

from itertools import combinations as comb

def gen_combinations(ar, n, k):
    res = [i for i in comb(ar, 4) if sum(i) == k]
    return len(res)

if __name__ == "__main__":
    ar = list(map(int, input().split()))
    k = int(input())
    print(gen_combinations(ar, len(ar), k))
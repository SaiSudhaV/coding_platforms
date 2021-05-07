# 5 For a given list of numbers, find its factors and add the factors. Then if the sum of factors is present in the original list, sort it and print it else print -1.

from math import sqrt

def factors(n):
    return [i for i in range(2, int(sqrt(n)) + 1)] + [1, n]

def factor_sum(ar):
    res = [i for i in ar if sum(factors(i)) in ar]
    return sorted(res) if res else -1

if __name__ == "__main__":
    n = int(input())
    ar = list(map(int, input().split()))
    print(factor_sum(ar))
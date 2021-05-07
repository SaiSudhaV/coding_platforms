# 7 Even Odd Series. Given a string and it contains the digits as well as non-digits. We have to find the largest even number
# from available digits after removing the duplicates. If not possible, print -1.

from itertools import permutations as perm

def even_no(ar):
    return ["".join(str(j) for j in i) for i in list(perm(ar))]

def odd_series(s, n):
    ar = [int(i) for i in s if i.isdigit()]
    res = max(even_no(set(ar)))
    return res if res else -1

if __name__ == "__main__":
    s = input()
    print(odd_series(s, n))
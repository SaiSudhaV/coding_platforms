# 4 Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.
from collections import Counter as count

def two_pair_sum(ar, k):
    res, tem = [], count(ar)
    for i in ar:
        p = k - i 
        if (i != p and tem[p]) or (i == p and tem[p] > 1): 
            res.append(i)
            res.append(p)
            tem.subtract((i, p))    
    return [ar.index(i) for i in res] if res else "No pair Exists"

if __name__ == "__main__":
    n, k = map(int, input().split())
    ar = list(map(int, input().split()))
    print(two_pair_sum(ar, k))
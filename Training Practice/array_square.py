# 3 Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

def squares(ar):
    return sorted([i ** 2 for i in ar])

if __name__ == "__main__":
    n = int(input())
    ar = list(map(int, input().split()))
    print(squares(ar))
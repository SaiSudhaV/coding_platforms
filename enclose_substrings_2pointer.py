from math import inf

def countArray(A):
    tem = [i for i in "abcdefghijklmnopqrstuvwxyz"]
    return [A.count(i) for i in tem]

def isValid(A, B):
    for i in range(26):
        if A < B:
            return False
    return True

def enclosing_substrings(A, n, B, m):
    count_A, count_B = countArray(A), countArray(B)
    ptr1, ptr2, res = 0, m - 1, inf
    while ptr2 < n and ptr1 < n:
        if isValid(count_A, count_B):
            count_A[ord(A[ptr1]) - ord('a')] -= 1
            res = min(ptr2 - ptr1 + 1, res)
            ptr1 += 1
        else:
            ptr2 += 1
            count_A[ord(A[ptr2]) - ord('a')] += 1
    return res if res != inf else -1
    
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        A, B = input().split()
        print(enclosing_substrings(B, len(B), A, len(A)))
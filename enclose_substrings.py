from math import inf

def enclosing_substrings(A, n, B, m):
    ptr, idx, tem, count, tem1, tem2 = 0, -1, inf, 0, [0] * 256, [0] * 256
    if n < m:
        return -1
    for i in range(m):
        tem1[ord(B[i])] += 1
    for i in range(n):
        tem2[ord(A[i])] += 1
        if tem2[ord(A[i])] <= tem1[ord(A[i])]:
            count += 1
        if m == count:
            while (tem1[ord(A[ptr])] < tem2[ord(A[ptr])] or tem1[ord(A[ptr])] == 0):
                if (tem1[ord(A[ptr])] < tem2[ord(A[ptr])]):
                    tem2[ord(A[ptr])] -= 1
                ptr += 1
            res = i - ptr + 1
            if res < tem:
                tem, idx = res, ptr
    return -1 if idx == -1 else tem
    
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        A, B = input().split()
        print(enclosing_substrings(B, len(B), A, len(A)))
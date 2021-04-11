def subsequence(A, B):
    ptr1, ptr2, n, m = 0, 0, len(A), len(B)
    if m == 0:
        return "No"
    if n == 0:
        return "Yes"
    while ptr1 < m:
        if B[ptr1] == A[ptr2]:
            ptr2 += 1
            if ptr2 == n:
                return "Yes"
        ptr1 += 1
    return "No"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        A, B = input().split()
        print(subsequence(A, B))

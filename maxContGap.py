def maximumGap(self, A):
    A, res, size = list(A), 0, len(A)
    A.sort()
    for i in range(size - 1):
        if(A[i + 1] - A[i] > res):
            res = A[i + 1] - A[i]
    return res
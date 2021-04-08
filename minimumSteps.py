def coverPoints(A, B):
    res, size = 0, len(A)
    for i in range(size - 1):
        res += max(abs(A[i + 1] - A[i]),abs(B[i + 1] - B[i]))
    return abs(res)
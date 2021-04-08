def maxSubArray(A):
    largest, temp, size = A[0], A[0], len(A)
    for i in range(1, size):
        temp  = max(A[i], temp + A[i])
        largest = max(largest, temp)
    return largest
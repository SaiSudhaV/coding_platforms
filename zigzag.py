def convert(A, B):
    n, tem, flag, i, j = len(A), [""] * B, True, 0, 0
    if n == 1 or B == 1:
        return A
    while i < n:
        k = 1
        if flag:
            k, flag = 0, False
        j += k
        while B > j and i < n:
            tem[j] += A[i]
            i, j = i + 1, j + 1
        j -= 2
        while i < n and j >= 0:
            tem[j] += A[i]
            i, j = i + 1, j - 1
        j += 1
    return "".join(i for i in tem)
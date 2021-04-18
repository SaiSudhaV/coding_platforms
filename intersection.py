class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        res, i, j, n, m = [], 0, 0, len(A), len(B)
        while i < n and j < m:
            if A[i] < B[j]:
                i += 1
            elif A[i] > B[j]:
                j += 1
            elif A[i] == B[j]:
                res.append(A[i])
                i, j = i + 1, j + 1
        return sorted(res)
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        n, ptr, i = len(A), 0, 0
        if n == 1 and A[0] == B:
            return 0
        for i in range(n):
            if A[i] == B:
                A[ptr], A[i] = A[i], A[ptr]
            else:
                A[ptr], A[i] = A[i], A[ptr]
                ptr += 1
            i += 1
        for i in range(n - 1, -1, -1):
            if A[i] != B:
                break
        return i + 1

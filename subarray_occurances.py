class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        n, i = len(A), 0
        if B not in A and C not in A:
            return (n * (n + 1)) // 2
        while i < n:
            A[i] = -1 if A[i] == C else 1 if A[i] == B else 0
            i+=1
        i, j, res = 0, 0, 0
        for i in range(n):
            k = 0
            for j in range(i, n):
                k += A[j]
                if k == 0:
                    res += 1
        return res
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n, tem, res, p = len(A), {}, 0, 0
        if n == 0:
            return 0
        if n == 1:
            return 1 if A[0] == B else 0
        tem[0] = 1
        for i in range(n):
            p ^= A[i]
            if p not in tem:
                tem[p] = 0
            if p ^ B in tem:
                res += tem[p ^ B]
            tem[p] += 1
        return res
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n, temp, res, p = len(A),dict(), -1, 10000000000000
        for i in range(n):
            if A[i] not in temp:
                temp[A[i]]=i
            else:
                if temp[A[i]] < p:
                    p = temp[A[i]]
                    res = A[i]
        return res
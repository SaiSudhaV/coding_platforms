class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        tem, res = dict(), []
        for i in A:
            p = i ^ B
            if p in tem:
               res.append(1)
            tem[i] = 1
        return sum(res)
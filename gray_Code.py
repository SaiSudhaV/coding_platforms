class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        if A == 1:
            return [0,1]
        else:
            A = A - 1
            res = self.grayCode(A)
            tem = res[::-1]
            return res + [i + 2 ** A for i in tem]
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def solve(self, A, tem, p, res):
        varlist, n = list(tem), len(A)
        res.append(varlist)
        for i in range(p, n):
            if i > p and A[i] == A[i - 1]:
                continue
            else:
                tem.append(A[i])
                self.solve(A, tem, i + 1, res)
                tem.pop()
        return
    
    def subsetsWithDup(self, A):
        res = []
        self.solve(sorted(A), [], 0, res)
        return res

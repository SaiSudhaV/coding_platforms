class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    
    def gen_comb(self, A, B, tem, res, pos, ptr):
        if tem == B:
            res.add(tuple(ptr[:]))
        elif tem > B:
            return
        for i in range (pos, len(A)):
            tem += A[i]
            ptr.append(A[i])
            self.gen_comb(A, B, tem, res, i + 1, ptr)
            tem -= ptr[-1]
            ptr.pop(-1)
    
    def combinationSum(self, A, B):
        res = set()
        self.gen_comb(sorted(A), B, 0, res, 0, [])
        return list(res)
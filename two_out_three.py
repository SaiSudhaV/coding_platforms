class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        t1, t2, t3 = set(A) & set(B), set(B) & set(C), set(A) & set(C)
        res = list(t1 | t2 | t3)
        return sorted(res)
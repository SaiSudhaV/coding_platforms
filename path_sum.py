
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        if A == None:
            return 0
        if A.left == None and A.right == None:
            if A.val != B:
                return 0
            return 1
        res = self.hasPathSum(A.right, B - A.val) or self.hasPathSum(A.left, B - A.val)
        return res
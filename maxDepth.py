# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxDepth(self, A):
        if A:
            left_depth, right_depth = self.maxDepth(A.left), self.maxDepth(A.right)
            if left_depth > right_depth:
                return left_depth + 1
            else:
                return right_depth + 1
        return 0
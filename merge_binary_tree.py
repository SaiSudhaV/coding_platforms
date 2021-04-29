# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 
class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return the root node in the tree
    def solve(self, A, B):
        if A == None and B == None:
            return None
        if A == None:
            return B
        if B == None:
            return A
        res = TreeNode(A.val + B.val)
        res.left = self.solve(A.left, B.left)
        res.right = self.solve(A.right, B.right)
        return res
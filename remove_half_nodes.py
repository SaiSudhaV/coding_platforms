# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def solve(self, A):
        if A:
            if A.right != None and A.left == None:
                return self.solve(A.right)
            elif A.left != None and A.right == None:
                return self.solve(A.left)
            A.left, A.right = self.solve(A.left), self.solve(A.right)
        return A
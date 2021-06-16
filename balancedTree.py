# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        if not A:
            return 1
        return 1 if abs(height(A.left) - height(A.right)) <= 1 and self.isBalanced(A.left) and self.isBalanced(A.right) else 0

def height(A):
    if not A:
        return -1
    return 1 + max(height(A.right), height(A.left))
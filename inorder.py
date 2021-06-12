# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):
        if A:
            root, high_index = TreeNode(max(A)), A.index(max(A))
            root.left, root.right = self.buildTree(A[:high_index]), self.buildTree(A[high_index + 1:])
            return root
        return None
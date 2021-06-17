# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    
    def isSymmetric(self, A):
        leftRoot, rightRoot = A.left, A.right
        def validSymmetry(leftRoot, rightRoot):
            if leftRoot == None and rightRoot == None:
                return 1
            tem1 = leftRoot.val if leftRoot != None else -1
            tem2  = rightRoot.val if rightRoot != None else -1
            if tem1 != tem2:
                return 0
            return min(validSymmetry(leftRoot.left, rightRoot.right), validSymmetry(leftRoot.right, rightRoot.left))
        return validSymmetry(A.left, A.right)
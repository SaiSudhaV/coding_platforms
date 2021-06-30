# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def getSuccessor(self, A, B):
        res = None
        if not A:
            return A
        tem = A
        while True:
            if tem.val > B:
                res, tem = tem, tem.left
            if not tem:
                break
            if tem.val <= B:
                tem = tem.right
            if not tem:
                break
        return res
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def pathSum(self, A, B):
        res = []
        findPath([], 0, A, B, res)
        return res
        
def findPath(tem, sum_val, A, B, res):
    if not A:
        return 
    if A.right is None and A.left is None:
        if sum_val + A.val == B:
            res.append(tem + [A.val])
            return
        else:
            return
    findPath(tem + [A.val], sum_val + A.val, A.left, B, res)
    findPath(tem + [A.val], sum_val + A.val, A.right, B, res)
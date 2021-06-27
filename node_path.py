# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        res = []
        if find_path(A, B, res):
            return res
        return res

def find_path(A, B, res):
    if A == None:
        return False
    res.append(A.val)
    if A.val == B:
        return True
    if find_path(A.left, B, res):
        return res
    if find_path(A.right, B, res):
        return res
    res.pop()
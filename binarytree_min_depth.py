# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

from math import inf

class Solution:
	# @param A : root node of tree
	# @return an integer
	def minDepth(self, A):
	    res1, res2 = float(inf), float(inf)
        if (not A) or (not A.right and not A.left):
            return 1
        if A.right:
            res1 = self.minDepth(A.right)
        if A.left:
            res2 = self.minDepth(A.left)
        return min(res1, res2) + 1
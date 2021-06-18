# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : root node of tree
	# @return an integer
	def isSameTree(self, A, B):
	    return 1 if traversal(A, "") == traversal(B, "") else  0

def traversal(A, res):
    if A != None:
        res = traversal(A.left, res)
        res += str(A.val)
        res = traversal(A.right, res)
    return res
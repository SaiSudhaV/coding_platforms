# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
	def kthsmallest(self, A, B):
	    res = []
	    inorder(A, res)
	    return res[B - 1]
	    
def inorder(A : TreeNode, res : [int]) -> None:
    if not A:
        return
    inorder(A.left, res)
    res.append(A.val)
    inorder(A.right, res)
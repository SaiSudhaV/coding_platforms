# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        head = []
        node(A, head)
        for i in range(1, len(head)):
            head[i - 1].right = head[i]
            head[i - 1].left = None
        return A

def node(A, head):
    head.append(A)
    if A.left:
        node(A.left, head)
    if A.right:
        node(A.right, head)
    return head
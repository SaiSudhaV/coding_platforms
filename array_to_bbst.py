class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def subtree(self, A, root, n):
        if not A:
            return root
        mid = n // 2
        if not root:
            root = TreeNode(A[mid])
        left_subtree = right_subtree = None
        root.left = self.subtree(A[0 : mid], left_subtree, len(A[0 : mid]))
        root.right = self.subtree(A[mid + 1 :], right_subtree, len(A[mid + 1 :]))
        return root

    def sortedArrayToBST(self, A):
        n = len(A)
        if not A:
            return None
        root = TreeNode(A[n // 2])
        head = root
        self.subtree(A, root, n)
        return head
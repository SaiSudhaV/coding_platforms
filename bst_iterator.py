# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.arr = []
        push(self.arr, root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return True if self.arr else False

    # @return an integer, the next smallest number
    def next(self):
        res = self.arr.pop()
        push(self.arr, res.right)
        return res.val

def push(arr, A):
    while A:
        arr.append(A)
        A = A.left

# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),

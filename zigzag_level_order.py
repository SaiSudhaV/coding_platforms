# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        if not A:
            return []
        res, x = [], [[A,1]]
        while len(x) > 0:
            p, q = [], []
            while len(x)>0:
                ar = x.pop(0)
                tem1, tem2 = ar[0], ar[1]
                p.append(tem1.val)
                if tem1.left:
                    q.append([tem1.left, tem2 + 1])
                if tem1.right:
                    q.append([tem1.right, tem2 + 1])
            p, x = p[::-1] if tem2 % 2 == 0 else p, q
            res.append(p)
        return res
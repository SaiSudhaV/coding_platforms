# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import deque

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        res = deque([A])
        flag = False
        while flag == False and res:
            for i in range(len(res)):
                tem = res.popleft()
                if not (tem.left and tem.left.val == B or tem.right and tem.right.val == B):
                    if tem.left:
                        res.append(tem.left)
                    if tem.right:
                        res.append(tem.right)
                else:
                    flag = True
        res = [i.val for i in res]
        return res
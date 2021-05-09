# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def verticalOrderTraversal(self, A):
        tem = {}
        my_dict, res, p = calc(A, tem, 0, 0), [], []
        for i in sorted(tem):
            tem[i] = sorted(tem[i], key = lambda k : k[0])
            st = []
            for j in tem[i]:
                st.append(j[1])
            res.append(st)
        return res
    
def calc(root, res, k, n):
    if not root:
        return res
    if k not in res:
        res[k] = [[n, root.val]]
    else:
        res[k].append([n, root.val])
    res = calc(root.left, res, k - 1, n + 1)
    res = calc(root.right, res, k + 1, n + 1)
    return res
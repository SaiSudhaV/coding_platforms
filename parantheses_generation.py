class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):
        res = []
        combinations(A, 0, '', res)
        return res

def combinations(n, tem, s, res):
    if len(s) == 2 * n:
        res.append(s)
        return
    if tem != n:
        combinations(n, tem + 1, s + '(', res)
    if len(s) < 2 * tem:
        combinations(n, tem, s + ')', res)
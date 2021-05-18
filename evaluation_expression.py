class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        res, opr = [], ['+', '-', '*', '/']
        for i in A:
            if i not in opr:
                res.append(i)
            elif len(res) >= 2:
                tem1 = str(res.pop())
                tem2 = str(res.pop())
                p = int(eval(tem2 + i + tem1))
                res.append(p)
        return res.pop()
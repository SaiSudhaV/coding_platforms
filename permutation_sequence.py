from math import factorial as fact

class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def getPermutation(self, A, B):
        tem, res = [i for i in range(1, A + 1)], ""
        while tem:
            n = len(tem)
            i = B // fact(n - 1)
            if (B % fact(n - 1) == 0):
                i -= 1
            res += str(tem[i])
            B -= fact(n - 1) * i
            tem.remove(tem[i])
        return(res)
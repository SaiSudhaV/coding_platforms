import math
 
class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):
        res = []
        idx = 0
        while idx < len(A) :
            tem = ''
            x = 0
            if len(A[idx]) < B :
                tem = A[idx]
                i = idx + 1
                while i < len(A):
                    if len(tem) + 1 + len(A[i]) > B :
                        break
                    tem += ' ' + A[i]
                    x, i = x + 1, i + 1
                idx = i
            elif len(A[idx]) == B :
                tem = A[idx]
            tem = tem.split() 
            s = 0
            for j in range(len(tem)):
                s += len(tem[j])
            p = B - s
            if len(tem) > 0:
                tem2 = tem[0]
            k = 1
            while x > 0:
                if p / x > p // x:
                    tem2 += ' '*(p // x + 1) + tem[k]
                    k, p, x = k + 1, p - p // x - 1, x - 1
                elif p / x == p // x :
                    tem2 += ' ' * (p // x) + tem[k]
                    k, p, x = k + 1, p - p // x, x - 1
            res.append(tem2.ljust(B,' '))
        if len(res) > 0:
            res[-1] = ' '.join(res[-1].split())
            res[-1] = res[-1].ljust(B,' ')
        
        return res    
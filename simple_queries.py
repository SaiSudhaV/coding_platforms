from bisect import bisect_left as bl
 
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
 
    def countArray(self, A, n):
        left, right, top, tem = [1] * n, [1] * n, -1, []
        for i in range(n):
            while top >= 0 and A[tem[top]] <= A[i]:
                top -= 1
                tem.pop()
            if top >= 0:
                left[i] = i - tem[top]
            else:
                left[i] = i + 1
            tem.append(i)
            top += 1
        tem, top = [], -1
        for i in range(n - 1, -1, -1):
            while top >= 0 and A[tem[top]] < A[i]:
                tem.pop()
                top -= 1
            if top >= 0:
                right[i] = tem[top] - i
            else:
                right[i] = n - i
            tem.append(i)
            top += 1
        for i in range(n):
            left[i] *= right[i]
        return left
        
    def calculate(self, A):
        tem, res = 2, 1
        for i in range(2, int(A ** 0.5)+1):
            if A % i == 0:
                if A // i != i:
                    tem += 1
                tem += 1
        for i in range(tem // 2):
            res = (res * A) % 1000000007
        if tem % 2:
            res = (res * (A ** 0.5)) % 1000000007
        return int(res)
    
    def solve(self, A, B):
        n = len(A)
        counts, res, tem = self.countArray(A, n), [], []
        for i in range(n):
            tem.append(self.calculate(A[i]))
        tem = sorted(list(zip(tem, counts)), reverse = True)
        ptr, p = [], 0
        for i in range(n):
            p += tem[i][1]
            ptr.append(p)
        res = []
        for i in B:
            res.append(tem[bl(ptr, i)][0])
        return res
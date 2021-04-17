from bisect import bisect_left
from math import sqrt as sq
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        frequencies = self.getFrequency(A)
        n, proA = len(A), []
        for i in range(n):
            proA.append(self.divisorProduct(A[i]))
        fA = list(zip(proA, frequencies))
        fA.sort(reverse = True)
        V, accumulated = [], 0
        for i in range(n):
            accumulated += fA[i][1]
            V.append(accumulated)
        res = []
        for i in B:
            res.append(fA[bisect_left(V, i)][0])
        #query 5
        return res

    def getFrequency(self, A):
        n = len(A)
        L, R = [1] * n, [1] * n
        S, top = [], -1
        for i in range(n):
            while(top >= 0 and A[S[top]] <= A[i]):
                S.pop()
                top -= 1
            if (top >= 0):
                L[i] = i - S[top]
            else:
                L[i] = i + 1
            S.append(i)
            top += 1
        S = []
        top = -1
        for i in range(n-1, -1, -1):
            while(top >= 0 and A[S[top]] < A[i]):
                S.pop()
                top -= 1
            if (top >= 0):
                R[i] = S[top] - i
            else:
                R[i] = n - i
            S.append(i)
            top += 1
        for i in range(n):
            L[i] *= R[i]
        return L
        
    def divisorProduct(self, A):
        div, res = 2, 1
        for i in range(2, int(sq(A))  + 1):
            if A % i == 0:
                if A // i != i:
                    div += 1
                div += 1
        for _ in range(div // 2):
            res *= A
            res %= (10 ** 9 + 7)
        if div % 2 != 0:
            res *= sq(A)
            res %= (10 ** 9 + 7)
        return int(res)
from heapq import heappop, heappush

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        A, B = sorted(A), sorted(B)
        tem, p, res = set(), list(), list()
        n, m = len(A) - 1, len(A) - 1
        tem.add((n, m))
        k = A[n] + A[m]
        p.append((-k, (n, m)))
        for i in range(C):
            sum, (n, m) = heappop(p)
            res.append(-sum)
            for i, j in [(n - 1, m), (n, m - 1)]:
                if i >= 0 and j >= 0 and (i, j) not in tem:
                    heappush(p, (-(A[i] + A[j]), (i, j)))
                    tem.add((i, j))
        return res
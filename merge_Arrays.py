from heapq import heappop, heappush

class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        n, tem, res = len(A[0]), [], []
        for i in range(len(A)):
            heappush(tem, (A[i][0], i, 0))
        while tem != []:
            top = heappop(tem)
            res.append(top[0])
            if top[2] == n - 1:
                continue
            heappush(tem, (A[top[1]][top[2] + 1], top[1], top[2] + 1))
        return res
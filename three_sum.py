class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        i, n, res = 0, len(A), A[0] + A[1] + A[2]
        A.sort()
        for i in range(n - 2):
            p1, p2 = i + 1, n - 1
            while p1 < p2:
                if abs(res - B) > abs(A[i] + A[p1] + A[p2] - B):
                    res = A[i] + A[p1] + A[p2]
                if A[i] + A[p1] + A[p2] < B:
                    p1 += 1
                elif A[i] + A[p1] + A[p2] > B:
                    p2 -= 1
                else:
                    return B
        return res
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        left, right, res = [A[0]], [A[len(A) - 1]], 0
        for i in range(len(A) - 2, -1, -1):
            right.append(max(right[ - 1], A[i]))
        for i in range(1, len(A)):
            left.append(max(left[i - 1] , A[i]))
        right = right[::-1]
        for i in range(len(A)):
            res += min(right[i], left[i]) - A[i]
        return res
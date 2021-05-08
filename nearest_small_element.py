class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        n = len(A)
        res, stack = [-1] * n, [A[0]]
        for i in range(1, n):
            while len(stack) > 0:
                top = stack[-1]
                if A[i] <= top:
                    stack.pop()
                else:
                    res[i] = top
                    break
            stack.append(A[i])
        return res
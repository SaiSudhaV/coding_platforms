class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
        A, n, res = sorted(list(A)), len(A), {}
        for i in range(n):
            if A[i] not in res:
                res[A[i] + B] = i
            else:
                return 1
        return 0
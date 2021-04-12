class Solution:
    # @param A : string
    # @return an integer
    def is_palindrome(self, A, m, n):
        while m < n:
            if A[m] != A[n]:
                return False
            m, n = m + 1, n - 1
        return True
    
    def solve(self, A):
        n = len(A)
        low, high, res = 0, n - 1, 0
        while low < high:
            if A[low] == A[high]:
                if self.is_palindrome(A, low, high):
                    return res
            res, low = res + 1, low + 1
        return res
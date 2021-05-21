class Solution:
    # @param A : string
    # @return a list of list of strings
    
    def is_palindrome(self, A):
        return A == A[::-1]
    
    def sol(self, A, res, k):
        if not A:
            res.append(k)
            return res
        for i in range(1, len(A) + 1):
            if self.is_palindrome(A[ : i]):
                self.sol(A[i :], res, k + [A[ : i]])
        return res
    
    def partition(self, A):
        return self.sol(A, [], [])
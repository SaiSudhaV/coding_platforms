class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n, k, flag = len(A), 0, False
        for i in range(1, n):
            if A[i] == A[k] and flag == True: 
                continue
            elif A[i] == A[k] and not flag:
                A[k + 1], flag, k = A[i], True, k + 1
            else:
                A[k + 1], k, flag = A[i], k + 1, False
        return len(A[:k + 1])
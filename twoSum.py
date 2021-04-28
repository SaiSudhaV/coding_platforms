from collections import defaultdict as def_dic

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        res, n = def_dic(int), len(A)
        for i in range(n):
            tem = B - A[i]
            if res[tem] != 0:
                return [res[tem], i + 1]
            elif res[A[i]] == 0:
                res[A[i]] = i + 1
        return []
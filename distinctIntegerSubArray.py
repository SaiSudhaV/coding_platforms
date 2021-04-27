from collections import Counter
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n, res, count, temp = len(A), 0, 0, 0
        countArray, j = Counter(A), 0
        for i in range(n):
            if countArray[A[i]] == 1:
                countArray[A[i]] += 1
                count += 1
            if count > B:
                j += 1
                countArray[A[j]] -= 1
                count -= 1
                temp = 0
            while countArray[A[j]] > 1:
                temp += 1
                j += 1
                countArray[A[j]] -= 1
            if count == B:
                res += temp + 1
        return res
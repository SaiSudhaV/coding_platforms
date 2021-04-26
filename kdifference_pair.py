from collections import Counter as count

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        res, counterList = [], count(A)
        for i in A:
            temp = B + i
            if (i != temp and counterList[temp]) or (i == temp and counterList[temp] > 1):
                res.append((i, temp))
                counterList.subtract((i, temp))
        return 1 if res else 0
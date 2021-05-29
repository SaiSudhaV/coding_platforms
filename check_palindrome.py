from collections import Counter as count

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        tem, flag = count(A).values(), False
        for i in tem:
            if (i % 2) and flag:
                return 0
            elif i % 2:
                flag = True
        return 1
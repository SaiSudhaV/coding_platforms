class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        n, A = A.__len__(), sorted(A)
        if n < 3:
            return []
        res = set()
        for i in range(n - 1):
            j, k = i + 1, n - 1
            while j < k:
                tem = (A[i], A[j], A[k])
                cur_sum = A[i] + A[j] + A[k]
                if cur_sum < 0:
                    j += 1
                elif cur_sum == 0:
                    res.add(tem)
                    j += 1
                else:
                    k -= 1
        return list(res)
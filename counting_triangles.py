class Solution:
# @param A : list of integers
# @return an integer
    def nTriang(self, A):
        A.sort()
        res, n = [], len(A)
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while k > j:
                if A[j] + A[k] > A[k]:
                    res.append(k - j)
                    k -= 1
                else:
                    j += 1
        return sum(res) % 1000000007
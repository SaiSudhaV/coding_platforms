class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        res = []
        A.sort()
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                low, high = j + 1, len(A) - 1
                while low < high:
                    x = A[i] + A[j] + A[low] + A[high]
                    if x == B:
                        res.append((A[i], A[j], A[low], A[high]))
                        high, low = high - 1, low + 1
                    elif x > B:
                        high -= 1
                    else:
                        low += 1
        res = set(res)
        return sorted(res)
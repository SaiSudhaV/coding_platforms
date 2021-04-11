class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        roman_int_pairs = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        res, i, n, valid = 0, 0, len(A), True
        i = 0
        while i < n - 1:
            if roman_int_pairs[A[i]] < roman_int_pairs[A[i + 1]]:
                res -= roman_int_pairs[A[i]] - roman_int_pairs[A[i + 1]]
                valid, i = False, i + 2
            else:
                res += roman_int_pairs[A[i]]
                valid, i = True, i + 1
        if i != n:
            return res + roman_int_pairs[A[-1]]
        return res

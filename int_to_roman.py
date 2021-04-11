class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        res, count = "", 1
        tem = [int(i) for i in str(A)]
        n = pos = len(tem)
        for i in range(n - 1, -1,-1):
            res += self.roman_val(tem[i], pos)
            pos -= 1
        return res
 
    def roman_val(self, n, k):
        ones = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        tens = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        hundreds = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        thousands = ['M', 'MM', 'MMM']
        if n == 0:
            return ""
        elif k == 1:
            return ones[n - 1]
        elif k == 2:
            return tens[n - 1]
        elif k == 3:
            return hundreds[n - 1]
        elif k == 4:
            return thousands[n - 1]

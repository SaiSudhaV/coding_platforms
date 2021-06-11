class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : integer
	# @return an integer
	def Mod(self, A, B, C):
        if B == 0:
            return 1 % C
        tem = self.Mod(A, B // 2, C)
        res = ((tem % C) ** 2) % C
        if B & 1:
            res = ((res % C) * (A % C)) % C
        return (res + C) % C
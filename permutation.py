class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def permute(self, A):
        res, n = [], len(A)
        if n != 1:
            for i in A:
                tem = [j for j in A if i != j]
                p = self.permute(tem)
                for j in p:
                    j.append(i)
                res += p
            return res
        return [A]
class Solution:
	# @param A : integer
	# @param B : integer
	# @return a list of list of integers
	
	def check(self, A, B, i, p, res):
        if(len(p) == B):
            res.append(p.copy())
            return
        if i <= A:
            p.append(i)
            self.check(A, B, i + 1, p, res)
            p.pop()
            self.check(A, B,i + 1, p, res)
            return
        return
        
	def combine(self, A, B):
        res, tem = [], []
        self.check(A, B, 1, tem, res)
        return res
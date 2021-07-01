from heapq import heappop, heapify, heappush

class Solution:
	# @param A : integer
	# @param B : list of integers
	# @return an integer
	def nchoc(self, A, B):
        res = 0
        if not B:
            return res
        B = [-x for x in B]
        heapify(B)
        while A > 0:            
            tem = heappop(B)
            res += tem
            heappush(B, -1 * (-1 * tem // 2))
            A -= 1
        return (-1 * res) % (1000000007)
class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
	    A, n = A.strip(), len(A)
        if n == 0:
            return 0
        if A[0] == '-' and not A[1].isdigit() and n > 1:
            return 0
        if A[0 : 2] == '-+' or A[0:2] == '- ':
            return 0
        if A[0] != '-' and not A[0].isdigit():
            if A[0] == '+' and A[1].isdigit() and n > 1:
                pass
            else:
                return 0
        mul, t1, t2 = 1, -1, -1
        for i in range(n):
            if t1 == -1 and A[i].isdigit():
                t1 = i
            elif A[i].isdigit() or A[i] == '.':
                pass
            else:
                if t1 != -1:
                    t2 = i
                    break
        if t2 == -1:
            t2 = n
        if t1 > 0:
            if A[t1 - 1] == '-':
                mul = -1
        if t1 == -1:
            return 0
        res =  int(A[t1 : t2]) 
        if res * mul < -1 * (2 ** 31):
            return -1 * (2 ** 31)
        if res * mul > 2 ** 31 - 1 :
            return (2 ** 31) - 1
        return int(res) * mul
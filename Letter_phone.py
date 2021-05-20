class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        key_pad = {1 : "1", 2 : "abc", 3 : "def", 4 : "ghi", 5 : "jkl", 6 : "mno", 7 : "pqrs", 8 : "tuv", 9 : "wxyz", 0 : "0"}
        res = [s for s in key_pad[int(A[0])]]
        A = A[1:]
        for i in A:
            p, tem = key_pad[int(i)], []
            n = len(p)
            for j in range(n):
                tem += [k + p[j] for k in res]
            res = tem
        return sorted(res)
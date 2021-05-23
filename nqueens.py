class Solution:
    # @param A : integer
    # @return a list of list of strings
        
    def calculate(self, n, res, s, row):
        if row == n:
            ar = []
            for i in range(n):
                tem = ''
                for j in range(n):
                    tem += s[i][j]
                ar.append(tem)
            res.append(ar)
            return
        for i in range(n):
            s[row][i]="Q"
            if self.validity_check(s, row, i):
                self.calculate(n, res, s, row + 1)
            s[row][i]="."
    
    def solveNQueens(self, A):
        ar, res, r = [], [], 0
        for i in range(A):
            s = []
            for j in range(A):
                s.append(".")
            ar.append(s)
        self.calculate(A, res, ar, r)
        return res

    def validity_check(self, s, n, m):
        for i in range(n):
            if(s[i][m]=="Q"):
                return 0
        r, c = n - 1, m - 1
        while r >= 0 and c >= 0:
            if s[r][c] == "Q":
                return 0
            r, c = r - 1, c - 1
        r, c = n - 1, m + 1
        while r >= 0 and c < len(s):
            if s[r][c] == "Q":
                return 0
            r, c = r - 1, c + 1
        return 1
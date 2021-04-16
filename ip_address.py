class Solution:
    # @param A : string
    # @return a list of strings
    def isValid(self, A):
        for i in A.split("."):
            if int(i) > 255:
                return False
        return True
    
    def restoreIpAddresses(self, A):
        res, n = [], len(A)
        if n > 12 or n < 4 or not A.isdigit():
            return res
        else:
            for i in range(1, n - 2):
                if n > i + 9:
                    continue 
                elif i > 3:
                    break
                elif A[0] == '0' and i > 1:
                    break 
                for j in range(i + 1, n - 1):
                    if j > i + 3:
                        break
                    elif A[i] == '0' and j > i + 1:
                        break 
                    elif n - j > 6:
                        continue 
                    for k in range(j + 1, n):
                        if A[j] == '0' and k > j + 1:
                            break 
                        elif A[k] == '0' and (n - k > 1): 
                            continue 
                        elif k > j + 3:
                            break 
                        elif n > k + 3:
                            continue 
                        tem = A[:i] + '.' + A[i:j] + '.' + A[j:k] + '.' + A[k:]
                        if self.isValid(tem):
                            res.append(tem)
        return res
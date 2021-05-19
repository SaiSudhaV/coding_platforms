class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        my_dict, res, n = {}, [], len(A)
        for i in range(n - 1):
            for j in range(i + 1, n):
                p = A[i] + A[j]
                if p not in my_dict:
                    my_dict[p] = [i, j]
                else:
                    tem = []
                    tem.extend(my_dict[p])
                    tem.append(i)
                    tem.append(j)
                    tem1 = set(tem)
                    if len(tem) == len(tem1):
                        res.append(tem)
        return sorted(res)[0]
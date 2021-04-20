class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
        ptr1, ptr2, tem, m, count, n = 0, 0, 0, 0, 0, len(A)
        while ptr2 < n:
            if count > B:
                if A[ptr1] == 0:
                    count -= 1
                ptr1 += 1
            if count <= B:
                if A[ptr2] == 0:
                    count += 1
                ptr2 += 1
            if (ptr2 - ptr1) > m and count <= B:
                m = ptr2 - ptr1 
                tem = ptr1
        res = [i for i in range(tem, tem + m)]
        return res
def maxSpecialProduct(self, A):
    ptr, ptr1, ptr2, tem, tem1, tem2, n = 0, 0, n - 1, 0, 1000000009, A[-1], n
    for i in range(n - 1, -1, -1):
        if A[i - 1] >= tem2:
            ptr2, tem2 = i - 1, A[i - 1]
        else:
            ptr1, tem1 = i - 1, A[i - 1]
            break
    for i in range(ptr1, 0, -1):
        if A[i - 1] > tem1:
            ptr, tem = i - 1, A[i - 1]
            break
        elif A[i - 1] < tem1:
            tem2, ptr2 = tem1, ptr1
        else:
            ptr1, tem1 = i - 1, A[i - 1]
    while tem2 < tem and ptr2 < n - 1 and tem2 < A[ptr2 + 1]:
        tem2, ptr2 = A[ptr2 + 1], ptr2 + 1
    return (ptr * ptr2) % 1000000007
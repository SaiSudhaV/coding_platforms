def largest_subsequence_zero(self, A):
    my_dict, tem, low, high, n = {0:-1}, 0, 0, 0, len(A)
    for i in range(n) :
        tem += A[i]
        if tem in my_dict:
            if i - my_dict[tem] > high - low :
                low, high = my_dict[tem], i 
        else :
            my_dict[tem] = i    
    return A[low + 1 : high + 1]
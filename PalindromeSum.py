def isPalindrome(num):
    return str(num) = str(num)[::-1]

def palindrome_sum(first,last):
    total = 0
    if first < 0 or last < 0:
        return -1
    elif first>last:
        return -2
    else:
        return sum([i for i in range(first,last) if isPalindrome(i)])
   



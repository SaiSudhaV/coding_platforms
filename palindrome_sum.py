def get_reverse(num):
    rev=0
    
    while num!=0:
       r=num%10
       rev=(rev*10)+r
       num=num//10
    return rev
def isPalindrome(num):
    
    if num==get_reverse(num):
        return True
    else:
        return False
def palindrome_sum(first,last):
    sum1=0
    if first<0 or last<0:
        return -1
    elif first>last:
        return -2
    else:
        for i in range(first,last):
            if(isPalindrome(i)):
                sum1=sum1+i
        return sum1

# 11 You are provided with a string of numbers, check whether it is a palindrome or not. If it is not a palindrome, then, reverse the string, add it to the original string 
# and check again. You are required to repeat the process until it becomes palindrome. Find the length of palindromic string.

def is_palindrome(s):
    return s == s[::-1]

def convert_palindrome(s):
    tem = "".join(reversed(list(s)))
    return str(int(s) + int(tem))

def gen_palindrome(s):
    res = s if is_palindrome(s) else convert_palindrome(s)
    return len(res)

if __name__ == "__main__":
    s = input()
    print(gen_palindrome(s))
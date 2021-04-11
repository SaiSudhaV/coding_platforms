def isPalindrome(s):
    return s == s[::-1]
    
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        s = input()
        print("Yes" if isPalindrome(s) else "No")

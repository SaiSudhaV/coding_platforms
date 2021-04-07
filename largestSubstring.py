def longestPalindrome(A):
    i = max_len = 0
    palindrome, l = None, len(A)
    while i < l:
        ch, m = A[i], i
        while i + 1 < l and ch == A[i + 1]:
            i += 1
        n = i
        while m - 1 >= 0 and n + 1 < l and A[m - 1] == A[n + 1]:
            m -= 1
            n += 1
        p = n - m + 1
        if p > max_len:
            max_len = p
            palindrome = A[m : n + 1]
        i += 1
    return palindrome

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        s = input()
        print(len(longestPalindrome(s)))
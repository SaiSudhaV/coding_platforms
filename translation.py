def reverseString(s, t):
    if s == t[::-1]:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    s = str(input())
    t = str(input())
    res = reverseString(s, t)
    print(res)
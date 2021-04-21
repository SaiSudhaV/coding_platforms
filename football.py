def footBall(s):
    count = 0
    for i in range(len(s) - 6):
        if s[i] == s[i + 1] == s[i + 2] == s[i + 3] == s[i + 4] == s[i + 5] == s[i + 6] == "0" or s[i] == s[i + 1] == s[i + 2] == s[i + 3] == s[i + 4] == s[i + 5] == s[i + 6] == "1" :
            count = 7
            break
        
    return "YES" if count == 7 else "NO"

if __name__ == "__main__" :
    s = input()
    print(footBall(s))

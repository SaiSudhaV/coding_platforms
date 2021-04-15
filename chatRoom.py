def chatRoom(s):
    t = "hello"
    res, j = 0 , 0
    for i in range(len(s)):
        if s[i] == t[j]:
            j += 1
            res += 1
            
            if res == 5:
                break
    return "YES" if res == 5 else "NO"
 
if __name__ == '__main__':
    s = input()
    print(chatRoom(s))

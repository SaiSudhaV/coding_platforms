# cook your dish here

def canForm(s, n):
    ctr = 0
    if s.count("1") > 0:
        for i in range(s.index('1'), n):
            if s[i] == '1':
                ctr += 1
            else:
                break
        return "YES" if ctr == s.count('1') else "NO"
    return "NO"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = input()
        print(canForm(s, len(s)))
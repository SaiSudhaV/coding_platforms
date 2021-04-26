
def matchStrings(s1, s2):
    for i in range(len(s1)):
        if (s1[i].isalpha() and s2[i].isalpha()) and s1[i] != s2[i]:
            return "No"
    return "Yes"

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s1 = input()
        s2 = input()
        print("No" if len(s1) != len(s2) else matchStrings(s1, s2))

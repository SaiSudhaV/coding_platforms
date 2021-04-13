#your code goes here

def missing_digits(s):
    if "machula" in s[0]:
        res = [str(int(s[4]) - int(s[2])), s[2], s[4]]
    elif "machula" in s[2]:
        res = [s[0], str(int(s[4]) - int(s[0])), s[4]]
    else:
        res = [s[0], s[2], str(int(s[0]) + int(s[2]))]
    return res[0], res[1], res[2]

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        input()
        s = input().split()
        a, b, c = missing_digits(s)
        print("%s + %s = %s" % (a, b, c))
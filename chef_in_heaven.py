# cook your dish here

def check_possibility(s, n):
    count, n = 0, len(s)
    if n == 1 and s == "1":
        return "YES"
    for i in range(0, n - 1, 2):
        tem = s[i : i + 2]
        if tem[0] == tem[1] == '1':
            count += 2
        if tem[0] != tem[1]:
            count += 1 
        if (i + 2) // 2 <= count:
            return "YES"
    return "NO"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        s = input()
        print(check_possibility(s, n))
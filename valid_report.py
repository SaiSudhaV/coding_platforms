# cook your dish here

def valid_report(s, n):
    tem, flag = None, True
    for i in s:
        if i == 'T':
            if tem != 'H':
                flag = False
                break
            else:
                tem = None
        elif i == "H":
            if tem:
                flag = False
                break
            else:
                tem = "H"
    return "Valid" if flag and not tem else "Invalid"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        s = input()
        print(valid_report(s, n))
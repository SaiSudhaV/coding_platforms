def hqn(s):
    lst = [i for  i in s if i in "HQ9"]
    return "YES" if len(lst) > 0 else "NO"
    
if __name__ == '__main__':
    s = str(input())
    print(hqn(s))
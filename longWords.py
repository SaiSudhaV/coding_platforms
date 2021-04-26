def longWords(s):
    lst = [i for i in s]
    length = len(s)
    if length > 10:
        lst1 = [lst[0], str(length - 2), lst[length - 1]]
        return "".join([i for i in lst1])
    else:
        return s

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        s = str(input())
        res = longWords(s)
        print(res)
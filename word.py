def word(n):
    lst = [i for i in n]
    lowerCase, upperCase, lst1 = 0, 0, []
    for i in lst:
        if 97 <= ord(i) <= 122:
            lowerCase += 1
        elif 65 <= ord(i) <= 90:
            upperCase += 1
            if upperCase > lowerCase:
                for i in lst:
                    if 97 <= ord(i) <= 122:
                        lst1.append(chr(ord(i) - 32))
                    else:
                        lst1.append(i)
        else:
            return n.casefold()
    return "".join([str(i) for i in lst1])

if __name__ == "__main__":
    n = str(input())
    res = word(n)
    print(res)

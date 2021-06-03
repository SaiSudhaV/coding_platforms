if __name__ == '__main__':
    N = int(input())
    ar = []
    for i in range(N):
        s = input().split()
        if s[0] == "insert":
            ar.insert(int(s[1]), int(s[2]))
        if s[0] == "remove" and int(s[1]) in ar:
            ar.remove(int(s[1]))
        if s[0] == "pop" and ar != []:
            ar.pop()
        if s[0] == "sort":
            ar.sort()
        if s[0] == "append":
            ar.append(int(s[1]))
        if s[0] == "reverse":
            ar.reverse()
        if s[0] == "print":
            print(ar)
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        res = []
        for j in range(n):
            i = int(input())
            if i in res:
                res.remove(i)
            else:
                res.append(i)
        print(res[0])
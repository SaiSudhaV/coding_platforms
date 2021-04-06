def findPerm(A, B):
    temp, res = [i for i in range(1, B + 1)], []
    for i in A:
        if i == 'I':
            res.append(temp.pop(0))
        else:
            res.append(temp.pop(-1))
    res.append(temp[0])
    return res
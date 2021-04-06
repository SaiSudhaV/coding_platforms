def colorful(self, A):
    tempList, hashSet, s = [], {}, str(A)
    for i in range(len(s)):
        for j in range(i, len(s)):
            tempList.append(s[i : j + 1])
    for i in range(len(tempList)):
        maxi = 1
        ptr = tempList[i]
        for j in range(len(ptr)):
            maxi *= int(ptr[j])
        hashSet[ptr] = maxi
    temp = []
    for k, v in hashSet.items():
        if v not in temp:
            temp.append(v)
    return 1 if len(temp) == len(tempList) else 0
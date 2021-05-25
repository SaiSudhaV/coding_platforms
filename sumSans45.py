l1 = list(map(int, input().strip().split(',')))
def is_check(l1):
    i = 0
    add = 0
    if len(l1) == 0:
        return 0
    else:
        for i in range(i, len(l1)):
            if l1[i] == 4 or l1[i] == 5:
                add += 0
            else:
                if l1[i] > 5:
                    add += 0
                else:
                    add += l1[i]
        return add
print(is_check(l1))

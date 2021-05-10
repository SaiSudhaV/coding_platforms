evenlastlist = [int(i) for i in input().split(',')]
k = len(evenlastlist)
def evenlast(evenlastlist):
    add = 0
    for i in range(k):   
        if i % 2 == 0:
            add += evenlastlist[i]
    res = add * evenlastlist[k - 1]
    return res
print(evenlast(evenlastlist))

l1 = list(map(int, input().strip().split(',')))
a = 0
while a < len(l1) - 1:
    if l1[a] > l1[a + 1]:
        print(a)
    a += 1

list1 = [int(i) for i in input()]
count = 0
for i in range(0, len(list1)):
    if (list1[i] == 1):
        count = count + 1
if (count % 2 == 0):
    list1.append(0)
else:
    list1.append(1)
for i in list1:
    print(i, end="")

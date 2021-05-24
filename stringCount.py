list1 = [str(i) for i in input().split(',')]
count = 0
for i in range(len(list1)):
    string = list1[i]
    if(len(string) >= 3):
        if string[0] == string[-1]:
            count += 1
print(count)

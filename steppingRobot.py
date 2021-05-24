import math
list1 = [x for x in input().split(',')]
up1 = 0
down1 = 0
left1 = 0
right1 = 0
for i in list1:
    for j in range(1, len(list1)):
        if "up" in i:
            up1 = int(i[len(i) - 1])
        if "down" in i:
            down1 = int(i[len(i) - 1])
        if "right" in i:
            right1 = int(i[len(i) - 1])
        if "left" in i:
            left1 = int(i[len(i) - 1])
        else:
            break
b = math.sqrt(math.pow((up1 - down1), 2) + math.pow((left1-right1), 2))
print(b)

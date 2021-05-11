numeralList = [int(i) for i in input()]
JammyNumeral = len(numeralList)
count = 0
for i in range(0, JammyNumeral):
    if numeralList[i] == 4 or numeralList[i] == 7:
        count += 1
if count == JammyNumeral:
    print(True)
else:
    print(False)

num1 = int(input(""))
num2 = int(input(""))
list1 =[num1]
list2 =[num2]
while num1 >= 1:
    num1 = num1 // 2
    list1.append(num1)
    num2 = num2 * 2
    list2.append(num2)
a = 0
add = 0
while a < len(list1):
    if list1[a] % 2 == 0:
        add += 0
    else:
        add += list2[a]
    a += 1
print(add)

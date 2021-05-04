num1 = int(input(""))
num2 = int(input(""))
def sumofdiv(a):
    add = 0
    for i in range(1, a):
        if a % i == 0:
            add += i
    return add
list1 = []
for i in range(num1, num2, 1):
    num = sumofdiv(i)
    if num > i:
        if sumofdiv(num) == i:
            mytuple = (i, num)
            list1.append(mytuple)
print(list1)

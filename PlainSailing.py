string = str(input(""))
a = 0
b = 0
while a < len(string) - 1:
    if string[a] == '+' and string[a + 1] == '+':
        b += 1
    a += 1
if b == 0:
    print(True)
else:
    print(False)

string = str(input(""))
new_string = string.split(" ")
length = len(new_string)
count = 0
for i in range(0, length):
    if type(new_string[i]) == str and type(new_string[i + 1] == str):
        count= 1
        break
if count == 0:
    print(False)
else:
    print(True)

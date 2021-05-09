string = str(input(""))
list1 = list(string)
if string == "0":
    count = 0
else:
    count = 1
    for i in range(0, len(list1) - 1):
        str1 = ""
        str1 = int(str1.join(list1[i : i + 2]))
        if(str1 > 0 and str1 <= 26):
            count = count + 1
print(count)

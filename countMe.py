string = input().split()
length = len(string)
def countme(string):
    count = 0
    for i in range(0, length):
        if string[i] == "me":
            count += 1
    if (string[0] == "'me" or string[length - 1] == "me'"):
        count += 1
    return count
print(countme(string))

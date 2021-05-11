num = input()
num = int(num)
if (num == 1):
    print("1")
else:
    for i in range(2, num + 1):
        if (num % i == 0):
            break
    if num == 1:
        print(num)
    else:
        print(i)

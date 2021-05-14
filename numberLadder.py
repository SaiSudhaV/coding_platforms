number = int(input(""))
def value(number):
    num = 1
    for i in range(number):
        num = 1
        for j in range(i + 1):
            print(num, end = "")
            num += 1
        print("\r")
value(number)

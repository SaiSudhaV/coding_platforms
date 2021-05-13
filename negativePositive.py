num1 = int(input(""))
num2 = int(input(""))
num3 = bool(input(""))
def check(x, y, z):
    if x < 0 and y < 0 and z == True:
        return True
    elif x < 0 and y > 0 and z == False:
        return False
    elif x < 0 and y > 0 and z == False:
        return True
    elif x > 0 and y < 0 and z == True:
        return False
    elif x > 0 and y < 0 and z == False:
        return True
    elif x > 0 and y < 0 and z == True:
        return True
    else:
        return True
print(check(num1, num2, num3))

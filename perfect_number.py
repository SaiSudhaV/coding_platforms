num = int(input(""))
def is_perfect(num):
    i = 1
    add = 0
    while i < num:
        if num % i == 0:
            add += i
        i += 1
    if add == num:
        return True
    else:
        return False
print(is_perfect(num))

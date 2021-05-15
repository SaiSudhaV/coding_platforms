string = str(input(""))
def symbols(string):
    x = '''!@#$%^&*(){}[]|~_+-=:;'`"<>\,.?'''
    for i in string.lower():
        if i in x:
            string = string.replace(i, "")
    return string
print(symbols(string))

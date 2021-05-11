status = bool(input(""))
hours = int(input(""))
print(True) if (status == (0 < hours < 6) or status == (16 < hours < 0)) else print(False)

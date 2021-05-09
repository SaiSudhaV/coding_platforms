years = int(input(""))
res = -1
if years == 1:
    res = 10.5
elif years == 2:
    res = 21
elif years > 2:
    res = 21
    for i in range(1, years - 1):
        res = res + 4
        
print(res)

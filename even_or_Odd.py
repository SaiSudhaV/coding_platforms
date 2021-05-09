num = int(input(""))
squares_list = []
for i in range(1, num + 1):
    if i % 2 == 0:
        j = i * i
        squares_list.append(j)
    else:
        j = i * i * i
        squares_list.append(j)
print(squares_list)

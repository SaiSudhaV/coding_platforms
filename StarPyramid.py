a = int(input(""))
i = 1
print("Half pyramid")
print("\r")
while i <= a:
    j = 1
    while j <= i:
        print('*', end="")
        j += 1
    print("")
    i += 1
print("\r")

print("Full pyramid")
print("\r")
for i in range(0, a):
    for j in range(0, a - i - 1):
        print(' ', end="")
    for k in range(0, 2 * i + 1):
        print('*', end ="")
    print("")
print("\r")

print("Inverted pyramid")
print("\r")
for i in range(a, 0, -1):
    for j in range(a - 1, i - 1, -1):
        print(' ', end="")
    for k in range(2 * i - 1, 0, -1):
        print('*', end ="")
    print("")
print("\r")

print("\r")

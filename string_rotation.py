# 8. String rotation in special manner You are provided two or more strings, where each string is associated with the number (seperated by :).
# If sum of square of digits is even then rotate the string right by one position, and if sum of square of digits is odd then rotate the string left by two position.

def square_digits_sum(n):
    res = sum([int(i) ** 2 for i in n])
    return res % 2 == 0

def rotation(s, n, k):
    return s[-1] + s[: k- 1] if square_digits_sum(n) else s[2 : ] + s[:2]

if __name__ == "__main__":
    k = list(map(str, input().split(",")))
    for i in k:
        s, n = map(str, i.split(":"))
        print(rotation(s, n, len(s)))
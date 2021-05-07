# 6 Pronic Number
# Given a string of random numbers, your job is to find the product of the numbers(one is lesser and one is greater) who is already present in the string.
# For instance, a pronic number is a number which is the product of two consecutive integers, that is, a number of the form n(n + 1). Like 6 is the pronic number as 2*3 = 6.

def pronic_number(s, n):
    ar = [int(i) for i in s]
    res = [i * j for i in ar[:n - 1] for j in ar[1 : n] if j == i + 1 and str(i * j) in s]
    return res if res else -1

if __name__ == "__main__":
    s = input()
    print(pronic_number(s, len(s)))
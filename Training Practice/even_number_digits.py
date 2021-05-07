# 2 Given an array nums of integers, return how many of them contain an even number of digits.

def even_number_digits(n):
    return len(n) % 2 == 0

def count_even_number_digits(ar):
    return len([i for i in ar if even_number_digits(str(i))])

if __name__ == "__main__":
    n = int(input())
    ar = list(map(int, input().split()))
    print(count_even_number_digits(ar))
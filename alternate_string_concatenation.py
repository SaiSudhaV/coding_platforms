# 9. Consider a string, group the similar characters in combinations. Then, concatenate first element and last element alternatively.

from itertools import groupby

def rotation(s, n):
    k = s.casefold
    tem = ["".join(list(j)) for i, j in groupby(sorted(s))]
    return tem

if __name__ == "__main__":
    s = input()
    print(rotation(list(s), len(s)))
 def make_anagrams(A):
    n, my_dict = len(A), {}
    for i in range(n):
        tem = "".join(sorted(A[i]))
        if not my_dict.get(tem):
            my_dict[tem] = [i + 1]
        else:
            my_dict[tem].append(i + 1)
    return list(my_dict.values())
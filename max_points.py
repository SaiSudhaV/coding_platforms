#your code goes here 

from collections import defaultdict as def_dic

def max_points(ar, n):
    tem, gst = def_dic(int), max(ar)
    res = [0] * (gst + 1)
    for i in ar:
        tem[i] += 1
    res[0], res[1] = 0, tem[1]
    for i in range(2, gst + 1):
        res[i] = max(res[i - 2] + tem[i] * i, res[i - 1])
    return res[-1]

if __name__ == "__main__":
    n, ar = int(input()), list(map(int, input().split()))
    print(max_points(ar, n))
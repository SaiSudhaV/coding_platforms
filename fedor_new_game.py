# your code goes here

def binary_format(x):
    return bin(x)[2:]

def is_valid(ar, br, n, k):
    tem1, tem2, res = n - len(ar), n - len(br), 0
    if tem1 > 0:
        ar = '0' * tem1 + ar
    if tem2 > 0:
        br = '0' * tem2 + br
    for i in range(n):
        if ar[i] != br[i]:
            res += 1
    return 0 if res > k else 1
 
def capacity_compete(ar, n, m, k):
    count = 0
    for i in ar[:m]:
        if is_valid(binary_format(ar[m]), binary_format(i), n, k):
            count += 1
    return count
    
if __name__ == "__main__":
    n, m, k = map(int, input().split())
    ar = []
    for i in range(m + 1):
        ar.append(int(input()))
    print(capacity_compete(ar, n, m, k))
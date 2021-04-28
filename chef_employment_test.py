# cook your dish here

def greatest_median(ar, n, k):
    tem, res = max(ar), ar
    while k:
        tem += 1
        k -= 1
        res.append(tem)
    res.sort()
    m = len(res)
    return res[m // 2]
    
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        ar = list(map(int, input().split()))
        print(greatest_median(ar, n, k))
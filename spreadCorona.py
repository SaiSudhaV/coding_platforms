def spreadCorona(arr, n):
    res, flag, count = [], 0, 1
    for i in range(n - 1):
        if arr[i + 1] - arr[i] <= 2:
            count += 1
        else:
            res.append(count)
            count = 1
    res.append(count)
    return " ".join([str(i) for i in (min(res), max(res))])
    
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(spreadCorona(arr, n))

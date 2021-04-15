def arrangements(arr, n, t):
    if n > 1:
        for i in range(t):
            flag = False
            for i in range(n - 1):
                if flag:
                    flag = False
                    continue
                if arr[i] == 'B' and arr[i + 1] == 'G':
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    flag = True
    return ''.join(arr)
    
if __name__ == "__main__":
    n, t = map(int, input().split())
    arr = list(map(str, input().strip()))
    print(arrangements(arr, len(arr), t))

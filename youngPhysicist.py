def youngPhysicist(arr, m):
    sum1, sum2, sum3 = 0, 0, 0
    for i in range(n - 2):
        sum1, sum2, sum3 = sum(arr[i]), sum(arr[i + 1]), sum(arr[i + 2])
    return "YES" if sum1 == sum2 == sum3 == 0 else "NO"
    
if __name__ == '__main__':
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    print(youngPhysicist(arr, n))

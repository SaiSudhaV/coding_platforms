# cook your dish here
def subArray(arr, n):
    res = [1 for i in range(n)]
    tot = 0
    for i in range(n):
        if i - 1 >= 0 and arr[i] >= arr[i - 1]:
            res[i] = res[i - 1] + 1
        tot += res[i]
    return tot

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(subArray(arr, n))

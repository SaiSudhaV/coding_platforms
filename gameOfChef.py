def isContiguous(arr):
    n = len(arr)
    for i in range(1 ,n): 
        if (arr[i] - arr[i - 1] > 1) : 
            return False
    return True

def subLists(arr): 
    lst = [[]] 
    for i in range(len(arr) + 1): 
        for j in range(i + 1, len(arr) + 1): 
            subArray = arr[i : j] 
            lst.append(subArray) 
    return lst
    
def maxSum(arr):
    lst = [sum(i) for i in subLists(arr) if isContiguous(sorted(i))]
    return max(lst)
    
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        print(maxSum(arr))
# your code goes here
def largestRectangleArea(ar, n):
    temp, largest, count = ar[0], ar[0], 1
    for i in range(1, n):
        temp, count = min(temp, ar[i]), count + 1
        if count * temp < ar[i]:
            temp, count, largest = ar[i], 1, max(largest, ar[i])
        else:
            largest = max(largest, count * temp)
    return largest
 
if __name__ == "__main__":
    flag = True
    while flag:
        ar = list(map(int, input().split()))
        if ar[0] != 0:
            print(largestRectangleArea(ar, len(ar)))
        else:
            flag = False 
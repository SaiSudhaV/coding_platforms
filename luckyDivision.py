 def luckyDivision(n):
    res = False
    arr = [4, 7, 47, 74, 44, 444, 447, 474, 477, 777, 774, 744]
    for i in range(12):
        if n % arr[i] == 0:
            res = True
    return "YES" if res else "NO"

if __name__ == '__main__':
    n = int(input())
    print(luckyDivision(n))

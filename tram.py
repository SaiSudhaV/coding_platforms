def tram(lst, n):
    res, result = 0, []
    res = lst[0][1] - lst[0][0]
    result .append(res)
    for i in range(1, n):
        res = res - lst[i][0] + lst[i][1]
        result.append(res)
    return max(result)
 
if __name__ == '__main__':
    n, lst = int(input()), []
    for i in range(n):
        a, b = map(int, input().split())
        lst.append((a, b))
    print(tram(lst, n))

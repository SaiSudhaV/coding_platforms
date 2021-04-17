#your code goes here

def calculate(n, m, k):
    p, res = (2 * k), ""
    tem = p / (n + m)
    tem1 = (m - n) / (tem - 5)
    tem2 = ((p / tem) - (tem - 1) * tem1) / 2
    if i >= 1:
        s = "\n" + str(int(tem))
        print(s)
    else:
        s = str(int(tem))
        print(s)
    while tem >= 1:
        res += str(int(tem2)) + " "
        tem2 += tem1
        tem -= 1
    return res
    
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, m, k = map(int, input().split())
        print(calculate(n, m, k))
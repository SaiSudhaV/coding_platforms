if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = [int(j) for j in input().split()]
        res = 0
        a = 2
        k = 2 * a[0]
        for l in a[1:] :
            res = (2 * res) + (l * k)
            k = k + a * l
            a = (a * 2) % 1000000007
        print(res % 1000000007)
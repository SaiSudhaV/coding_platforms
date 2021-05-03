def wrongSubtraction(n, k):
    for  i in range(k):
        n = n / 10 if n % 10 == 0 else n - 1
    return int(n)

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(wrongSubtraction(n, k)) 

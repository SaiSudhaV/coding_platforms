def Elephant(n):
    return int(n / 5 if n % 5 == 0 else n / 5 + 1)

if __name__ == '__main__':
    n= int(input())
    print(Elephant(n))

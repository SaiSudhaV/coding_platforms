def twovsten(n):
    return 0 if n % 10 == 0 else 1 if n % 5 == 0 else -1
    
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(twovsten(n))
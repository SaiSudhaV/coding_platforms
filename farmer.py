# cook your dish here
def calculate(m, n):
    temp, res = 1, []
    while True:
        t = m + n + temp
        if prime(t):
            res.append(temp)
            break
        temp += 1
    return " ".join(str(i) for i in res)
    
def prime(n):
    for i in range(2,(n // 2) + 1):
        if n % i == 0:
            return False
    else:
        return True
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        m, n = map(int, input().split())
        print(calculate(m, n))

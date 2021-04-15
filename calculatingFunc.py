def cal_function(n):
    return n //2 if n % 2 == 0 else -(n + 1) // 2

if __name__ == '__main__':
    n = int(input())
    print(cal_function(n))

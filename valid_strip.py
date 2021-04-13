# cook your dish here

def valid_strip(ar, n):
    flag = True
    if n % 2 == 0:
        return "no"
    for i in range(n // 2 + 1):
        if ar[i] != i + 1 or ar[n - i - 1] != i + 1:
            flag = False
            break
    return "yes" if flag else "no"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        ar =list(map(int, input().split()))
        print(valid_strip(ar, n))
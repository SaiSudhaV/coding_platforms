# cook your dish here

def is_balanced(ar, n, p):
    tem1, tem2 = 0, 0
    for i in ar:
        if i <= p // 10:
            tem1 += 1
        elif i >= p // 2:
            tem2 += 1
    return "no" if p == 1 else "yes" if tem1 == 2 and tem2 == 1 else "no"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, p = map(int, input().split())
        ar = list(map(int, input().split()))
        print(is_balanced(ar, n, p))
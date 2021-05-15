# cook your dish here

def equal_sequence(ar, n):
    tem = {}
    for i in ar:
        tem[i] = tem.get(i, 0) + 1
    return n - max(tem.values())

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, ar = int(input()), list(map(int, input().split()))
        print(equal_sequence(ar, n))
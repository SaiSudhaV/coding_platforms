# cook your dish here

def calc(a1, a2, n):
    l = [i for i in range(1, n + 1)]
    tracked, untracked = len([i for i in a1 if i in a2]), len([i for i in l if i not in list(set(a1 + a2))])
    return " ".join(str(i) for i in [tracked, untracked])

if _name_ == "_main_":
    t = int(input())
    for i in range(t):
        n, m, k = map(int, input().split())
        a1, a2 = list(map(int, input().split())), list(map(int, input().split()))
        print(calc(a1, a2, n))
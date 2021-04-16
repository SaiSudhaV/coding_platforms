# cook your dish here

def solve(k):
    return 1 if k.count('he') > 0 or  k.count('ch') > 0 or  k.count('ef') > 0 else 0

if __name__ == "__main__":
    t = int(input())
    res = []
    for i in range(t):
        k = input()
        res.append(solve(k))
    print(sum(res))
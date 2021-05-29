# cook your dish here

def isPossible(s, n):
    res = []
    for i in s:
        if i not in res:
            res.append(i)
        else:
            res.remove(i)
    return "NO" if len(res) else "YES"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, s = int(input()), input()
        print(isPossible(s, n))
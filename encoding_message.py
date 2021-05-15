# cook your dish here

def encode(s, n):
    tem, res = [], []
    l1, l2 = "zyxwvutsrqponmlkjihgfedcba", "abcdefghijklmnopqrstuvwxyz"
    for i in range(0, n - 1, 2):
        tem.append(s[i + 1])
        tem.append(s[i])
    if n % 2:
        tem.append(s[-1])
    for i in tem:
        res.append(l1[l2.index(i)])
    return "".join(res)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, s = int(input()), input()
        print(encode(s, n))
# cook your dish here

def max_pairs_count(s, n):
    res, i = 0, 0
    while i < n - 1:
        if (s[i] == "x" and s[i + 1] == "y") or (s[i] == "y" and s[i + 1] == "x"):
            i, res = i + 2, res + 1
        else: 
            i += 1
    return res

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = input()
        print(max_pairs_count(s, len(s)))
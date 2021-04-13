# cook your dish here

def message(s, n, k):
    tem, tem1 = len([i for i in s if i.islower()]), len([i for i in s if i.isupper()])
    return "both" if tem <= k and tem1 <= k else "brother" if tem <= k else "chef" if tem1 <= k else "none"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        s = input()
        print(message(s, n, k))
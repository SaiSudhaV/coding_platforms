# cook your dish here

def gen_list(ar, n):
    res = []
    for i in range(n):
        tem = 0
        for j in range(i + 1, n):
            if ar[i] < ar[j]:
                tem += 1
        res.append(tem)
    return  " ".join(str(i) for i in res)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, ar = int(input()), list(map(int, input().split()))
        print(gen_list(ar, n))
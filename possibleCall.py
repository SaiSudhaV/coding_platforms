# cook your dish here

def possible_call(ar, n):
    tem, res = [], []
    for i in range(n):
        k = ar[i].index(" ")
        tem.append(ar[i][:k])
    for i in range(len(tem)):
        res.append(ar[i] if tem.count(tem[i]) > 1 else tem[i])
    return "\n".join(i for i in res)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        ar = [input() for i in range(n)]
        print(possible_call(ar, n))
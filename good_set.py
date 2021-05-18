# cook your dish here

def distinct_set(n):
    tem = [i for i in range(1, 500, 2)]
    res = [tem[i] for i in range(n)]
    return " ".join(str(i) for i in res)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print(distinct_set(n))
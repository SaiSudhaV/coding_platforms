# cook your dish here

def deleted_elements_sum(ar, n, k, v):
    tem, tot = (k + n) * v, sum(ar)
    t1, t2 = (tem - tot) // k, (tem - tot) % k
    return t1 if (t2 == 0) and (t1 not in ar) and (tem > tot) else -1

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, k, v = map(int, input().split())
        ar = list(map(int, input().split()))
        print(deleted_elements_sum(ar, n, k, v))
# cook your dish here

def gen_sequence(ar, n):
    res = []
    for i in ar:
        if i == min(ar) or i == max(ar):
            res.append(i)
    return " ".join(str(i) for i in [res[0], res[1]])

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, ar = int(input()), list(map(int, input().split()))
        print(gen_sequence(ar, n))
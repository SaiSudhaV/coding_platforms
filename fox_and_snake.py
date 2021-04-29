# your code goes here
 
def gen_pattern(n, k):
    res = []
    for i in range(n):
        rem = i % 4
        if rem == 0:
            res.append("#" * k)
        elif rem == 1:
            res.append("." * (k - 1) + "#")
        elif rem == 2:
            res.append("#" * k)
        elif rem == 3:
            res.append("#" + "." * (k - 1))
    return "\n".join(res)
 
if __name__ == "__main__":
    n, k = map(int, input().split())
    print(gen_pattern(n, k))
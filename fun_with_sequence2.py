#your code goes here

def gen_sequence(ar, n, br, m):
    tem1, tem2 = sum(ar), sum(br)
    return ar if tem1 > tem2 else br

if __name__ == "__main__":
    n = int(input())
    ar = list(map(int, input().split()))
    m = int(input())
    br = list(map(int, input().split()))
    print(" ".join(str(i) for i in gen_sequence(ar, n, br, m)))
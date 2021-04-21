#your code goes here

def gen_sequence(ar, n, br, m):
    k = min(n, m)
    res = [i + 1 for i in range(k) if ar[i] == br[i]]
    return res

if __name__ == "__main__":
    n = int(input())
    ar = list(map(int, input().split()))
    m = int(input())
    br = list(map(int, input().split()))
    print(" ".join(str(i) for i in gen_sequence(ar, n, br, m)))
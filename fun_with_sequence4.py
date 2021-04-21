#your code goes here

def gen_sequence(ar, n, br, m):
    res = [i for i in ar if i not in br]
    return res

if __name__ == "__main__":
    n = int(input())
    ar = list(map(int, input().split()))
    m = int(input())
    br = list(map(int, input().split()))
    print(" ".join(str(i) for i in gen_sequence(ar, n, br, m)))
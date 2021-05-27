# your code goes here

def evenness(ar, n):
    res = [i % 2 for i in ar]
    return res.index(sum(res) == 1) + 1

if __name__ == "__main__":
    n = int(input())
    ar = list(map(int, input().split()))
    print(evenness(ar, n))
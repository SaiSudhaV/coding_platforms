#your code goes here 

def findUnique(ar):
    res = int("".join([str(i) for i in ar if ar.count(i) == 1]))
    return ar.index(res) + 1

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        ar = list(map(int, input().split()))
        print(findUnique(ar))
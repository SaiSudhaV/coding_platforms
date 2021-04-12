def doesExist(ar, n):
    res = sum(ar)
    for i in ar: 
        if res - i in ar:
            return "No"
    return "Yes"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        ar = list(map(int, input().split()))
        print(doesExist(ar, n))
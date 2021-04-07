#your code goes here

def possiblePairsCount(ar1, n1, ar2, n2):
    count = 0
    for i in ar1:
        for j in ar2:
            if i - j in range(-1, 2) :
                ar2.remove(j)
                count += 1
                break
    return count

if __name__ == "__main__":
    n1, ar1 = input(), list(map(int,input().split()))
    n2, ar2 = input(), list(map(int,input().split()))
    print(possiblePairsCount(sorted(ar1), n1, sorted(ar2), n2))
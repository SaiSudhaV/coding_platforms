#your code goes here

def max_poss(n, a, b, c):
    tem, res = [a, b, c], [0 for i in range(n + 1)]
    for i in range(len(res)):
        var = 0
        for j in range(len(tem)):
            if tem[j] <= i and res[i - tem[j]] + 1 > var:
                if i - tem[j] != 0 and res[i - tem[j]] == 0:
                    continue
                var = res[i - tem[j]] + 1
        res[i] = var
    return res[n]

if __name__ == "__main__":
    n, a, b, c = map(int, input().split())
    print(max_poss(n, a, b, c))
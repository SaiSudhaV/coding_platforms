def solve(A, tem, p, res):
    varlist, n = list(tem), len(A)
    res.append(varlist)
    for i in range(p, n):
        if i > p and A[i] == A[i - 1]:
            continue
        else:
            tem.append(A[i])
            solve(A, tem, i + 1, res)
            tem.pop()
    return
    
def subsets(A):
    res = []
    solve(sorted(A), [], 0, res)
    res = [" ". join(str(i) for j in res for i in j)]
    return "\n".join(i for i in res)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        ar = list(map(int, input().split()))
        print(subsets(ar))
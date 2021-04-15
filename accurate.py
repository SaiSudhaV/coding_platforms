def accuracy_check(A, B):
    res = []
    for i in range(len(A)):
        res.append(1 if A[i] != B[i] else 0)
    return "".join(str(i) for i in res)
    
if __name__ == "__main__":
    A = input()
    B = input()
    print(accuracy_check(A, B))

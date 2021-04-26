def concat(A):
    idx, res = len(A) - 1, 0
    while A[idx] == "9":
        res, idx = res + 1, idx - 1
        if idx < 0:
            return "1" + "0" * res
    return A[:idx] + str(int(A[idx]) + 1) + "0" * res
def divide(A):
    mid = len(A) // 2
    return A[: mid], A[mid : -mid], A[-mid :]

def sol(A):
    if len(A) == 1:
        return "11" if A == "9" else int(A) + 1
    left, middle, right = divide(A)
    if left[::-1] > right:
        return left + middle + left[::-1]
    A = concat(left + middle) + "0" * len(right)
    left, middle, right = divide(A)
    if left[::-1] > right:
        return left + middle + left[::-1]
    
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        A = input()
        print(sol(A))

# cook your dish here

def palin_substring(A, B):
    flag = False
    for i in A:
        if i in B:
            flag = True
            break
    return "Yes" if flag else 'No'

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        A = str(input())
        B = str(input())
        print(palin_substring(A, B))

def average(A, n):
    return sum(A) / n
    
if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    print(float(average(A, n)))

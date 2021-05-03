if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    print(" ".join(str(i) for i in sorted(A)))

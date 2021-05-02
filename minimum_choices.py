def unique_colors(A):
    return 4 - len(A)
    
if __name__ == "__main__":
    A = list(map(int, input().split()))
    print(unique_colors(set(A)))

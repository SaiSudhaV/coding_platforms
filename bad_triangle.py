# your code goes here

def impossible_triangle_coordinates(ar, n):
    res = "1 2 "
    return -1 if (ar[0] + ar[1]) > ar[n - 1] else "".join(str(i) for i in [res, n])
    
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        ar = list(map(int, input().split()))
        print(impossible_triangle_coordinates(sorted(ar), n))
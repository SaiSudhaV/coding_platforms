# your code goes here

def min_pushes(n, m):
    count = 0
    while not n == m:
        count += 1
        m = m + 1 if m & 1 or m < n else m // 2
    return count

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(min_pushes(n, m))
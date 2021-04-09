# cook your dish here

def swap(a, b):
    return b, a
    
def largestNumber(ar, n):
    idx = ar.index(n - 1)
    ar[0], ar[idx] = swap(ar[0], ar[idx])
    return max(ar[1:])

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        ar = list(map(int, input().split()))
        print(largestNumber(ar, len(ar)))
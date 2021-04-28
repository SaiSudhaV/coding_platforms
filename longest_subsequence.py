# your code goes here

def longest_subsequence(ar):
    return len(ar)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        ar = list(map(int, input().split()))
        print(longest_subsequence(set(ar)))
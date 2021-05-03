from itertools import combinations as comb

def sumOfOddIntegers(n, m):
    oddNums = [i for i in range(n + 1) if i % 2 != 0]
    res = [sum(i) for i in comb(oddNums, m) if sum(i) == n]
    return "YES" if res else "NO"

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        print(sumOfOddIntegers(n, m))
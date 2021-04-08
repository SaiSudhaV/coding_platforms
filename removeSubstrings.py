def subStringRemoval(s):
    return sum(s[::-2])
 
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = map(len, input().split('0'))
        print(subStringRemoval(sorted(s)))
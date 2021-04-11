def evenSplit(n):
    return "Yes" if n % 4 == 0 else "No"
    
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print(evenSplit(n))

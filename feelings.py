def feeling(n):
    res = []
    for i in range (1, n + 1):
        res.append("I love it" if n == i and i % 2 == 0 else "I love that" if i % 2 == 0 else "I hate it" if n == i else "I hate that")
    return " ".join(str(i) for i in res)
    
if __name__ == "__main__":
    n = int(input())
    print(feeling(n))

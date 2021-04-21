def helpfulMaths(n):
    result = n[::2]
    result = sorted(result)
    return '+'.join(result)

if __name__ == "__main__":
    inputStr =input()
    print(helpfulMaths(inputStr))
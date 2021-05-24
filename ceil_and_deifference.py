# cook your dish here

def mistake(n):
    n = str(n)
    return '9' + n[1:] if n[0] == '1' else '1' + n[1:]

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(mistake(n - k))
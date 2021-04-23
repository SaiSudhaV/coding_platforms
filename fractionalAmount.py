def fractionalAmount(a, b, c, d):
    return "YES" if a == b else "NO" if c == d else "YES" if abs(a - b) % abs(c - d) == 0 else "NO"
		
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b, c, d = map(int, input().split())
        print(fractionalAmount(a, b, c, d))

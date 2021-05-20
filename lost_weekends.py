# cook your dish here

def check_possibility(a, b, c, d, e):
    return "Yes" if sum([a, b, c, d, e]) > 120 else "No"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a, b, c, d, e, k = map(int, input().split())
        print(check_possibility(a * k, b * k, c * k, d * k, e * k))
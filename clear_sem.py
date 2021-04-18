# cook your dish here

def will_pass(am, bm, cm, tm, a, b, c):
    if a < am or b < bm or c < cm:
        return "NO"
    if a + b + c < tm:
        return "NO"
    return "YES"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        am, bm, cm, tm, a, b, c = map(int, input().split())
        print(will_pass(am, bm, cm, tm, a, b, c))
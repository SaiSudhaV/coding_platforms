# cook your dish here

def best_recipe(a, b, c, d, e):
    tem1, tem2 = abs(c - a) / d, abs(c - b) / e
    return "Chef" if tem1 < tem2 else "Kefa" if tem2 < tem1 else "Draw"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a, b, c, d, e = map(int, input().split())
        print(best_recipe(a, b, c, d, e))
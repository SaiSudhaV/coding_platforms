# cook your dish here

def is_possible(x, y, z):
    return "yes" if x + y == z or y + z == x or z + x == y else "no"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        print(is_possible(a, b, c))
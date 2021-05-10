# cook your dish here

def calculate_amount(a, b, x):
    return (b + (100 - a) * x ) * 10

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a, b, x = map(int, input().split())
        print(calculate_amount(a, b, x))
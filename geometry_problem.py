# your code goes here

def calculate_length(a, b, c):
    return  2 * b - c - a

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        print(calculate_length(a, b, c))
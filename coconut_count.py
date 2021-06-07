# cook your dish here

def find_coconuts_count(x, y, X, Y):
    return (X // x) + (Y // y)
    
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        x, y, X, Y = map(int, input().split())
        print(find_coconuts_count(x, y, X, Y))
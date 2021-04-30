# cook your dish here

def repeat_count(m, s):
    return m // s 

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        m, s = map(int, input().split())
        print(repeat_count(m, s))
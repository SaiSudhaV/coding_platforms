# cook your dish here

def check_possibility(ar, p):
    return "Yes" if sum([i * p for i in ar]) == 120 else "No"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        ar = list(map(int, input().split()))
        print(check_possibility(ar[: 4], ar[-1]))
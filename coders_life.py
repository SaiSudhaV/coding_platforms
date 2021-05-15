# cook your dish here

def solve(s):
    return "#allcodersarefun" if "111111" not in s else "#coderlifematters"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = input().split(" ")
        print(solve("".join(s)))
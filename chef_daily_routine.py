# cook your dish here

def correctness(s):
    return "no" if 'SC' in  s or 'SE' in s or 'EC' in s else "yes"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s = input()
        print(correctness(s))
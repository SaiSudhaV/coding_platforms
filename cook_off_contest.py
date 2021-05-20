# cook your dish here

def possible_set(ar, n):
    res = []
    if ar.count("cakewalk") == 1 and ar.count("simple") == 1 and ar.count("easy") == 1 and (ar.count("hard") == 1 or ar.count("medium-hard") == 1) and (ar.count("medium") == 1 or ar.count("easy-medium") == 1):
        return "Yes"
    return "No"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, ar = int(input()), []
        for i in range(n):
            ar.append(input())
        print(possible_set(ar, n))
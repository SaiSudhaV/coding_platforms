# cook your dish here

def possible_set(ar, n):
    res = [0] * n
    for i in ar:
        if i == "easy":
            res[0] = 1
        elif i == "cakewalk":
            res[1] = 1
        elif i == "simple":
            res[2] = 1
        elif i == "medium-hard" or i == "hard":
            res[3] = 1
        elif i == "easy-medium" or i == "medium":
            res[4] = 1
    return "Yes" if res.count(1) == 5 else "No"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, ar = int(input()), []
        for i in range(n):
            ar.append(input())
        print(possible_set(ar, n))
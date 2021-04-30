# cook your dish here

def who_win(ar, a, b):
    score1, score2 = 0, 0
    for i in ar:
        if i[0] in "EQUINOX":
            score1 += a
        else:
            score2 += b
    return "SARTHAK" if score1 > score2 else "ANURADHA" if score2 > score1 else "DRAW"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, a, b = map(int, input().split())
        ar = []
        for i in range(n):
            ar.append(input())
        print(who_win(ar, a, b))
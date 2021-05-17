# cook your dish here

def is_valid(ar):
    player1, player2 = 0, 0
    for i in ar:
        if i == 'X':
            player1 += 1
        if i == 'O':
            player2 += 1
    total = 9 - (player1 + player2)
    if player1 > player2 + 1 or player1 < player2:
        return 3
    tem1, tem2 = check_board(ar, 'X'), check_board(ar, 'O')
    if (tem1 == 1 and tem2 == 1) or (tem1 == 1 and player1 == player2) or (tem2 == 1 and player1 > player2):
        return 3
    if tem1 == 1 or tem2 == 1:
        return 1
    return 2 if total != 0 else 1

def check_board(ar, k):
    if (ar[0] == k and ar[0] == ar[1] and ar[0] == ar[2]) or (ar[0] == k and ar[0] == ar[3] and ar[0] == ar[6]):
        return 1
    if (ar[0] == k and ar[0] == ar[4] and ar[0] == ar[8]) or (ar[1] == k and ar[1] == ar[4] and ar[1] == ar[7]):
        return 1
    if (ar[2] == k and ar[2] == ar[4] and ar[2] == ar[6]) or (ar[2] == k and ar[2] == ar[5] and ar[2] == ar[8]):
        return 1
    if (ar[3] == k and ar[3] == ar[4] and ar[3] == ar[5]) or (ar[6] == k and ar[6] == ar[7] and ar[6] == ar[8]):
        return 1
    return 0

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        ar = []
        for i in range(3):
            s = input()
            ar.append(s[0])
            ar.append(s[1])
            ar.append(s[2])
        print(is_valid(ar))
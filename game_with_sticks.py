# your code goes here

def who_win(ar):
    res = min(ar)
    return 'Malvika' if res % 2 == 0 else 'Akshat'

if __name__ == "__main__":
    ar = list(map(int, input().split()))
    print(who_win(ar))
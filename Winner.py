def who_win(n):
    return "Santa" if n % 6 else "Banta"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print("Santa" if n % 6 else "Banta")
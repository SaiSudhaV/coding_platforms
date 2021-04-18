#your code goes here

def choose_team(ar, n, k):
    res = [1 for i in ar if k <= 5 - i]
    return sum(res) // 3

if __name__ == "__main__":
    n, k = map(int, input().split())
    ar = list(map(int, input().split()))
    print(choose_team(ar, n, k))
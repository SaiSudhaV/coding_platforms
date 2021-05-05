#your code goes here

def sum_total_entrance_fees(ar, br):
    if ar[0] < br[1]:
        return "Y"
    elif ar[0] == br[0]:
        return "N" if br.count(br[0]) >= 2 else "Y"
    elif ar[0] <= br[0]:
        return "Y"
    return "N"

if __name__ == "__main__":
    while True:
        n = input()
        if n != "0 0":
            ar, br = list(map(int, input().split())), list(map(int, input().split()))
            print(sum_total_entrance_fees(sorted(ar), sorted(br)))
        else:
            break
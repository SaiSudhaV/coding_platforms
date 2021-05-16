# cook your dish here

def calculate_score(ar, br, n):
    for i in range(n):
        for j in range(i + 1, n):
            if ar[i] == ar[j]:
                if br[i] <= br[j]:
                    br[i] = 0
                else:
                    br[j] = 0
    return sum(br)

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n =  int(input())
        ar, br = [], []
        for i in  range(n):
            p, s = map(int, input().split())
            if p <= 8:
                ar.append(p)
                br.append(s)
        print(calculate_score(ar, br, len(ar)))
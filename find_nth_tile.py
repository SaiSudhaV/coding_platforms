#your code goes here 

def calculate(n):
    tem = [1, 1, 5, 11, 36, 95, 281, 781, 2245, 6336, 18061, 51205, 145601, 413351, 1174500, 3335651, 9475901, 26915305, 76455961, 217172736, 616891945, 1752296281]
    return tem[n]

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        res = [i + 1, 0] if n == 0 else [i + 1, calculate(n)]
        print(" ".join(str(i) for i in res))
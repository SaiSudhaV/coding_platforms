# your code goes here

def special_string(ar, n):
    for i in range(3, 31):
        ar.append(2 * ar[n - 1] + ar[n - 2])
    return ar[n]

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print(special_string([0, 3, 9], n))
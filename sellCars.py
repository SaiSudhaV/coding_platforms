#Sell All the Cars

def carsSell(arr, n):
    temp = sorted(arr)
    return sum([temp[i] - i] for i in range(n) if i - temp[i] < 0) % 1000000007
    
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(carsSell(list(map(int, input().split())), n))

def carsSell(arr, n):
    temp = sorted(arr)[::-1]
    return sum([temp[i] - i for i in range(n) if i - temp[i] < 0]) % 1000000007
    
if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        print(carsSell(list(map(int, input().split())), n))
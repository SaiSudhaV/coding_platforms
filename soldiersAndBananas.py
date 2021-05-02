def soldiersAndBananas(a, b, c):
    res = sum(list(i * a for i in range(1, c + 1)))
    return res - b if res > b else 0
    
if __name__ == '__main__':
    price, dollars, bananasreq = map(int, input().split())
    print(soldiersAndBananas(price, dollars, bananasreq))
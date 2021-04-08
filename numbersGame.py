# your code goes here

def win(n):
    return "2" if n % 10 == 0 else "1\n%d" % (n % 10)
    
if __name__ == "__main__":
    n = int(input())
    print(win(n))
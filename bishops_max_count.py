# your code goes here
 
def bishops_max_count(n):
    if n == 1:
        res = 1
    elif n > 1:
        res = (n - 1) * 2
    return res
 
if __name__ == "__main__":
    for i in range(1024):
        n = int(input())
        print(bishops_max_count(n)) 
# your code goes here
 
from math import log
 
def calculate_length(n):
    return log(n) / log(2)
 
if __name__ == "__main__":
    while True:
        n = int(input())
        if n != 0:
            print(int(calculate_length(n)))
        else:
            break 
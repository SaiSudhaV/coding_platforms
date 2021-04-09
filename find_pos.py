# your code goes here

import math

def calculate_position(n):
    log_val = math.log(n, 2)
    tem = 2 ** int(log_val)
    return (n - tem) * 2 + 1

if __name__ == "__main__":
    while 1:
        n = float(input())
        if n != 0:
            print('%d' % (calculate_position(n)))
        else:
            break
        
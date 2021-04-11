def find_set_bits_count(n):
    res = 0
    while n != 0:
        res += 1
        n &= n << 1
    return res
    
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print(find_set_bits_count(n))

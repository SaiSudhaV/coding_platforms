# your code goes here
 
def max_state(n):
    a, b = int(n), n[:-1]
    c = int(b[:-1] + n[-1])
    return max(a, int(b), c)
 
 
if __name__ == "__main__":
    n = input()
    print(max_state(n))

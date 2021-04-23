#your code goes here
 
def exponent_2_sum(n):
    k = 505
    res = [0] * k
    res[0] = 2
    for i in range(1, k):
        res[i] = res[i - 1] * 2
    return res[n] % 1298074214633706835075030044377087 - 1
 
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print(exponent_2_sum(n)) 
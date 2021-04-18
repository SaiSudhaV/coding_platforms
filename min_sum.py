#your code goes here
 
def min_sum(a, b, c, d):
    res = [a * c, -a // b * -d, a // b * d + a % b * c]
    return min(res)
 
if __name__ == "__main__":
    a, b, c, d = map(int, input().split())
    print(min_sum(a, b, c, d))
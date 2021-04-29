# your code goes here
 
def error_count(n, a, b, c):
    res = [sum(a) - sum(b), sum(b) - sum(c)]
    return "\n".join(str(i) for i in res)
 
if __name__ == "__main__":
    n, a = int(input()), list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(error_count(n, a, b, c))
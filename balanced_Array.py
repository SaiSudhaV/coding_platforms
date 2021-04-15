#your code goes here 
 
def construct_array(n):
    tem1, tem2 = [2 * i for i in range(1, n // 2 + 1)], [2 * i + 1 for i in range(n // 2 + 1) if i != n // 4]
    res = [*tem1, *tem2]
    return "NO" if n % 4 != 0 else "YES\n" + " ".join(str(i) for i in res)
 
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print(construct_array(n))
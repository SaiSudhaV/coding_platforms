def is_ordinary(n):
    res = [i for i in n]
    return len(set(res)) == 1
 
def count_ordinary_numbers(n):
    ordinary_numbers = [i for i in range(1, n + 1) if is_ordinary(str(i))]
    return len([i for i in ordinary_numbers if i <= n])
    
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print(count_ordinary_numbers(n))
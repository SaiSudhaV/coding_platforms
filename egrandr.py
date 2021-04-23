def egrandr(lst, n):
    score = sum(lst) / n
    count = 0
    for i in lst:
        if i <= 2:
            return "No"
        if i == 5:
            count += 1
    if count >= 1:
        if score < 4:
            return "No"
        return "Yes"
    return "No"
    
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        print(egrandr(a, n))
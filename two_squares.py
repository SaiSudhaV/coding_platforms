def valid_two_squares(n):
    i = 2
    while (i ** 2 <= n):
        count = 0
        if n % i == 0:
            while n % i == 0:
                count += 1
                n /= i
            if n % 4 == 4 and count % 2 != 0:
                return "No"
        i += 1
    return "Yes" if n % 4 !=3 else "No"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print(valid_two_squares(n))
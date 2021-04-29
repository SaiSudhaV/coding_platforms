# your code goes here

def div(A, n):
    return A // n

def rem(A, n):
    return A % n

def min_bills_count(n):
    res = div(n, 100) + div(rem(n, 100), 20) + div(rem(n, 20), 10) + div(rem(n, 10), 5) + rem(n, 5)
    return res

if __name__ == "__main__":
    n = int(input())
    print(min_bills_count(n))
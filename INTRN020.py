def is_prime(n):
    if n in [2, 3, 5, 7]:
        return True
    if n % 2 == 0:
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True

LIMIT = int(input())

def prime_list():
    return [i for i in range(1, 1000) if is_prime(i)]

def primes_range(LIMIT):
    list_of_primes = prime_list
    for i in range(LIMIT):
        print(list_of_primes[i])

primes_range(LIMIT)

from math import gcd

def cpFact(self, A, B):
    while True:
        if gcd(A, B) != 1:
            A //= gcd(A, B)
        else:
            return A
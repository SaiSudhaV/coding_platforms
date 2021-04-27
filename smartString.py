import numpy

def smartString(n, q, d, x):
    temp = numpy.prod(d)
    return " ".join(str(i) for i in [i // temp for i in x])
    
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, q = map(int, input().split())
        d = list(map(int, input().split()))
        x = list(map(int, input().split()))
        print(smartString(n, q, d, x))

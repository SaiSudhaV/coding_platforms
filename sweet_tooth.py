fib = [1, 2]
l = 2
def search(key, start, stop):
    mid = (start+stop)//2;
    
    if(fib[mid]<=key and (fib[len(fib)-1] == key or fib[mid+1]>key)):
        return mid+1;
    elif(fib[mid]< key):
        return search(key, mid+1, stop)
    else:
        return search(key, start, mid-1)
    
t = int(input())

for _ in range(t):
    n = int(input())
    c = int(input())
    
    if n <= fib[l-1]:
        print(search(n, 0, l-1)*c)
    else:
        while fib[l-1] < n:
            fib.append(fib[l-1]+fib[l-2])
            l += 1
        print((l-1)*c)

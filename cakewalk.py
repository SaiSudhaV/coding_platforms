import math
def reverse(s): 
    if len(s) == 0: 
        return s
    return reverse(s[1:]) + s[0]
    
def Log2(x): 
    if x == 0: 
        return false; 
    return (math.log10(x) / math.log10(2))

def isPowerOfTwo(n): 
    return (math.ceil(Log2(n)) == math.floor(Log2(n))); 
t = int(input())
for x in range (t):
    n = input()
    pos =0
    
    t = reverse(n)
    for k in range(0,len(t)):                                                                                       
        if t[k]!=0:
            pos = k
            break        

    print(pos)
    z = len(n)-pos
    
    a = n[0:z]
    a = int(a)
    if isPowerOfTwo(a):
        p=Log2(a)
        if len(n)-z >p:
            print("Yes")
        else:
            print("No")
    else:
        print("No")                                                                                     

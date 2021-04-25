from itertools import combinations as ncr
t=int(input())
for i in range(t):
    s=input().split()
    n=int(s[0])
    r=int(s[1])
    lst=list(map(int,input().split()))
    comb=ncr(lst,r)
    
    l=[sum(i) for i in comb]
    res=min(l)
    print(l.count(res))

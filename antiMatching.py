def get():
    return [ int(x) for x in input().split() ]

import sys

def detectTriangle(adj):
    for x in range(len(adj)):
        for y in adj[x]:
            if not set(adj[x]).isdisjoint(adj[y]):
                return True
            
for _ in range( int(input()) ):
    n, m = get()
    
    adj = [ [] for _ in range(n) ] 
    for _ in range(m):
        src, dest = get()
        src -= 1
        dest -= 1
        
        adj[src].append(dest)
        adj[dest].append(src)
        
    max_degree = max( [len(a) for a in adj] )
    
    if( max_degree >= 3 ):
        print(max_degree)
        continue
    if detectTriangle(adj):
        print(3)
        continue
    
    print(max_degree)                

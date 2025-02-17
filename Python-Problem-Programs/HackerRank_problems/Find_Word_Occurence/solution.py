from collections import defaultdict

n,m=(map(int,input().split()))
a=[input() for x in range(n)]
b=[input() for x in range(m)]
counts=defaultdict(list)

for char in b:
    indices=[i+1 for i in range(n) if a[i]==char]
    
    counts[char]=indices if indices else [-1]

for i in b:              
    print(*counts[i],end='\n')



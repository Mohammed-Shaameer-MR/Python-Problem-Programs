from itertools import combinations
import sys

s,r=(x for x in sys.stdin.read().split())
s=sorted(s)
r=int(r)
result=[]
for i in range(1,r+1):
    result.extend([''.join(x) for x in combinations(s,i)])

print(*result,sep='\n')

from itertools import permutations
import sys

s,k=(x for x in sys.stdin.read().split())
s=sorted(s)
k=int(k)
result=[''.join(x) for x in permutations(s,k)]
print(*result,sep='\n')

from itertools import combinations
import sys

n,s,k=(x for x in sys.stdin.read().splitlines())
n,k=int(n),int(k)
s=[i for i in s.split()]
combs=[x for x in combinations(s,k)]
result=[i for i in combs if 'a' in i ]

print(f"{len(result)/len(combs):.3f}")

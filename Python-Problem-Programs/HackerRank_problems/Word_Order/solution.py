import sys
from collections import Counter

n=int(input())
words=sys.stdin.read().splitlines()
words=Counter(words)

print(len(words))
for keys,values in words.items():
    print(values,end=' ')

import sys

k,m=(int(x) for x in sys.stdin.readline().split())
klist=[x for x in sys.stdin.read().splitlines()]
mlist=[[int(i) for i in x.split()] for x in klist]
n=[i[0] for i in mlist]
lists=[i[1:] for i in mlist]

sums={0}
for i in lists:
    temp={y**2 for y in i}
    sums={x+y for x in sums for y in temp}
    sums={x%m for x in sums}

print(f"{max(sums)}") 

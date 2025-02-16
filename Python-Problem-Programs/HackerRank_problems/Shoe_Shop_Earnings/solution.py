from collections import Counter 

x=int(input())
sizes=list(map(int,input().split()))
n=int(input())
billings=list(tuple(map(int,input().split()))for _ in range(n))
avail=Counter(sizes)

sp=0
for size,price in billings:
    if avail[size]>0:
        sp+=price
        avail[size]-=1
    
print(sp)

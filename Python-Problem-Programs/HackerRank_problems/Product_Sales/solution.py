from collections import OrderedDict
import sys

n=int(input())
products=OrderedDict()
data=sys.stdin.read().splitlines()

for lines in data:
    name,price=lines.rsplit(" ",1)  #splits from right once
    if name not in products:    
        products[name]=int(price)
    else:
        products[name]+=int(price)
        
print(*[f"{keys} {values}" for keys,values in products.items()],sep='\n')
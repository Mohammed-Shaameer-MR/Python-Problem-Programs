from itertools import groupby

s=input()
comp=[(len(list(groups)),int(key)) for key,groups in groupby(s)]
print(*comp,sep=' ')

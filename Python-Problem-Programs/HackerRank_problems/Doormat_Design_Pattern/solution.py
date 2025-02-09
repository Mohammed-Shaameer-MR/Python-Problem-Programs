line=input().strip().split(' ')
n,m=tuple(int(l) for l in line)

welcome='WELCOME'

#Upper part
for i in range(n//2):
    print(('.|.'*(2*i+1)).center(m,'-')) #Repeating '.|.' for odd no of times per each iteration
        
#Middle Part
print(welcome.center(m,'-'))

#Lower part
for i in range(n//2,0,-1):
    print(('.|.'*(2*i-1)).center(m,'-'))
    
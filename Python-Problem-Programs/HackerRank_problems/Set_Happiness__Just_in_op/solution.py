import sys

#Get the data
n,m=(int(x) for x in input().strip().split(' '))
arr=[int(x) for x in sys.stdin.readline().split()]
like={int(x) for x in sys.stdin.readline().split()}
unlike={int(x) for x in sys.stdin.readline().split()}

#Happiness container
happy=0

#Checking for happiness
for i in arr:
    if i in like:
        happy+=1
    elif i in unlike:
        happy-=1
    else:
        continue

#Display Happiness
print(happy)
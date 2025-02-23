from collections import deque
import sys

n=int(input())
cmds=sys.stdin.read().splitlines()
dq=deque([])

for cmd in cmds:
    temp=cmd.split()
    if "append" in temp:
        dq.append(int(temp[1]))
    elif "appendleft" in temp:
        dq.appendleft(int(temp[1]))
    elif "pop" in temp:
        dq.pop()
    elif "popleft" in temp:
        dq.popleft()
        
print(*dq,sep=' ')
